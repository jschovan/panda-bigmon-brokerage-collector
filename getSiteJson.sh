#!/bin/bash
echo "$(basename $0) $(date) start"
source /data/adcpbm1/PandaBrokerageMonitor/PandaBrokerageMonitor.conf
#cd /home/ookey/workspace/PandaBrokerageMonitor
cd ${WORKDIR}
/bin/rm -f ${WORKDIR}/panda_queues.json*
/usr/bin/wget -q http://adc-ssb.cern.ch/SITE_EXCLUSION/panda_queues.json -O ${WORKDIR}/panda_queues.json
echo "$(basename $0) $(date) finish"

