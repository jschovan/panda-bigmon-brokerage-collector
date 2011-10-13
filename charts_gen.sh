#!/bin/bash
source /home/ookey/.bash_profile

cd /home/ookey/workspace/PandaBrokerageMonitor
/usr/bin/python charts_week.py > /dev/null 2>&1
/usr/bin/python charts_month.py > /dev/null 2>&1
