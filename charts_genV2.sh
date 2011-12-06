#!/bin/bash
source /data/adcpbm1/PandaBrokerageMonitor/PandaBrokerageMonitor.conf

source ${WORKDIR}/pbm_profile

cd ${WORKDIR}

/usr/bin/python ${WORKDIR}/charts_allV2.py > /dev/null 2>&1


