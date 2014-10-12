# -*- coding: utf-8 -*-
from BSXPath import BSXPathEvaluator,XPathResult, XPathExpression
from BeautifulSoup import BeautifulSoup
from dailyDBV2 import dailyDBV2

### get it from: http://www.crummy.com/software/BeautifulSoup/
try:
    import json
except:
    import simplejson as json
import re
import sys
import os
import pycurl
import time
from datetime import datetime, date, timedelta
#import simplejson as json
from logger import logger
#from dateutil import parser
#from pd2p_monitoring import WORKDIR

USERNAME="adcpbm1"

OUTPUT_FILENAME_PREFIX = 'analyBrokerageLog'
db = dailyDBV2()

MESSAGE_CATEGORIES=[' action=skip ', ' action=choose ', ' action=exclude ', ' action=use ',' use ']
SKIPPED_REASONS=['notmaxweight', 'missingapp','nopilot']
QUERY_HOUR = 0
QUERY_LIMIT = 0
DEBUG = 0

WORKDIR="/data/adcpbm1/PandaBrokerageMonitor"
PUBDIR="/data/adcmon-preproduction/PandaBrokerageMon/pubdir"
LOGDIR="%s/logs" % (WORKDIR)
logname="dailyCollectV2"
logfile="%s/logging.%s" % (LOGDIR, logname)
LOGGER=logger(logname, logfile)


# get cloud name
fjson = open('%s/panda_queues.json' % WORKDIR,'r')
data = fjson.read()
dic = json.loads(data)
fjson.close()

# get query options
try:
    qjson = open('%s/queryOptions.json' % WORKDIR,'r')
    data = qjson.read()
    qoptions = json.loads(data)
    qjson.close()
    QUERY_HOUR = qoptions['QUERY_HOUR']
    QUERY_LIMIT = qoptions['QUERY_LIMIT']
except:
    QUERY_HOUR = 1
    QUERY_LIMIT = 11111

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def get_URL():
    global QUERY_HOUR
    return 'http://bigpanda.cern.ch/pbm/api/?type=analy_brokerage&starttime=%s&endtime=%s' % \
        ((datetime.utcnow() - timedelta(hours=QUERY_HOUR)).isoformat(), \
          datetime.utcnow().isoformat())


def get_document():
    LOGGER.info(u'Starting get_document()')
    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL, get_URL())
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
    LOGGER.info(u'Finished get_document()')
    
    return t.contents

def is_this_category(string, category_pattern):
    if re.search(category_pattern, str(string)) is None:
        return False
    else:
        return True
    
def get_dic_dic_siteid():
    global dic
    dic_dic={}
    for queueinfo in dic:
        sitename=queueinfo['agis_ssb_site_name']
        pandasiteid=queueinfo['panda_siteID']
        cloud=queueinfo['cloud']
        dic_dic[pandasiteid]={'sitename':sitename, 'cloud':cloud, 'pandasiteid': pandasiteid}
    return dic_dic
dic_dic_siteid = get_dic_dic_siteid()

def get_dic_dic_ATLASsitename():
    global dic
    dic_dic={}
    for queueinfo in dic:
        sitename=queueinfo['agis_ssb_site_name']
        pandasiteid=queueinfo['panda_siteID']
        cloud=queueinfo['cloud']
        dic_dic[sitename]={'sitename':sitename, 'cloud':cloud, 'pandasiteid': pandasiteid}
    return dic_dic
dic_dic_ATLASsitename = get_dic_dic_ATLASsitename()

def merge_dic_dics():
    global dic_dic_siteid, dic_dic_ATLASsitename
    dic_dic_merged=dic_dic_siteid
    dic_dic_merged.update(dic_dic_ATLASsitename)
    return dic_dic_merged
dic_dic_merged=merge_dic_dics()

def get_sitecloud_name(siteID):
    global dic_dic_merged
    cloud = siteID
    site_name = siteID
    
    try: 
        cloud=dic_dic_merged[siteID]['cloud']
    except KeyError:
        cloud=siteID
    try: 
        site_name=dic_dic_merged[siteID]['sitename']
    except KeyError:
        site_name=siteID
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
    
def write_document(document, FILENAME):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()
    LOGGER.info("Wrote file %s" % FILENAME)

def get_log_year(p_year,p_date,p_time=''):
    DATEFORMAT = "%Y-%m-%d %H:%M:%S"
    r_year = p_year
    t1 = time.time()
    tf = time.strftime(DATEFORMAT,time.gmtime(t1))
    dt1_string="%s-%s %s"%(p_year,p_date,p_time)
    if len(p_time)==5:
        dt1_string="%s:00" % (dt1_string)
    #dt1 = parser.parse("%s-%s %s"%(p_year,p_date,p_time))
    #dt2 = parser.parse(tf)
    dt1=datetime.strptime(dt1_string, DATEFORMAT)
    dt2=datetime.strptime(tf, DATEFORMAT)
    if dt1 > dt2:
        r_year -= 1
    return r_year


