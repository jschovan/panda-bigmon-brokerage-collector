#!/bin/bash
source /home/ookey/.bash_profile

cd /home/ookey/workspace/PandaBrokerageMonitor
/usr/bin/python charts_weekV2.py > /dev/null 2>&1
/usr/bin/python charts_monthV2.py > /dev/null 2>&1
/usr/bin/python charts_seasonV2.py > /dev/null 2>&1
/usr/bin/python charts_yearV2.py > /dev/null 2>&1
