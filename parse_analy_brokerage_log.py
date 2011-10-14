# -*- coding: utf-8 -*-
from BSXPath import BSXPathEvaluator,XPathResult, XPathExpression
from BeautifulSoup import BeautifulSoup
from dailyDB import dailyDB

### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import os
import pycurl
import time
#from pd2p_monitoring import WORKDIR


OUTPUT_FILENAME_PREFIX = 'analyBrokerageLog'
db = dailyDB()

#MESSAGE_CATEGORIES=[' - SKIPPED ', ' - triggered ', ' - UNSELECTEDT2 ', ' - SELECTEDT2 ']
MESSAGE_CATEGORIES=[' action=skip ', ' action=choose ', ' use ']
SKIPPED_REASONS=['notmaxweight', 'missingapp','nopilot']
QUERY_HOUR = 1
QUERY_LIMIT = 1000

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def get_URL():
    return 'http://panda.cern.ch/server/pandamon/query?mode=mon&name=panda.mon.prod&type=analy_brokerage&hours=%d&limit=%d'%(QUERY_HOUR,QUERY_LIMIT)
    #return 'http://panda.cern.ch/server/pandamon/query?mode=mon&name=panda.mon.prod&type=pd2p&hours=2&limit=500'
    ##return 'http://panda.cern.ch/server/pandamon/query?mode=mon&hours=48&name=panda.mon.prod&type=pd2p&limit=20000'
    #return 'http://hpv2.farm.particle.cz/~schovan/pd2p/tadashi.html'
    #return 'http://hpv2.farm.particle.cz/~schovan/pd2p/tadashi-300.html'
    #return 'http://hpv2.farm.particle.cz/~schovan/pd2p/tadashi-300.2.html'
    #return 'file:///home/jschovan/ATLAS/adc-monitoring/pd2p/run/pd2pLog.2011-09-28.10.26.11.html'


def get_document():
    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL, get_URL())
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
    
    return t.contents

def is_this_category(string, category_pattern):
    if re.search(category_pattern, str(string)) is None:
        return False
    else:
        return True
    
def get_sitecloud_name(dic, siteID):
    cloud = siteID
    site_name = siteID
    for site_dic in dic:
        if site_dic['panda_siteID']==siteID:
            cloud = site_dic['cloud']
            site_name = site_dic['agis_ssb_site_name']
            break
    return (site_name,cloud)

def is_in_buf(records, logDate, category, site, dnUser):
    found = False
    idx = 0
    for record in records:
        if record[1]==logDate and record[2]==category and record[3]==site and record[5]==dnUser:
            found = True
            break
        idx += 1
    if not found:
        return None
    else:
        return idx

