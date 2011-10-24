#!/bin/bash

cd /home/ookey/workspace/PandaBrokerageMonitor
/bin/rm -f panda_queues.json
/usr/bin/wget -q http://adc-ssb.cern.ch/SITE_EXCLUSION/panda_queues.json
