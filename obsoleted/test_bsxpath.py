# -*- coding: utf-8 -*-
from BSXPath import BSXPathEvaluator,XPathResult, XPathExpression
from BeautifulSoup import BeautifulSoup
### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import os
import pycurl
import time

QUERY_HOUR = 1
QUERY_LIMIT = 50

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def get_URL():
    return 'http://panda.cern.ch/server/pandamon/query?mode=mon&name=panda.mon.prod&type=analy_brokerage&hours=%d&limit=%d'%(QUERY_HOUR,QUERY_LIMIT)


def get_document():
    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL, get_URL())
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
    
    return t.contents

def parse_document(document):
    BSXdocument = BSXPathEvaluator(document)
    
    XPath_table = './/*[@id="main"]/p[2]/table'
    XPath_table_body = '%s/tbody' % (XPath_table)
    XPath_table_header = '%s/tr[1]' % (XPath_table_body)
    XPath_table_lines = '%s/tr' % (XPath_table_body)
    rows = BSXdocument.getItemList(XPath_table_lines)[1:]
    
    for row_counter in xrange(len(rows)):
        row = rows[row_counter]
        # print row
        # print "======"
        rowDoc = BSXPathEvaluator('%s'%row)

        XPath_table_row = '/'

        XPath_table_row_cell_category = '%s/td[%d]/text()' % (XPath_table_row, 1)
        cell_category = rowDoc.getFirstItem(XPath_table_row_cell_category)
        
        XPath_table_row_cell_type = '%s/td[%d]/text()' % (XPath_table_row, 2)
        cell_type = rowDoc.getFirstItem(XPath_table_row_cell_type)

        XPath_table_row_cell_time = '%s/td[%d]/text()' % (XPath_table_row, 3)
        cell_time = rowDoc.getFirstItem(XPath_table_row_cell_time)

        XPath_table_row_cell_level = '%s/td[%d]/text()' % (XPath_table_row, 4)
        cell_level = rowDoc.getFirstItem(XPath_table_row_cell_level)

        XPath_table_row_cell_message = '%s/td[%d]/text()' % (XPath_table_row, 5)
        cell_message = rowDoc.getFirstItem(XPath_table_row_cell_message)
        
        print "======", row_counter, "======"
        print "Category:",cell_category
        print "Type:",cell_type
        print "Time:",cell_time
        print "Level:",cell_level
        print "Message:",cell_message
        
    return rows

def run():
    document = get_document()
    rows = parse_document(document)

if __name__ == "__main__":
    run()
    


