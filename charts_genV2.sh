#!/bin/bash

#set -x

PYTHON_EXECUTABLE="/usr/bin/python2.5"

source /data/adcpbm1/PandaBrokerageMonitor/PandaBrokerageMonitor.conf
source ${WORKDIR}/pbm_profile

cd ${WORKDIR}

#${PYTHON_EXECUTABLE} ${WORKDIR}/charts_allV2.py > /dev/null 2>&1
${PYTHON_EXECUTABLE} ${WORKDIR}/charts_allV2.py >>${WORKDIR}/logs/charts_allV2.log 2>&1


