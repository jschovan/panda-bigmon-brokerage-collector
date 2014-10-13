#!/bin/bash
#set -x

PYTHON_EXECUTABLE=$( if [ -f /usr/bin/python ]; then echo "/usr/bin/python" ; else echo "/usr/bin/python2.5"; fi ) 

source /data/adcpbm1/lib/python2.6/site-packages/pbm_collector/settings/PandaBrokerageMonitor.conf
source ${WORKDIR}/settings/pbm_profile
cd ${WORKDIR}

mkdir -p ${TMP_DIR}

TIMESTAMP=$(date '+%F %T' -u)


date >> ${WORKDIR}/logs/PBMonV2.log
${PYTHON_EXECUTABLE} ${WORKDIR}/parse_analy_brokerage_logV2.py >> ${WORKDIR}/logs/PBMonV2.log 2>&1
mypid="0"
### cleanup the PID file
PIDFILE=${TMP_DIR}/pbm_pidfile 
if [ -f "${PIDFILE}" ]; then 
	if [ -s "${PIDFILE}" ]; then
		mypid=$(cat ${PIDFILE} )
		if [ -z "$(ps ux | awk '{print $2;}' | grep ${mypid})" ]; then
			echo "Found not-empty file ${PIDFILE}, but the process is not running. Will delete ${PIDFILE}."
			rm ${PIDFILE}
		fi
	else
			echo "Found EMPTY file ${PIDFILE}, but the process is not running. Will NOTdelete ${PIDFILE}."
	fi
fi


### Deal with unresolved filesystems
if [ -f "${PIDFILE}" ]; then 
### mail to ADMIN
    ADMIN="adcpbm1@cern.ch"
    echo -e "$(basename $0) INFO [${TIMESTAMP} UTC] Please check logs and remove PIDfile (/tmp/adcpbm1/pbm_pidfile :ls $(ls -l ${PIDFILE})) :cat $(cat ${PIDFILE})" | mail -s "[PandaBrokerageMonitor] $(basename $0) - PID file stale lock" ${ADMIN} 
fi



