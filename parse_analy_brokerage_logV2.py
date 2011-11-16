# -*- coding: utf-8 -*-
from BSXPath import BSXPathEvaluator,XPathResult, XPathExpression
from BeautifulSoup import BeautifulSoup
from dailyDBV2 import dailyDBV2

### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import os
import pycurl
import time
import datetime
import simplejson as json
from dateutil import parser
#from pd2p_monitoring import WORKDIR


OUTPUT_FILENAME_PREFIX = 'analyBrokerageLog'
db = dailyDBV2()

MESSAGE_CATEGORIES=[' action=skip ', ' action=choose ', ' action=exclude ', ' action=use ',' use ']
SKIPPED_REASONS=['notmaxweight', 'missingapp','nopilot']
QUERY_HOUR = 1
QUERY_LIMIT = 11000
DEBUG = 0

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

def is_in_buf(records, logDate, jobSet, category, site, dnUser):
    found = False
    idx = 0
    for record in records:
        if record[1]==logDate and record[2]==jobSet and record[3]==category and record[4]==site and record[6]==dnUser:
            found = True
            break
        idx += 1
    if not found:
        return None
    else:
        return idx
    
def is_excluded(ex_record,dn,jobset,site):
    found = False
    for r in ex_record:
        if r[0]==dn and r[1]==jobset and r[2]==site:
            found = True
            break
    return found
    
def get_log_year(p_year,p_date,p_time=''):
    DATEFORMAT = "%Y-%m-%d %H:%I:%S"
    r_year = p_year
    t1 = time.time()
    tf = time.strftime(DATEFORMAT,time.localtime(t1))
    dt1 = parser.parse("%s-%s %s"%(p_year,p_date,p_time))
    dt2 = parser.parse(tf)
    if dt1 > dt2:
        r_year -= 1
    return r_year
    