def parse_document(document_filename):
    global db, WORKDIR, LOGGER
    LOGGER.info('Using document file %s' % (document_filename))
    f = open(document_filename)
    document = json.loads(f.read())
    f.close()
    LOGGER.info('Retrieved content of file %s' % (document_filename))
    LOGGER.debug('len(document)=%d. type(document)=%s.' % (len(document), type(document)))

    ### get the data -> rows
    rows = []
    try:
        rows = document['data']
    except:
        rows = []
    LOGGER.info('Retrieved %d rows to process.' % (len(rows)))

    # Load unprocessed records
    input_file='%s/allunprocess.json' % WORKDIR
    fjson = open(input_file,'r')
    data = fjson.read()
    records = json.loads(data)
    fjson.close()
    
    LOGGER.info('Retrieved content of file %s' % (input_file))
    
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
    this_year = date.today().year
    if maxId is None:
        maxId = 0
    processed_rows = 0
    
    LOGGER.info('maxId=%s' % (maxId))
    LOGGER.info('info=%s' % (last_time))
    
    error_skip =0
    ferror = open("%s/last_errors.txt" % WORKDIR,'a')
    
    LOGGER.info('Starting loop over input rows.')
    
    row_counter = 0
#    for row_counter in xrange(len(rows)):
    for row in rows:
        LOGGER.debug('Processing line %d/%d' % (row_counter+1, len(rows)))
        record = ()
        ex_rec = ()
        SHIFT=0
        
        cell_time = row['time']
        cell_message = row['message']
        
        LOGGER.debug('retrieved message for line %d' % (row_counter+1))
        
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
        
        LOGGER.debug('Will apply category rules to message for line %d' % (row_counter+1))
        
        # Skip the leading uncompleted minute
        this_time = "%s %s" % (message_date, message_time)
        logDate = str("%s" % (message_date))
        
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
            if not is_this_category(cell_message, ' action=skip '):
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
                records[reckey]['jobSet'] = "%s|%s"%(message_dn,message_jobset)
                records[reckey]['nJobs'] = message_njobs
                records[reckey]['country'] = message_country
            else:
                records[reckey] = {'jobSet':"%s|%s"%(message_dn,message_jobset),'nJobs':message_njobs,'country':message_country}
        # exclude : add at 2011-10-26
        elif is_this_category(cell_message, ' action=exclude '):
            message_category = "E"
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
            reckey = "%s|%s|%s"%(message_dn,message_jobset,message_site)
            if ex_records.has_key(reckey):
                ex_records[reckey]['logDate'] = logDate
                ex_records[reckey]['jobSet'] = "%s|%s"%(message_dn,message_jobset)
                ex_records[reckey]['category'] = message_category
                ex_records[reckey]['site'] = message_site
            else:
                ex_records[reckey] = {'logDate':logDate,'jobSet':"%s|%s"%(message_dn,message_jobset),'category':message_category,'site':message_site}
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
            LOGGER.warning("action=%s is not processed!"%message_action)
        
        LOGGER.debug('Category rules applied to message for line %d' % (row_counter+1))
        
        if message_category in ['A','B','C']:
            reckey = "%s|%s|%s"%(message_dn,message_jobset,message_jobdef)
            if records.has_key(reckey):
                records[reckey]['logDate'] = logDate
                records[reckey]['jobSet'] = "%s|%s"%(message_dn,message_jobset)
                records[reckey]['category'] = message_category
                records[reckey]['site'] = message_site
            else:
                records[reckey] = {'logDate':logDate,'jobSet':"%s|%s"%(message_dn,message_jobset),'category':message_category,'site':message_site}
            
            if not records[reckey].has_key('nJobs'):
                records[reckey]['nJobs'] = "1"
                records[reckey]['country'] = '--'
        LOGGER.debug('Finished processing of line %d' % (row_counter+1))
        row_counter += 1
    LOGGER.info('Finished processing of all %d lines' % (len(rows)))
    
    ferror.close()

    eff_records = []
    exist_records = []
    in_buf_records = []
    sum_nJobs = 0
    lost_nJobs = 0
    
    fjson = open("%s/allunprocess.json.new" % WORKDIR,'w')
    fjson.write("{\n")
    jcom = ""
    
    LOGGER.info('Processing %d records' % (len(records)))
    
    for rec in records:
        LOGGER.debug('Processing record: %s' % (rec))
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
        site_name,cloud = get_sitecloud_name(records[rec]['site'])
        dailyLogId = db.is_exist_item(logDate, jobSet, category, site_name, dnUser)
        
        LOGGER.debug('Insert record to DB: %s' % (rec))
        
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
            
        LOGGER.debug('Finished processing of record: %s' % (rec))
    fjson.write("}\n")
    fjson.close()
    os.unlink("%s/allunprocess.json.bak" % WORKDIR)
    os.rename("%s/allunprocess.json" % WORKDIR, "%s/allunprocess.json.bak" % WORKDIR)
    os.rename("%s/allunprocess.json.new" % WORKDIR, "%s/allunprocess.json" % WORKDIR)
    

    LOGGER.info('Processing %s records "For Excluded"' % (len(ex_records)))
    ## for Excluded        
    for rec in ex_records:
        LOGGER.debug('Processing excluded record: %s' % (rec))
        if not ex_records[rec].has_key('category'):
            continue
        rec_idx = None
        dnUser = rec.split('|')[0]
        logDate = ex_records[rec]['logDate']
        jobSet = ex_records[rec]['jobSet']
        category = ex_records[rec]['category']
        country = "--"
        nJobs = "1"
        site_name,cloud = get_sitecloud_name(ex_records[rec]['site'])
        dailyLogId = db.is_exist_item(logDate, jobSet, category, site_name, dnUser)
        LOGGER.debug('Insert record to DB: %s' % (rec))
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
        LOGGER.debug('Finished processing of record: %s' % (rec))
    LOGGER.info('Finished processing %s records "For Excluded"' % (len(ex_records)))
    
    if (this_time is not None) and not (this_time <= last_time):
        print u"Error: === NOT Reach the last updated time (%s -> %s) ==="%(this_time,last_time)
        LOGGER.error("DID NOT Reach the last updated time (%s -> %s) ==="%(this_time,last_time))
    if error_skip > 0:
        print u"WARNING: Missing jobSet/jobDef skiped = %d"%error_skip
        LOGGER.warning("Missing jobSet/jobDef skiped = %d"%error_skip)
    if processed_rows == 0:
        write_document(document,"%s/zero_process.html" % WORKDIR)
        LOGGER.warning("Processed 0 rows")

    return (set_last,processed_rows,sum_nJobs,lost_nJobs,eff_records, exist_records, in_buf_records)

