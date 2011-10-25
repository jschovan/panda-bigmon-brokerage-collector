#!/bin/bash
source /home/ookey/.bash_profile

cd /home/ookey/workspace/PandaBrokerageMonitor
/usr/bin/python pack_analy_brokerage_log.py >> logs/PBMon.log 2>&1
