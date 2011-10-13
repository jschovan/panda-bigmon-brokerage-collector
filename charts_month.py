# -*- coding: utf-8 -*-
from dailyDB import dailyDB

import re
import sys
import pycurl
import time

ADC_COLOR = {
             'CA': '#FF1F1F',
             'CERN': '#AE3C51',
             'DE': '#000000',
             'ES': '#EDBF00',
             'FR': '#0055A5',
             'IT': '#009246',
             'ND': '#6298FF',
             'NL': '#D97529',
             'TW': '#89000F',
             'UK': '#356C20',
             'US': '#00006B'
             }
CHARTS = [
          ["P1_month","Category A,B,C Analy - monthly"],
          ["P2_month","Top 10 sites of Category A - monthly"],
          ["P3_month","Cloud Analy of Category B - monthly"],
          ["P4_month","Top 10 sites of Category C - monthly"],
          ["P5_month","Cloud Analy of Category C - monthly"]
          ]
SQLS = [
        "select category, sum(count) nums from dailylog where logDate > '%s' group by category order by category",
        "select site, sum(count) nums from dailylog where category='A' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(count) nums from dailylog where category='B' and logDate > '%s' group by cloud order by nums DESC",
        "select site, sum(count) nums from dailylog where category='C' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(count) nums from dailylog where category='C' and logDate > '%s' group by cloud order by nums DESC"
        ]

db = dailyDB()
DATEFORMAT = "%Y-%m-%d"
last_updated = db.get_last_updated_time()
query_from = time.strftime(DATEFORMAT,time.localtime(time.time()-30*24*60*60)) # monthly

def parse_document_category():
    data = open('template/P1_month.html').read()
    title_text = CHARTS[0][1]
    comm = ""
    series_data = ""
    sql = SQLS[0]
    rs = db.query(sql%query_from)
    for row in rs:
        series_data = "%s %s ['%s', %d]"%(series_data,comm,row[0],row[1])
        comm = ","
    data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return data

def parse_document_site(idx):
    data = open('template/P1_month.html').read()
    title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    limit = 0
    others = 0
    for row in rs:
        limit += 1
        if limit <= 10:
            series_data = "%s %s ['%s', %d]"%(series_data,comm,row[0],row[1])
            comm = ","
        else:
            others += row[1]
    if others > 0:
        series_data = "%s %s ['others', %d]"%(series_data,comm,others)
    data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return data

def parse_document_cloud(idx):
    data = open('template/P1_month.html').read()
    title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    for row in rs:
        color = ADC_COLOR[row[0]]
        series_data = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data,comm,row[0],row[1],color)
        comm = ","
    data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return data

def write_document(document, FILENAME):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()


def run():
    document = parse_document_category()
    write_document(document, '%s.html' % CHARTS[0][0] )
    
    document = parse_document_site(1)
    write_document(document, '%s.html' % CHARTS[1][0] )
    document = parse_document_site(3)
    write_document(document, '%s.html' % CHARTS[3][0] )
    
    document = parse_document_cloud(2)
    write_document(document, '%s.html' % CHARTS[2][0] )
    document = parse_document_cloud(4)
    write_document(document, '%s.html' % CHARTS[4][0] )
    #rec,exist_rec,in_buf_rec = parse_document(document)
    # print_records(rec, '%s.data' % (OUTPUT_FILENAME_PREFIX) )
    print u'DEBUG: Done'
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


