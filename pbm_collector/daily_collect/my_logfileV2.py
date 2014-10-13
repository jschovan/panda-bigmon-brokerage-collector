# -*- coding: utf-8 -*-

### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import os
import pycurl
import time
import datetime
import calendar
import simplejson as json
import smtplib
import email

last_hours = 4
NOTIFY_MIN = 10 # mins
NOTIFY_MAX = 30 # mins
mFrom = 'PBMon <no-reply@cern.ch>'
mTo = 'ookey.lai@twgrid.org,ookeykimo@yahoo.com.tw,adcpbm1@cern.ch'

WORKDIR="/data/adcpbm1/PandaBrokerageMonitor"
PUBDIR="/data/adcmon-preproduction/PandaBrokerageMon/pubdir"

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
            try:
                limit,hour = buf[4].split('/')
            except:
                limit = 11000
                hour = 1
            processed,all = buf[6].split('/')
            nJobs = buf[8]
            parsingTime = buf[10]
            unprocessed = buf[12]
            
            records.append((buf_datetime,processed,all,parsingTime,nJobs,unprocessed,limit))
    
    if to_date is not None:
        tnow = time.time()
        tm_todate = time.strptime(to_date,"%Y-%m-%d %H:%M")
        todate = calendar.timegm(tm_todate)
        tdiff = int((tnow-todate)/60) #in mins
        my_notify(tdiff,to_date)
        update_queryOptions(tdiff)
                       
    return (from_date, to_date, records)

def my_notify(tdiff,todate):
    global NOTIFY_MIN, NOTIFY_MAX, mFrom, mTo
    msg = email.message_from_string("Data missing for %d mins from %s"%(tdiff,todate))
    msg['Subject'] = "Notification from PandaBrokerageMonitor"
    msg['From'] = mFrom
    msg['To'] = mTo
    if tdiff > NOTIFY_MIN and tdiff < NOTIFY_MAX:
        s = smtplib.SMTP('localhost')
        s.sendmail(mFrom, [mTo], msg.as_string())
        s.quit()
    return True

def update_queryOptions(tdiff):
    options = {'QUERY_HOUR': 1, 'QUERY_LIMIT': 12000}
    hour = int(tdiff/60)
    q = tdiff%60
    if q>0:
        hour += 1
    cycle = int(tdiff/5)
    limit = 12000 + 1000*cycle
    options['QUERY_HOUR'] = hour
    options['QUERY_LIMIT'] = limit
    write_jsonfile(options)
    return True

def write_jsonfile(options):
    global WORKDIR
    of = open("%s/queryOptions.json" % WORKDIR,'w')
    json_string = json.dumps(options)
    of.write(json_string)
    of.close()

def write_document(from_date, to_date, records, doc_file="my_logfile.html"):
    global last_hours, WORKDIR, PUBDIR
    doc_file='%s/%s' % (PUBDIR, doc_file)
    from_date = None
    to_date = None
    data = open('%s/template/CHART_mylogV2.html' % WORKDIR).read()
    DATEFORMAT = "%Y-%m-%d %H:%M"
    t1 = time.time()
    t2 = t1 - last_hours*60*60
    tnow = time.strftime(DATEFORMAT,time.gmtime(t2))

    comm = ""
    comm1 = ""
    series_data1 = ""
    series_data2 = ""
    series_data3 = ""
    series_data4 = ""
    series_data5 = ""
    series_data6 = ""
    series_data7 = ""
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
        series_data6 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data6,comm1,sy,sm,sd,sh,si,c[5])
        comm1 = ","
        if c[0]<tnow:
            continue
        if from_date is None:
            from_date = c[0]
        to_date = c[0]
        series_data1 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data1,comm,sy,sm,sd,sh,si,c[1])
        series_data2 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data2,comm,sy,sm,sd,sh,si,c[2])
        series_data3 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data3,comm,sy,sm,sd,sh,si,c[3])
        series_data7 = "%s %s [Date.UTC(%d,%d,%d,%d,%d), %s]"%(series_data7,comm,sy,sm,sd,sh,si,int(c[6])/10)
        comm = ","
        
    data = data.replace('#FROM_DATE#',from_date)
    data = data.replace('#TO_DATE#',to_date)
    
    data = data.replace('#SERIES_DATA1#',series_data1)
    data = data.replace('#SERIES_DATA2#',series_data2)
    data = data.replace('#SERIES_DATA3#',series_data3)
    data = data.replace('#SERIES_DATA4#',series_data4)
    data = data.replace('#SERIES_DATA5#',series_data5)
    data = data.replace('#SERIES_DATA6#',series_data6)
    data = data.replace('#SERIES_DATA7#',series_data7)
        
    of = open(doc_file, 'w')
    print >>of, data
    of.close()
    return True

def run(logfile):
    document = get_document(logfile)
    t2 = time.time()
    from_date,to_date,records = parse_document(document)
    t3 = time.time()
    time_parse = t3-t2
    
    write_document(from_date,to_date,records)

if __name__ == "__main__":
    run('%s/logs/PBMonV2.log' % WORKDIR)


