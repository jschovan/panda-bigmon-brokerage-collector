#!/bin/bash
#source /home/ookey/workspace/PandaBrokerageMonitor/pbm_profile
#cd /home/ookey/workspace/PandaBrokerageMonitor

#set -x
PYTHON_EXECUTABLE="/usr/bin/python2.5"

source /data/adcpbm1/PandaBrokerageMonitor/PandaBrokerageMonitor.conf
source ${WORKDIR}/pbm_profile
cd ${WORKDIR}

mkdir -p ${TMP_DIR}

TIMESTAMP=$(date '+%F %T' -u)


date >> ${WORKDIR}/logs/PBMonV2.log
${PYTHON_EXECUTABLE} ${WORKDIR}/parse_analy_brokerage_logV2.py >> ${WORKDIR}/logs/PBMonV2.log 2>&1
mypid="0"
### cleanup the PID file
PIDFILE=/tmp/adcpbm1/pbm_pidfile 
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

${PYTHON_EXECUTABLE} ${WORKDIR}/my_logfileV2.py > /dev/null 2>&1