def parse_document(document):
    BSXdocument = BSXPathEvaluator(document)
    
    XPath_table = './/*[@id="main"]/p[2]/table'
    XPath_table_body = '%s/tbody' % (XPath_table)
    XPath_table_header = '%s/tr[1]' % (XPath_table_body)
    XPath_table_lines = '%s/tr' % (XPath_table_body)
    rows = BSXdocument.getItemList(XPath_table_lines)[1:]
    # get cloud name
    data = open('panda_queues.json').read()
    dic = eval(data)
    
    records = []
    exist_records = []
    in_buf_records = []
    maxId = db.get_max_id()
    last_time = db.get_last_updated_time()
    if last_time is None:
        db.first_last_updated_time()
        last_time = db.get_last_updated_time()
    this_time = None
    skip_time = None
    set_last = None
    if maxId is None:
        maxId = 0
    processed_rows = 0
    
    for row_counter in xrange(len(rows)):
        record = ()
        SHIFT=0
        
        row = rows[row_counter]
        XPath_table_row = '%s/tr[%d]' % (XPath_table_body, row_counter+1)
        """
        XPath_table_row_cell_category = '%s/td[%d]/text()' % (XPath_table_row, 1)
        cell_category = BSXdocument.getItemList(XPath_table_row_cell_category)
        if len(cell_category)>0:
            cell_category = cell_category[0]
        
        XPath_table_row_cell_type = '%s/td[%d]/text()' % (XPath_table_row, 2)
        cell_type = BSXdocument.getItemList(XPath_table_row_cell_type)
        if len(cell_type)>0:
            cell_type = cell_type[0]
        """
        XPath_table_row_cell_time = '%s/td[%d]/text()' % (XPath_table_row, 3)
        cell_time = BSXdocument.getItemList(XPath_table_row_cell_time)
        if len(cell_time)>0:
            cell_time = cell_time[0]
        """
        XPath_table_row_cell_level = '%s/td[%d]/text()' % (XPath_table_row, 4)
        cell_level = BSXdocument.getItemList(XPath_table_row_cell_level)
        if len(cell_level)>0:
            cell_level = cell_level[0]
        """
        XPath_table_row_cell_message = '%s/td[%d]/text()' % (XPath_table_row, 5)
        cell_message = BSXdocument.getItemList(XPath_table_row_cell_message)
        if len(cell_message)>0:
            cell_message = cell_message[0]
        
        
        message_category="no.category"
        message_date = ""
        message_time = ""
        message_dn = ""
        message_jobset ="no.jobset"
        message_jobdef = "no.jobdef"
        message_action = ""
        message_site="no.site"
        message_reason="no.reason"
        message_weight="no.weight"
        
        message_datetime = str(cell_time).split(' ')
        message_date = message_datetime[0].strip()
        message_time = message_datetime[1].strip()
        
        # Skip the leading uncompleted minute
        this_time = "2011-%s %s"%(message_date, message_time)
        
        if skip_time is None or skip_time == this_time:
            skip_time = this_time
            continue
        # set the last updated time when skip done.( Records in time DESC )
        if set_last is None:
            db.set_last_updated_time(this_time)
            set_last = True
        
        # Break when reach the last_time
        if (last_time is not None) and (this_time <= last_time):
            break
               
        # print 'Debug:',message_date,message_time,row_counter,cell_message
        processed_rows += 1
        
        tmp_message = str(cell_message.replace('&nbsp;', ' ')).split(' : ')
        message_dn = tmp_message[0].split('=')[1].replace("\\\'","").strip().replace(' ','_')
        tmp_job = tmp_message[1].split(' ')
        if len(tmp_job) > 1:
            message_jobset = tmp_job[0].split('=')[1].strip() 
            message_jobdef = tmp_job[1].split('=')[1].strip()
        else:
            if is_this_category(tmp_job[0],'jobset'):
                message_jobset = tmp_job[0].split('=')[1].strip()
            if is_this_category(tmp_job[0],'jobdef'):
                message_jobdef = tmp_job[0].split('=')[1].strip()
        ###print;print;print
        #print u'DEBUG: date time=', message_date, message_time
        #print u'DEBUG: dn=', message_dn
        #print u'DEBUG: jobset=', message_jobset
        #print u'DEBUG: jobdef=', message_jobdef
        #print u'DEBUG: ln113: tmp_message[1]=', tmp_message[1]
        #print u'DEBUG: ln113: tmp_message[2]=', tmp_message[2]
        
        ## skip
        if is_this_category(cell_message, ' action=skip '):
            continue # try to speed up
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
            message_reason = message_skip[2].split('=')[1].strip()
            if re.search('=',message_skip[4]):
                message_weight = message_skip[4].split('=')[1].strip()
            else:
                message_reason = '_'.join(message_skip[3:]).strip('_')
        
        ## choose
        elif is_this_category(cell_message, ' action=choose '):
            message_category = "C"
            message_choose = tmp_message[2].split(' ')
            message_action = message_choose[0].split('=')[1].strip()
            message_site = message_choose[1].split('=')[1].strip()
            message_reason = message_choose[2].split('=')[1].strip()
            if re.search('=',message_choose[5]):
                message_weight = message_choose[5].split('=')[1].strip()
            else:
                message_reason = '_'.join(message_choose[3:]).strip('_')
        
        ## use site or cloud
        elif is_this_category(cell_message, ' use '):
            message_use = tmp_message[2].split(' ')
            message_action = message_use[0].strip()
            message_site = message_use[1].strip()
            message_reason = '_'.join(message_use[3:]).strip('_')
            if is_this_category(message_reason, 'site'):
                message_category = "A"
            if is_this_category(message_reason, 'cloud'):
                message_category = "B"
        
        ## append to records it belong to
        if message_category in ['A','B','C']:
            logDate = str("2011-%s"%message_date)
            site_name,cloud = get_sitecloud_name(dic,message_site)
            dailyLogId = db.is_exist_item(logDate, message_category, site_name, message_dn)
            rec_idx = is_in_buf(records, logDate, message_category, site_name, message_dn)
            if dailyLogId is not None:
                exist_records.append([dailyLogId])
            elif rec_idx is not None:
                record = (logDate, message_category, site_name, message_dn)
                in_buf_records.append(record)
            else:
                maxId += 1
                count = 1               
                record = (maxId, logDate, message_category, site_name, \
                  cloud, message_dn, count)
                records.append(record)
    
    if (this_time is not None) and not (this_time <= last_time):
        print "Error: === NOT Reach the last updated time (%s -> %s) ==="%(this_time,last_time)
        
    return (processed_rows,records, exist_records, in_buf_records)


def print_records(records, FILENAME):
    of = open(FILENAME, 'w')
    for record in records: 
        message_date, message_time, message_category, \
                  message_dn, message_jobset, message_jobdef, \
                  message_action, message_site, message_reason, message_weight = record
        of.write('%s %s %s %s %s %s %s %s %s %s \n' % ( \
                  message_date, message_time, message_category, \
                  message_dn, message_jobset, message_jobdef, \
                  message_action, message_site, message_reason, message_weight) )
    of.close()


def write_document(document, FILENAME):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()

def run():
    t1 = time.time()
    document = get_document()
    t2 = time.time()
    processed_rows,rec,exist_rec,in_buf_rec = parse_document(document)
    t3 = time.time()
    db.add_logs(rec)
    db.increase_logs_count(exist_rec)
    db.increase_buf_count(in_buf_rec)
    t4 = time.time()
    
    time_get = t2-t1
    time_parse = t3-t2
    time_db = t4-t3
    
    logs_count = len(rec)+len(exist_rec)+len(in_buf_rec)
    last_time = db.get_last_updated_time()
    
    print u'DEBUG: %s Done(Limit-%d, Effective logs: %d/%d). Time: get-%d, parse-%d, db-%d'%(last_time,QUERY_LIMIT,logs_count,processed_rows,time_get,time_parse,time_db)
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


