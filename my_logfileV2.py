# -*- coding: utf-8 -*-

### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import os
import pycurl
import time
import datetime

def get_document(logfile):
    log = open(logfile,'r')
    data = log.read().split('\n')
    return data

def is_this_category(string, category_pattern):
    if re.search(category_pattern, str(string)) is None:
        return False
    else:
        return True
    
def parse_document(document):
    records = []    
    from_date = None
    to_date = None
    
    for row in document:
        buf = row.split(' ')
        #print buf
        if not is_this_category(buf[0], 'INFOR') or is_this_category(buf[1],'Pack'):
            continue
        else:
            if buf[1] == 'None': # Not get datetime info
                continue
            buf_datetime = buf[1]+" "+buf[2]
            if from_date is None:
                from_date = buf_datetime
            if to_date == buf_datetime:
                continue
            to_date = buf_datetime
            processed,all = buf[6].split('/')
            nJobs = buf[8]
            parsingTime = buf[10]
            
            records.append((buf_datetime,processed,all,parsingTime,nJobs))
                       
    return (from_date, to_date, records)

def write_document(from_date, to_date, records, doc_file="my_logfileV2.html", last_hours=4):
    from_date = None
    to_date = None
    data = open('template/CHART_mylogV2.html').read()

    comm = ""
    comm1 = ""
    series_data1 = ""
    series_data2 = ""
    series_data3 = ""
    series_data4 = ""
    series_data5 = ""
    skip = len(records)-12*last_hours
    r = 0
    for c in records:
        sDate, sTime = c[0].split(' ')
        sy,sm,sd = sDate.split('-')
        sh,si = sTime.split(':')
        sy = int(sy)
        sm = int(sm)-1 # DATE.UTC: month: 0-11
        sd = int(sd)
        sh = int(sh)
        si = int(si)
        series_data4 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data4,comm1,sy,sm,sd,sh,si,c[2])
        series_data5 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data5,comm1,sy,sm,sd,sh,si,c[4])
        comm1 = ","
        r += 1
        if r<skip:
            continue
        if from_date is None:
            from_date = c[0]
        to_date = c[0]
        series_data1 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data1,comm,sy,sm,sd,sh,si,c[1])
        series_data2 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data2,comm,sy,sm,sd,sh,si,c[2])
        series_data3 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data3,comm,sy,sm,sd,sh,si,c[3])
        comm = ","
        
    data = data.replace('#FROM_DATE#',from_date)
    data = data.replace('#TO_DATE#',to_date)
    
    data = data.replace('#SERIES_DATA1#',series_data1)
    data = data.replace('#SERIES_DATA2#',series_data2)
    data = data.replace('#SERIES_DATA3#',series_data3)
    data = data.replace('#SERIES_DATA4#',series_data4)
    data = data.replace('#SERIES_DATA5#',series_data5)
        
    of = open(doc_file, 'w')
    print >>of, data
    of.close()
    return data

def run(logfile):
    document = get_document(logfile)
    t2 = time.time()
    from_date,to_date,records = parse_document(document)
    t3 = time.time()
    time_parse = t3-t2
    
    write_document(from_date,to_date,records)

if __name__ == "__main__":
    
    """
    if len(sys.argv) < 2:
        print "ERROR: too few input parameters"
        print "USAGE: python   parse_logfile.py   <input logfile>"
        sys.exit(1) # before Python 2.5, after: exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]
    """

    run('logs/PBMonV2.log')
    


