# -*- coding: utf-8 -*-
from BSXPath import BSXPathEvaluator,XPathResult, XPathExpression
from BeautifulSoup import BeautifulSoup

from dashboard.dao.DAOFactory import DAOFactory
from dashboard.dao.DAOContext import DAOContext

### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import pycurl
#from pd2p_monitoring import WORKDIR


OUTPUT_FILENAME_PREFIX = 'analyBrokerageLog'

#MESSAGE_CATEGORIES=[' - SKIPPED ', ' - triggered ', ' - UNSELECTEDT2 ', ' - SELECTEDT2 ']
MESSAGE_CATEGORIES=[' action=skip ', ' action=choose ', ' use ']
SKIPPED_REASONS=['notmaxweight', 'missingapp','nopilot']

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def get_URL():
    return 'http://panda.cern.ch/server/pandamon/query?mode=mon&name=panda.mon.prod&type=analy_brokerage&hours=2&limit=100'
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

def parse_document(document):
    BSXdocument = BSXPathEvaluator(document)
    
    XPath_table = './/*[@id="main"]/p[2]/table'
    XPath_table_body = '%s/tbody' % (XPath_table)
    XPath_table_header = '%s/tr[1]' % (XPath_table_body)
    XPath_table_lines = '%s/tr' % (XPath_table_body)
    rows = BSXdocument.getItemList(XPath_table_lines)[1:]
    
    records = []
    
    for row_counter in xrange(len(rows)):
        record = ()
        SHIFT=0
        
        
        row = rows[row_counter]
        XPath_table_row = '%s/tr[%d]' % (XPath_table_body, row_counter+1)
        
        XPath_table_row_cell_category = '%s/td[%d]/text()' % (XPath_table_row, 1)
        cell_category = BSXdocument.getItemList(XPath_table_row_cell_category)
        if len(cell_category)>0:
            cell_category = cell_category[0]
        
        XPath_table_row_cell_type = '%s/td[%d]/text()' % (XPath_table_row, 2)
        cell_type = BSXdocument.getItemList(XPath_table_row_cell_type)
        if len(cell_type)>0:
            cell_type = cell_type[0]
        
        XPath_table_row_cell_time = '%s/td[%d]/text()' % (XPath_table_row, 3)
        cell_time = BSXdocument.getItemList(XPath_table_row_cell_time)
        if len(cell_time)>0:
            cell_time = cell_time[0]
        
        XPath_table_row_cell_level = '%s/td[%d]/text()' % (XPath_table_row, 4)
        cell_level = BSXdocument.getItemList(XPath_table_row_cell_level)
        if len(cell_level)>0:
            cell_level = cell_level[0]
        
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
        
        print u'DUBUG:(',row_counter,') cell message=', cell_message
        
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
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
            message_reason = message_skip[2].split('=')[1].strip()
            if re.search('=',message_skip[4]):
                message_weight = message_skip[4].split('=')[1].strip()
            else:
                message_reason = '_'.join(message_skip[3:]).strip('_')
        
        ## choose
        if is_this_category(cell_message, ' action=choose '):
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
        if is_this_category(cell_message, ' use '):
            message_use = tmp_message[2].split(' ')
            message_action = message_use[0].strip()
            message_site = message_use[1].strip()
            message_reason = '_'.join(message_use[3:]).strip('_')
            if is_this_category(message_reason, 'site'):
                message_category = "A"
            if is_this_category(message_reason, 'cloud'):
                message_category = "B"
        if message_category in ['A','B','C']:                
            record = (message_date, message_time, message_category, \
                  message_dn, message_jobset, message_jobdef, \
                  message_action, message_site, message_reason, message_weight \
                  )
            records.append(record)
        
    return records


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
    document = get_document()
    # write_document(document, '%s.html' % (OUTPUT_FILENAME_PREFIX) )
    rec = parse_document(document)
    print_records(rec, '%s.data' % (OUTPUT_FILENAME_PREFIX) )
    print u'DEBUG: Done'
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


