#!/bin/bash
# run on adcmon.cern.ch

# adcmon
WORKDIR=/data/jschovan/PandaBrokerageMon/verify_values
PUBDIR=/var/www/html/PandaBrokerageMon/verify_values
# lxplus
WORKDIR=/afs/cern.ch/user/j/jschovan/scratch0/PandaBrokerageMon/verify_values
PUBDIR=${WORKDIR}/pub

LOGDIR=${WORKDIR}/logs
DATESTRING=$(date +%F.%H%M%S)
INDEX=${PUBDIR}/index.html

mkdir -p ${LOGDIR} ${PUBDIR}

cd ${WORKDIR}

echo "Running at ${DATESTRING}."

# get data from DB
/usr/bin/time python verifyDB.py ${WORKDIR} 2>&1 | tee ${LOGDIR}/log.verifyDB.${DATESTRING}

# process data
/usr/bin/time python verify_values.py ${WORKDIR} 2>&1 | tee ${LOGDIR}/log.verify_values.${DATESTRING}

# publish data
cp ${WORKDIR}/DAILYLOGV2.py ${PUBDIR}/DAILYLOGV2.py
cp ${LOGDIR}/log.verify_values.${DATESTRING} ${PUBDIR}/log.verify_values.txt

# bzip files
bzip2 ${LOGDIR}/log.verifyDB.${DATESTRING} ${LOGDIR}/log.verify_values.${DATESTRING}

# create index
cd ${PUBDIR}
echo -n >${INDEX}
for file in $(ls . | grep -v "index.html"); 
do
    lsl=$(ls -l $file)
    html="<div>$(echo $lsl | sed -e "s#$file#<a href=\"./$file\">$file</a>#g" | awk '{printf $5 " " $6 " " $7 " " $8 " " $9 " " $10;}')</div>"
    echo $html >> ${INDEX}
done


