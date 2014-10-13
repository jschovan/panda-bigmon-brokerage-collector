# -*- coding: utf-8 -*-
from BSXPath import BSXPathEvaluator,XPathResult, XPathExpression
from BeautifulSoup import BeautifulSoup
### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import pycurl
from pd2p_monitoring import WORKDIR


OUTPUT_FILENAME_PREFIX = 'pd2pLog'

#MESSAGE_CATEGORIES=[' - SKIPPED ', ' - triggered ', ' - UNSELECTEDT2 ', ' - SELECTEDT2 ']
MESSAGE_CATEGORIES=[' - action=SKIPPED ', ' - triggered ', ' - action=UNSELECTEDT2 ', ' - action=SELECTEDT1 ', \
                    ' - action=SELECTEDT2 ', ' - action=SELECTEDT2_T1MOU ', ' - action=SELECTEDT2_T2MOU ' ]
SKIPPED_REASONS=['TOO_MANY_T2_REPLICAS', 'TOO_MANY_T2_SUBSCRIPTIONS']

WEIGHT_NA_STRING="NA"
WEIGHT_NA_VALUE=-2
WEIGHT_T2_T1MOU_VALUE=-3
WEIGHT_T2_T2MOU_VALUE=-4
WEIGHT_T1_VALUE=-4


