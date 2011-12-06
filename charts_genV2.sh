#!/bin/bash
source /home/ookey/workspace/PandaBrokerageMonitor/pbm_profile

cd /home/ookey/workspace/PandaBrokerageMonitor
/usr/bin/python charts_allV2.py > /dev/null 2>&1