def run():
    global db, QUERY_HOUR, QUERY_LIMIT, USERNAME
    #t1 = time.time()
    LOGGER.info(u'Starting run.')
    LOGGER.info(u'Retrieving document.')
    document = get_document()
    document_filename = '/tmp/%s/pbm.json' % (USERNAME)
    f = open(document_filename, 'w')
    f.write(document)
    f.close()
    LOGGER.info(u'Document retrieved.')
    LOGGER.info(u'Processing of retrieved document.')
    t2 = time.time()
    set_last, processed_rows, sum_nJobs, lost_nJobs, eff_records, \
        exist_records, in_buf_records = parse_document(document_filename)
    t3 = time.time()
    LOGGER.info(u'Finished processing of retrieved document.')
    LOGGER.info(u'Increasing DB counters.')
    db.add_logs(eff_records)
    db.increase_logs_count(exist_records)
    db.increase_buf_count(in_buf_records)
    LOGGER.info(u'Finished increasing DB counters.')
    
    LOGGER.info(u'Re-setting last_updated.')
    if set_last is not None:
        db.set_last_updated_time(set_last) # set when all done.
    LOGGER.info(u'Finished re-setting last_updated: %s' % (set_last))
    
    time_parse = t3-t2
    
    logs_count = len(eff_records)+len(exist_records)+len(in_buf_records)
    
    print u'INFO: %s Limit: %d/%d Effective: %d/%d nJobs: %d ParsingTime: %d nJobsUnprocess: %d' % (set_last, QUERY_LIMIT, QUERY_HOUR, logs_count, processed_rows, sum_nJobs, time_parse, lost_nJobs)
    LOGGER.info(u'%s Limit: %d/%d Effective: %d/%d nJobs: %d ParsingTime: %d nJobsUnprocess: %d'%(set_last,QUERY_LIMIT,QUERY_HOUR,logs_count,processed_rows,sum_nJobs,time_parse,lost_nJobs))


def main():
    global USERNAME
    pid = str(os.getpid())
    pidfile = "/tmp/%s/pbm_pidfile" % (USERNAME)
    LOGGER.debug(u'PID: %s PIDFILE: %s' % (pid, pidfile) )
    if os.path.isfile(pidfile):
        print u'WARNING: another parser (in %s) is running.'%(pidfile)
        LOGGER.critical(u'Another parser (in %s) is running. Skipping this run.'%(pidfile))
        sys.exit()
    else:
        file(pidfile,'w').write(pid)
        run()
        os.unlink(pidfile)


if __name__ == "__main__":
    main()


