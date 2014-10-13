#!/bin/bash
#source /home/ookey/workspace/PandaBrokerageMonitor/pbm_profile
#cd /home/ookey/workspace/PandaBrokerageMonitor

#set -x
PYTHON_EXECUTABLE="/usr/bin/python2.5"


source /data/adcpbm1/PandaBrokerageMonitor/PandaBrokerageMonitor.conf
#source ${WORKDIR}/pbm_profile
WORKDIR=/data/adcpbm1/PandaBrokerageMonitor/helpers/copy_data
TMP_DIR=${WORKDIR}/tmp
source /afs/cern.ch/project/oracle/script/setoraenv.sh -s prod
cd ${WORKDIR}

mkdir -p ${TMP_DIR} ${WORKDIR}/logs

TIMESTAMP=$(date '+%F %T' -u)

export PYTHONPATH=${PYTHONPATH}:/data/adcpbm1/dump.2012-10-13/verify_values/work

LOGFILE=${WORKDIR}/logs/copy_data.log
date >> ${LOGFILE}
${PYTHON_EXECUTABLE} ${WORKDIR}/copy_data.py >> ${LOGFILE} 2>&1

### cleanup the PID file
PIDFILE=/tmp/adcpbm1/pbm_pidfile_copy_data 
if [ -f "${PIDFILE}" ]; then 
	mypid=$(cat ${PIDFILE} )
	if [ -z "$(ps ux | awk '{print $2;}' | grep ${mypid})" ]; then
		echo "Found file ${PIDFILE}, but the process is not running. Will delete ${PIDFILE} ."
		rm ${PIDFILE}
	fi
fi


### Deal with unresolved filesystems
if [ -f "${PIDFILE}" ]; then 
### mail to ADMIN
    ADMIN="adcpbm1@cern.ch"
    echo -e "$(basename $0) INFO [${TIMESTAMP} UTC] Please check logs and remove PIDfile (/tmp/adcpbm1/pbm_pidfile)" | mail -s "[PandaBrokerageMonitor] $(basename $0) - PID file stale lock" ${ADMIN} 
fi

# ${PYTHON_EXECUTABLE} ${WORKDIR}/my_logfileV2.py > /dev/null 2>&1


