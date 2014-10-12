#!/bin/bash
### Script to prepare environment for adcpbm1 to run PanDA Brokerage Collector.
###    Run as adcpbm1 when migrating to a new machine.
### Author: Jaroslava Schovancova <jaroslava.schovancova@cern.ch>

### Following 3 commands should be done by root
# sudo mkdir -p /data/adcmusr1
# sudo chown adcmusr1:zp /data/adcmusr1
# sudo chmod og-rwx /data/adcmusr1


mkdir -p /tmp/${USER}
WORKDIR=/data/${USER}/PandaBrokerageMonitor
mkdir -p ${WORKDIR}
svn co svn+ssh://svn.cern.ch/reps/adcsw/adcmon/PandaBrokerageMonitor/trunk ${WORKDIR}

cd ${WORKDIR}

mkdir -p logs 

echo -n "{}" > allunprocess.json
cp allunprocess.json allunprocess.json.bak
cp allunprocess.json allunprocess.json.new
touch zero_process.html panda_queues.json last_errors.txt

### get getSiteJson.shcontent of panda_queues.json
./getSiteJson.sh

### edit config files
# vim PandaBrokerageMonitor.conf
# vim PandaBrokerageMonitorDB.conf

### set up crontab, see content of crontab_adcpbm1


