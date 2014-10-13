# -*- coding: utf-8 -*-
from dailyDB import dailyDB
from monthlyDB import monthlyDB

import re
import sys
import os
import time
import datetime
import simplejson as json

dailydb = dailyDB()
monthlydb = monthlyDB()

DEBUG = 0

def get_document():
    lastID = monthlydb.get_last_updated_id()
    sql = 'select dailyLogId,logDate,category,site,cloud,dnUser,jobdefCount from dailyLog where dailyLogId>%d order by dailyLogId'%lastID
    rs = dailydb.query(sql)
    return rs

def parse_document(rs):
    
    maxId = monthlydb.get_max_id()
    if maxId is None:
        maxId = 0
    processed_rows = 0
    new_rows = 0
    old_rows = 0
    
    for row in rs:
        record = ()
        dailyLogId = row[0]
        logMonth = row[1][0:7]
        category = row[2]
        site = row[3]
        cloud = row[4]
        dnUser = row[5]
        count = row[6]
        processed_rows += 1
        
        monthlyLogId = monthlydb.is_exist_item(logMonth, category, site, dnUser)
        if monthlyLogId is not None:
            old_rows += 1
            monthlydb.increase_log_count(monthlyLogId, count)
        else:
            new_rows += 1
            maxId += 1
            monthlydb.add_log(maxId, logMonth, category, site, cloud, dnUser, count)
        
        if DEBUG==1:
            print "========="
            print "DEBUG:", maxId, logMonth, category, site, cloud, dnUser, count
            print "========="
    
    monthlydb.set_last_updated_id(dailyLogId)    

    return processed_rows, new_rows, old_rows

def run():
    #t1 = time.time()
    rs = get_document()
    t2 = time.time()
    if rs is not None:
        processed_rows,new_rows,old_rows = parse_document(rs)
    t3 = time.time()
    time_parse = t3-t2
    #time_db = t4-t3
    
    
    print u'INFOR: Pack Done(%d New:%d Old:%d). ParsingTime: %d'%(processed_rows,new_rows,old_rows,time_parse)
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


