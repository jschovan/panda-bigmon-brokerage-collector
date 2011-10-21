# -*- coding: utf-8 -*-
from dailyDB import dailyDB

import re
import sys
import pycurl
import time

interval_days = 7 # Weekly

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
          ["P1_week","Category A,B,C Analy - Weekly"],
          ["P2_week","Top 10 sites of Category A - Weekly"],
          ["P3_week","Cloud Analy of Category B - Weekly"],
          ["P4_week","Top 10 sites of Category C - Weekly"],
          ["P5_week","Cloud Analy of Category C - Weekly"],
          ["P6_week","Top 10 users - Weekly"]
          ]
SQLS = [
        "select category, sum(count) nums from dailylog where logDate > '%s' group by category order by category",
        "select site, sum(count) nums from dailylog where category='A' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(count) nums from dailylog where category='B' and logDate > '%s' group by cloud order by nums DESC",
        "select site, sum(count) nums from dailylog where category='C' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(count) nums from dailylog where category='C' and logDate > '%s' group by cloud order by nums DESC",
        "select dnUser, sum(count) nums from dailylog where logDate > '%s' group by dnUser order by nums DESC"
        ]

db = dailyDB()
DATEFORMAT = "%Y-%m-%d"
last_updated = db.get_last_updated_time()
query_from = time.strftime(DATEFORMAT,time.localtime(time.time()-interval_days*24*60*60))
data = open('panda_queues.json').read()
dic = eval(data)

def get_cloud_name(site):
    cloud = site
    for site_dic in dic:
        if site_dic['agis_ssb_site_name']==site:
            cloud = site_dic['cloud']
            break
    return cloud

def parse_document_category():
    data = open('template/P1_week.html').read()
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

def parse_document_site(idx,show_others=True):
    data = open('template/P1_week.html').read()
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
            # series_data = "%s %s ['%s', %d]"%(series_data,comm,row[0],row[1])
            cloud = get_cloud_name(row[0])
            color = ADC_COLOR[cloud]
            series_data = "%s %s {name: '%s (%s)', y: %d, color: '%s'}"%(series_data,comm,row[0],cloud,row[1],color)
            comm = ","
        else:
            others += row[1]
    if others > 0 and show_others:
        # series_data = "%s %s ['others', %d]"%(series_data,comm,others)
        series_data = "%s %s {name: 'others', y: %d, color: '#CCCCCC'}"%(series_data,comm,others)
    data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return data

def parse_document_cloud(idx):
    data = open('template/P1_week.html').read()
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

def parse_document_user(idx):
    data = open('template/P1_week.html').read()
    title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    limit = 0
    for row in rs:
        limit += 1
        if limit <= 10:
            series_data = "%s %s ['%s', %d]"%(series_data,comm,row[0],row[1])
            comm = ","
        else:
            break
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
    document = parse_document_site(3,False)
    write_document(document, '%s.html' % CHARTS[3][0] )
    
    document = parse_document_cloud(2)
    write_document(document, '%s.html' % CHARTS[2][0] )
    document = parse_document_cloud(4)
    write_document(document, '%s.html' % CHARTS[4][0] )

    document = parse_document_user(5)
    write_document(document, '%s.html' % CHARTS[5][0] )

    print u'DEBUG: Done'
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