class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def get_URL():
    return 'http://panda.cern.ch/server/pandamon/query?mode=mon&name=panda.mon.prod&type=pd2p&hours=2&limit=20000'
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
        
        
        message_category=""
        message_date=""
        message_time=""
        message_dataset=""
        message_site="no.site"
        message_reason="no.reason"
        message_weight="no.weight"
        message_weight_val=0
        message_weight_0=0
        message_weight_1=0
        message_weight_2=0
        message_weight_3=0
        message_weight_4=0
        message_weight_5=0
        message_treshold="no.treshold"
        message_treshold_current=0
        message_treshold_expected=0
        
        ###print;print;print
        ###print u'DEBUG: ln113: cell_message=', cell_message
        
        ## SKIPPED
        if is_this_category(cell_message, ' - action=SKIPPED '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            #print  u'test', 'row:', row_counter, u'|tmp_message|=', len(tmp_message), tmp_message
            ###print u'DEBUG ln123: tmp_message=', tmp_message
            message_category="SKIPPED"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            message_dataset=tmp_message[5].split('=')[1]
            message_reason=tmp_message[4].split('=')[1]
            ### SKIPPED_REASONS=['TOO_MANY_T2_REPLICAS', 'TOO_MANY_T2_SUBSCRIPTIONS']
            if message_reason=="TOO_MANY_T2_REPLICAS":
                try:
                    #message_treshold_current=re.sub(r"[)(>]", '', re.sub("&gt", '', str(tmp_message[13])  ) ).split('=')[0]
                    #message_treshold_expected=re.sub(r"[)]", '', str(tmp_message[14]) ).split('=')[1]
                    message_treshold_current=re.sub(r"[)(>]", '', str(tmp_message[13]) ).split('=')[0]
                    message_treshold_expected=re.sub(r"[)(>]", '', str(tmp_message[13]) ).split('=')[1]
                except: 
                    message_treshold_current=-1
                    message_treshold_expected=-1
                    #print  u'test', 'row:', row_counter, u'|tmp_message|=', len(tmp_message), tmp_message
            elif message_reason=="TOO_MANY_T2_SUBSCRIPTIONS": 
                try:
                    #message_treshold_current=re.sub(r"[)(>]", '', re.sub("&gt", '', str(tmp_message[11])  ) ).split('=')[0]
                    #message_treshold_expected=re.sub(r"[)]", '', str(tmp_message[12]) ).split('=')[1]
                    message_treshold_current=re.sub(r"[)(>]", '', str(tmp_message[12]) ).split('=')[0]
                    message_treshold_expected=re.sub(r"[)]", '', str(tmp_message[12]) ).split('=')[1]
                except: 
                    message_treshold_current=-1
                    message_treshold_expected=-1
                    #print  u'test', 'row:', row_counter, u'|tmp_message|=', len(tmp_message), tmp_message
            #message_treshold=tmp_message[13]
            #print u'row:', row_counter, message_treshold, re.sub(r"[)(]", '', str(message_treshold) )
            #message_treshold_current=re.sub(r"[)(>]", '', re.sub("&gt", '', str(tmp_message[13])  ) ).split('=')[0]
            #message_treshold_expected=re.sub(r"[)]", '', str(tmp_message[13]) ).split('=')[1]
            #message_weight=0
            #message_weight_val=0.0
            #message_weight_0=0
            #message_weight_1=0
            #message_weight_2=0
            #message_weight_3=0
            #message_weight_4=0
            #message_weight_5=0
            #print u'test', message_date, message_time, message_dataset, message_reason, message_treshold_current, message_treshold_expected
            #print u'test::', tmp_message
        ## triggered
        if is_this_category(cell_message, ' - triggered '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            ###print u'DEBUG ln166: tmp_message=', tmp_message
            message_category="triggered"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            message_dataset=tmp_message[6]
            #message_weight=0
            #message_weight_val=0.0
            #message_weight_0=0
            #message_weight_1=0
            #message_weight_2=0
            #message_weight_3=0
            #message_weight_4=0
            #message_weight_5=0
            #message_treshold=""
            #message_treshold_current=0
            #message_treshold_expected=0
            ###print u'test', message_date, message_time, message_dataset
        ## UNSELECTEDT2
        if is_this_category(cell_message, ' - action=UNSELECTEDT2 '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            ###print u'DEBUG ln184: tmp_message=', tmp_message
            message_category="UNSELECTED"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            try:
                message_dataset=tmp_message[6].split('=')[1]
            except IndexError:
                dataset_field = ""
                for tmp_item in tmp_message: 
                    if re.search('^dataset=', tmp_item):
                        message_dataset=tmp_item.split('=')[1]
                        break
            message_site=tmp_message[4].split('=')[1]
            message_weight=tmp_message[5].split('=')[1]
            if message_weight == WEIGHT_NA_STRING:
                message_weight=message_weight_0=message_weight_1=message_weight_2=message_weight_3=message_weight_4=message_weight_5=WEIGHT_NA_VALUE
                message_weight_val=WEIGHT_NA_VALUE
            else:
                #message_weight_val=eval(float(message_weight)*1.0)
                message_weight_params=re.sub(r"[()]", '', re.sub(r"[+/*]", ';', str(message_weight) ) ).split(';')
                message_weight_0=message_weight_params[0]
                message_weight_1=message_weight_params[1]
                message_weight_2=message_weight_params[2]
                message_weight_3=message_weight_params[3]
                message_weight_4=message_weight_params[4]
                message_weight_5=message_weight_params[5]
                try:
                    message_weight_val=(float(message_weight_0)+float(message_weight_1)/float(message_weight_2))*float(message_weight_3)/float(message_weight_4)/float(message_weight_5)
                except:
                    message_weight_val=-1
                    #print  u'test', 'row:', row_counter, u'|tmp_message|=', len(tmp_message), tmp_message
            #message_treshold=""
            #message_treshold_current=0
            #message_treshold_expected=0
            ###print u'test', message_date, message_time, message_dataset, message_site, message_weight, message_weight_0, message_weight_1, message_weight_2, message_weight_3, message_weight_4, message_weight_5
        ## SELECTEDT1
        if is_this_category(cell_message, ' - action=SELECTEDT1 '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            ###print u'DEBUG ln213: tmp_message=', tmp_message
            message_category="SELECTEDT1"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            #message_dataset=tmp_message[6].split('=')[1]
            try:
                message_dataset=tmp_message[6].split('=')[1]
            except IndexError:
                dataset_field = ""
                for tmp_item in tmp_message: 
                    if re.search('^dataset=', tmp_item):
                        message_dataset=tmp_item.split('=')[1]
                        break
            message_site=tmp_message[4].split('=')[1]
            #message_weight=tmp_message[5].split('=')[1]
            #message_weight_params=re.sub(r"[()]", '', re.sub(r"[+/*]", ';', str(message_weight) ) ).split(';')
            #print u'DEBUG ln246: message_weight_params=', message_weight_params
            #message_weight_0=message_weight_params[0]
            #message_weight_1=message_weight_params[1]
            #message_weight_2=message_weight_params[2]
            #message_weight_3=message_weight_params[3]
            #message_weight_4=message_weight_params[4]
            #message_weight_5=message_weight_params[5]
            #try:
            #    message_weight_val=(float(message_weight_0)+float(message_weight_1)/float(message_weight_2))*float(message_weight_3)/float(message_weight_4)/float(message_weight_5)
            #except:
            #    message_weight_val=-1
            message_weight=message_weight_0=message_weight_1=message_weight_2=message_weight_3=message_weight_4=message_weight_5=message_weight_val=WEIGHT_T1_VALUE
        ## SELECTEDT2
        if is_this_category(cell_message, ' - action=SELECTEDT2 '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            ###print u'DEBUG ln213: tmp_message=', tmp_message
            message_category="SELECTEDT2"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            #message_dataset=tmp_message[6].split('=')[1]
            try:
                message_dataset=tmp_message[6].split('=')[1]
            except IndexError:
                dataset_field = ""
                for tmp_item in tmp_message: 
                    if re.search('^dataset=', tmp_item):
                        message_dataset=tmp_item.split('=')[1]
                        break
            message_site=tmp_message[4].split('=')[1]
            message_weight=tmp_message[5].split('=')[1]
            message_weight_params=re.sub(r"[()]", '', re.sub(r"[+/*]", ';', str(message_weight) ) ).split(';')
            message_weight_0=message_weight_params[0]
            message_weight_1=message_weight_params[1]
            message_weight_2=message_weight_params[2]
            message_weight_3=message_weight_params[3]
            message_weight_4=message_weight_params[4]
            message_weight_5=message_weight_params[5]
            try:
                message_weight_val=(float(message_weight_0)+float(message_weight_1)/float(message_weight_2))*float(message_weight_3)/float(message_weight_4)/float(message_weight_5)
            except:
                message_weight_val=-1
        ## SELECTEDT2_T1MOU
        if is_this_category(cell_message, ' - action=SELECTEDT2_T1MOU '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            ###print u'DEBUG ln213: tmp_message=', tmp_message
            message_category="SELECTEDT2_T1MOU"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            #message_dataset=tmp_message[6].split('=')[1]
            try:
                message_dataset=tmp_message[6].split('=')[1]
            except IndexError:
                dataset_field = ""
                for tmp_item in tmp_message: 
                    if re.search('^dataset=', tmp_item):
                        message_dataset=tmp_item.split('=')[1]
                        break
            message_site=tmp_message[4].split('=')[1]
            #message_weight=tmp_message[5].split('=')[1]
            #message_weight_params=re.sub(r"[()]", '', re.sub(r"[+/*]", ';', str(message_weight) ) ).split(';')
            #message_weight_0=message_weight_params[0]
            #message_weight_1=message_weight_params[1]
            #message_weight_2=message_weight_params[2]
            #message_weight_3=message_weight_params[3]
            #message_weight_4=message_weight_params[4]
            #message_weight_5=message_weight_params[5]
            #try:
            #    message_weight_val=(float(message_weight_0)+float(message_weight_1)/float(message_weight_2))*float(message_weight_3)/float(message_weight_4)/float(message_weight_5)
            #except:
            #    message_weight_val=-1
            ###message_weight_params=re.sub(r"[()]", '', re.sub(r"[+/*]", ';', str(message_weight) ) ).split(';')
            message_weight=message_weight_0=message_weight_1=message_weight_2=message_weight_3=message_weight_4=message_weight_5=message_weight_val=WEIGHT_T2_T1MOU_VALUE
        ## SELECTEDT2_T2MOU
        if is_this_category(cell_message, ' - action=SELECTEDT2_T2MOU '):
            tmp_message=re.sub(r'\s+', ';', str( cell_message.replace('&nbsp;', ' ') ) ).split(';')
            ###print u'DEBUG ln213: tmp_message=', tmp_message
            message_category="SELECTEDT2_T2MOU"
            message_date=tmp_message[0]
            message_time=tmp_message[1]
            #message_dataset=tmp_message[6].split('=')[1]
            try:
                message_dataset=tmp_message[6].split('=')[1]
            except IndexError:
                dataset_field = ""
                for tmp_item in tmp_message: 
                    if re.search('^dataset=', tmp_item):
                        message_dataset=tmp_item.split('=')[1]
                        break
            message_site=tmp_message[4].split('=')[1]
            #message_weight=tmp_message[5].split('=')[1]
            #message_weight_params=re.sub(r"[()]", '', re.sub(r"[+/*]", ';', str(message_weight) ) ).split(';')
            #message_weight_0=message_weight_params[0]
            #message_weight_1=message_weight_params[1]
            #message_weight_2=message_weight_params[2]
            #message_weight_3=message_weight_params[3]
            #message_weight_4=message_weight_params[4]
            #message_weight_5=message_weight_params[5]
            #try:
            #    message_weight_val=(float(message_weight_0)+float(message_weight_1)/float(message_weight_2))*float(message_weight_3)/float(message_weight_4)/float(message_weight_5)
            #except:
            #    message_weight_val=-1
            message_weight=message_weight_0=message_weight_1=message_weight_2=message_weight_3=message_weight_4=message_weight_5=message_weight_val=WEIGHT_T2_T2MOU_VALUE
        #print u'DEBUG::      message:', cell_message
        #print u'============='
        
        record = (message_date, message_time, message_category, message_dataset, message_site, \
                  message_reason, message_weight, \
                  message_weight_val, message_weight_0, message_weight_1, \
                  message_weight_2, message_weight_3, \
                  message_weight_4, message_weight_5, \
                  message_treshold_current, message_treshold_expected
                  )
        records.append(record)
        
    return records


def print_records(records, FILENAME):
    of = open(FILENAME, 'w')
    for record in records: 
        message_date, message_time, message_category, message_dataset, \
            message_site, message_reason, message_weight, \
            message_weight_val, message_weight_0, message_weight_1, \
            message_weight_2, message_weight_3, \
            message_weight_4, message_weight_5, \
            message_treshold_current, message_treshold_expected = record
        of.write('%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n' % (message_date, \
                message_time, message_category, message_dataset, message_site, \
                message_reason, message_weight_val, message_weight, \
                message_weight_0, message_weight_1, \
                message_weight_2, message_weight_3, \
                message_weight_4, message_weight_5, \
                message_treshold_current, message_treshold_expected) )
    of.close()


def write_document(document, FILENAME):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()


def run():
    document = get_document()
    write_document(document, '%s.html' % (OUTPUT_FILENAME_PREFIX) )
    rec = parse_document(document)
    print_records(rec, '%s.data' % (OUTPUT_FILENAME_PREFIX) )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "ERROR: too few input parameters"
        print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
        exit(1)
    else:
        OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


