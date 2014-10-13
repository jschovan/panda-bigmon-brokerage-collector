#!/bin/bash
echo "$(basename $0) $(date) start"
source /data/adcpbm1/lib/python2.6/site-packages/pbm_collector/settings/PandaBrokerageMonitor.conf
cd ${WORKDIR}
/bin/rm -f ${WORKDIR}/settings/panda_queues.json*
/usr/bin/wget -q "http://atlas-agis-api.cern.ch/request/pandaqueue/query/list/?json&preset=ssb" -O ${WORKDIR}/settings/panda_queues.json
echo "$(basename $0) $(date) finish"

