#!/bin/bash
### Script to prepare environment for adcpbm1 to run PanDA Brokerage Collector.
###    Run as adcpbm1 when migrating to a new machine.
### Author: Jaroslava Schovancova <jaroslava.schovancova@cern.ch>

### Following 3 commands should be done by root
# sudo mkdir -p /data/adcmusr1
# sudo chown adcmusr1:zp /data/adcmusr1
# sudo chmod og-rwx /data/adcmusr1

TMPDIR=/tmp/${USER}
mkdir -p ${TMPDIR}


WORKDIR=/data/${USER}/lib/python2.6/site-packages/pbm_collector
mkdir -p ${WORKDIR}
# git clone https://github.com/jschovan/panda-bigmon-brokerage-collector.git ${WORKDIR}
# yum install bigpanda-brokerage-collector



mkdir -p ${WORKDIR}/logs 



cd ${WORKDIR}/settings/
echo -n "{}" > allunprocess.json
cp allunprocess.json allunprocess.json.bak
cp allunprocess.json allunprocess.json.new
touch zero_process.html panda_queues.json last_errors.txt

### edit config files
# vim PandaBrokerageMonitor.conf
# vim PandaBrokerageMonitorDB.conf



### get getSiteJson.shcontent of panda_queues.json
${WORKDIR}/get_site/getSiteJson.sh



### set up crontab, see content of crontab_adcpbm1



