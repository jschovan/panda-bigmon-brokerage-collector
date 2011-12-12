#!/bin/bash
#source /home/ookey/workspace/PandaBrokerageMonitor/pbm_profile
#cd /home/ookey/workspace/PandaBrokerageMonitor

set -x

PYTHON_EXECUTABLE="/usr/bin/python2.5"

source /data/adcpbm1/PandaBrokerageMonitor/PandaBrokerageMonitor.conf
source ${WORKDIR}/pbm_profile
cd ${WORKDIR}

mkdir -p ${TMP_DIR}

date >> ${WORKDIR}/logs/PBMonV2.log
${PYTHON_EXECUTABLE} ${WORKDIR}/parse_analy_brokerage_logV2.py >> ${WORKDIR}/logs/PBMonV2.log 2>&1
${PYTHON_EXECUTABLE} ${WORKDIR}/my_logfileV2.py > /dev/null 2>&1

