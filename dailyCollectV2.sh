#!/bin/bash
source /home/ookey/.bash_profile

cd /home/ookey/workspace/PandaBrokerageMonitor
/usr/bin/python parse_analy_brokerage_logV2.py >> logs/PBMonV2.log 2>&1
/usr/bin/python my_logfileV2.py > /dev/null 2>&1