def parse_document(document):
    BSXdocument = BSXPathEvaluator(document)
    
    XPath_table = './/*[@id="main"]/p[2]/table'
    XPath_table_body = '%s/tbody' % (XPath_table)
    XPath_table_header = '%s/tr[1]' % (XPath_table_body)
    XPath_table_lines = '%s/tr' % (XPath_table_body)
    rows = BSXdocument.getItemList(XPath_table_lines)[1:]
    # get cloud name
    fjson = open('panda_queues.json','r')
    data = fjson.read()
    dic = json.loads(data)
    fjson.close()
    
    # Load unprocessed records
    fjson = open('unprocess.json','r')
    data = fjson.read()
    records = json.loads(data)
    fjson.close()
    
    # records = {}
    ex_records = {}
    maxId = db.get_max_id()
    last_time = db.get_last_updated_time()
    if last_time is None:
        db.first_last_updated_time()
        last_time = db.get_last_updated_time()
    this_time = None
    skip_time = None
    set_last = None
    this_year = datetime.date.today().year
    if maxId is None:
        maxId = 0
    processed_rows = 0
    
    error_skip =0
    ferror = open("last_errors.txt",'a')

    for row_counter in xrange(len(rows)):
        record = ()
        ex_rec = ()
        SHIFT=0
        
        row = rows[row_counter]

        rowDoc = BSXPathEvaluator('%s'%row)

        #XPath_table_row = '%s/tr[%d]' % (XPath_table_body, row_counter+1)
        XPath_table_row = '/'
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
        cell_time = rowDoc.getFirstItem(XPath_table_row_cell_time)
        #if len(cell_time)>0:
            #cell_time = cell_time[0]
        """
        XPath_table_row_cell_level = '%s/td[%d]/text()' % (XPath_table_row, 4)
        cell_level = BSXdocument.getItemList(XPath_table_row_cell_level)
        if len(cell_level)>0:
            cell_level = cell_level[0]
        """
        XPath_table_row_cell_message = '%s/td[%d]/text()' % (XPath_table_row, 5)
        cell_message = rowDoc.getFirstItem(XPath_table_row_cell_message)
        #if len(cell_message)>0:
            #cell_message = cell_message[0]
        
        
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
        log_year = get_log_year(this_year, message_date, message_time)
        this_time = "%s-%s %s"%(log_year, message_date, message_time)
        logDate = str("%s-%s"%(log_year, message_date))
        
        if skip_time is None or skip_time == this_time:
            skip_time = this_time
            continue
        # set the last updated time when skip done.( Records in time DESC )
        if set_last is None:
            # save it when every thing done
            set_last = this_time
        
        # Break when reach the last_time
        if (last_time is not None) and (this_time <= last_time):
            break
                       
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
        if message_jobset=='no.jobset' or message_jobdef=='no.jobdef':
            error_skip += 1
            ferror.write("Error: %s %s %s %s %s\n"%(message_date,message_time,message_dn,tmp_message[1],tmp_message[2]))
            continue

        processed_rows += 1
        
        ## skip
        if is_this_category(cell_message, ' action=skip '):
            # continue # try to speed up
            message_category = "D"
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
        
        # nJobs : add at 2011-11-10
        elif is_this_category(cell_message, 'nJobs'):
            message_category = "D"
            message_buf = tmp_message[2].split(' ')
            message_njobs = message_buf[0].split('=')[1].strip()
            message_country = message_buf[1].split('=')[1].strip()
            reckey = "%s|%s|%s"%(message_dn,message_jobset,message_jobdef)
            if records.has_key(reckey):
                records[reckey]['jobSet'] = message_jobset
                records[reckey]['nJobs'] = message_njobs
                records[reckey]['country'] = message_country
            else:
                records[reckey] = {'jobSet':message_jobset,'nJobs':message_njobs,'country':message_country}
            
        # exclude : add at 2011-10-26
        elif is_this_category(cell_message, ' action=exclude '):
            message_category = "E"
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
            reckey = "%s|%s|%s"%(message_dn,message_jobset,message_site)
            if ex_records.has_key(reckey):
                ex_records[reckey]['logDate'] = logDate
                ex_records[reckey]['jobSet'] = message_jobset
                ex_records[reckey]['category'] = message_category
                ex_records[reckey]['site'] = message_site
            else:
                ex_records[reckey] = {'logDate':logDate,'jobSet':message_jobset,'category':message_category,'site':message_site}
        
        ## choose
        elif is_this_category(cell_message, ' action=choose '):
            message_category = "C"
            message_choose = tmp_message[2].split(' ')
            message_action = message_choose[0].split('=')[1].strip()
            message_site = message_choose[1].split('=')[1].strip()
            reckey = "%s|%s|%s"%(message_dn,message_jobset,message_jobdef)
         
        ## action=use: add at 2011-10-26
        elif is_this_category(cell_message, ' action=use '):
            #message_category = "C"
            message_choose = tmp_message[2].split(' ')
            message_action = message_choose[0].split('=')[1].strip()
            message_site = message_choose[1].split('=')[1].strip()
            message_reason = '_'.join(message_choose[3:]).strip('_')
            if is_this_category(message_reason, 'site'):
                message_category = "A"
            if is_this_category(message_reason, 'cloud'):
                message_category = "B"
        
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
                
        ## other actions
        elif is_this_category(cell_message, ' action='):
            message_category = "D"
            message_buf = tmp_message[2].split(' ')
            message_action = message_buf[0].split('=')[1].strip()
            print "WARNING: action=%s is not processed!"%message_action

        if message_category in ['A','B','C']:
            reckey = "%s|%s|%s"%(message_dn,message_jobset,message_jobdef)
            if records.has_key(reckey):
                records[reckey]['logDate'] = logDate
                records[reckey]['jobSet'] = message_jobset
                records[reckey]['category'] = message_category
                records[reckey]['site'] = message_site
            else:
                records[reckey] = {'logDate':logDate,'jobSet':message_jobset,'category':message_category,'site':message_site}
            
            if not records[reckey].has_key('nJobs'):
                records[reckey]['nJobs'] = "1"
                records[reckey]['country'] = '--'
    
    ferror.close()

    eff_records = []
    exist_records = []
    in_buf_records = []
    sum_nJobs = 0
    lost_nJobs = 0
    
    fjson = open("unprocess.json",'w')
    fjson.write("{\n")
    jcom = ""
    
    for rec in records:
        if not records[rec].has_key('category'):
            if records[rec].has_key('nJobs'):
                lost_nJobs += int(records[rec]['nJobs'])
            json_string = "%s\"%s\":%s\n"%(jcom,rec,json.dumps(records[rec]))
            fjson.write(json_string)
            jcom = ","
            continue
        rec_idx = None
        dnUser = rec.split('|')[0]
        logDate = records[rec]['logDate']
        jobSet = records[rec]['jobSet']
        category = records[rec]['category']
        country = records[rec]['country']
        nJobs = records[rec]['nJobs']
        site_name,cloud = get_sitecloud_name(dic,records[rec]['site'])
        dailyLogId = db.is_exist_item(logDate, jobSet, category, site_name, dnUser)
        
        if country == '--':
            lost_nJobs += int(nJobs)
            json_string = "%s\"%s\":%s\n"%(jcom,rec,json.dumps(records[rec]))
            fjson.write(json_string)
            jcom = ","
            continue
                     
        sum_nJobs += int(nJobs)
        if dailyLogId is None:
            rec_idx = is_in_buf(eff_records, logDate, jobSet, category, site_name, dnUser)
        if dailyLogId is not None:
            record = (int(nJobs),dailyLogId)
            exist_records.append(record)
        elif rec_idx is not None:
            record = ( int(nJobs), logDate, jobSet, category, site_name, dnUser)
            in_buf_records.append(record)
        else:
            maxId += 1
            record = (maxId, logDate, jobSet, category, site_name, cloud, dnUser, '1', nJobs, country)
            eff_records.append(record)
            
    fjson.write("}\n")
    fjson.close()
    
    ## for Excluded        
    for rec in ex_records:
        if not ex_records[rec].has_key('category'):
            continue
        rec_idx = None
        dnUser = rec.split('|')[0]
        logDate = ex_records[rec]['logDate']
        jobSet = ex_records[rec]['jobSet']
        category = ex_records[rec]['category']
        country = "--"
        nJobs = "1"
        site_name,cloud = get_sitecloud_name(dic,ex_records[rec]['site'])
        dailyLogId = db.is_exist_item(logDate, jobSet, category, site_name, dnUser)
        if dailyLogId is None:
            rec_idx = is_in_buf(eff_records, logDate, jobSet, category, site_name, dnUser)
        if dailyLogId is not None:
            record = (int(nJobs),dailyLogId)
            exist_records.append(record)
        elif rec_idx is not None:
            record = (int(nJobs), logDate, jobSet, category, site_name, dnUser )
            in_buf_records.append(record)
        else:
            maxId += 1
            record = (maxId, logDate, jobSet, category, site_name, cloud, dnUser, '1', nJobs, country)
            eff_records.append(record)

    if (this_time is not None) and not (this_time <= last_time):
        print "Error: === NOT Reach the last updated time (%s -> %s) ==="%(this_time,last_time)
    if error_skip > 0:
        print "WARNING: Missing jobSet/jobDef skiped = %d"%error_skip

    return (set_last,processed_rows,sum_nJobs,lost_nJobs,eff_records, exist_records, in_buf_records)

def run():
    #t1 = time.time()
    document = get_document()
    t2 = time.time()
    set_last,processed_rows,sum_nJobs,lost_nJobs,eff_records,exist_records,in_buf_records = parse_document(document)
    t3 = time.time()

    db.add_logs(eff_records)
    db.increase_logs_count(exist_records)
    db.increase_buf_count(in_buf_records)

    #t4 = time.time()
    db.set_last_updated_time(set_last) # set when all done.
    
    #time_get = t2-t1
    time_parse = t3-t2
    #time_db = t4-t3
    
    logs_count = len(eff_records)+len(exist_records)+len(in_buf_records)
    #last_time = db.get_last_updated_time()
    
    print u'INFOR: %s Limit: %d Effective: %d/%d nJobs: %d ParsingTime: %d nJobsUnprocess: %d'%(set_last,QUERY_LIMIT,logs_count,processed_rows,sum_nJobs,time_parse,lost_nJobs)
    
if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    

