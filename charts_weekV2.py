# -*- coding: utf-8 -*-
from dailyDBV2 import dailyDBV2

import re
import sys
import pycurl
import time
import simplejson as json

interval_days = 7 # Weekly
pname = "Weekly"
CATENAME = {
            'A': 'A:Site by User',
            'B': 'B:Cloud by User',
            'C': 'C:Choose by Panda',
            'D': 'D:Skip by Panda',
            'E': 'E:Exclude by User'
            }

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
          ["P1_week","Category A,B,C,E Analy - %s"%pname],
          ["P2_week","Top 10 sites of Category A (Site by User) - %s"%pname],
          ["P3_week","Cloud Analy of Category B (Cloud by User) - %s"%pname],
          ["P4_week","Top 20 sites of Category C (Choose by Panda) - %s"%pname],
          ["P5_week","Cloud Analy of Category C (Choose by Panda) - %s"%pname],
          ["P6_week","Top 20 sites of Category E (Exclude by User) - %s"%pname],
          ["P7_week","Cloud Analy of Category E (Exclude by User) - %s"%pname],
          ["P11_week","Category A,B,C Analy - %s"%pname]
          ]
SQLS = [
        "select category, sum(jobdefCount) nums from dailylogV2 where logDate > '%s' group by category order by category",
        "select site, sum(jobdefCount) nums from dailylogV2 where category='A' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(jobdefCount) nums from dailylogV2 where category='B' and logDate > '%s' group by cloud order by nums DESC",
        "select site, sum(jobdefCount) nums from dailylogV2 where category='C' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(jobdefCount) nums from dailylogV2 where category='C' and logDate > '%s' group by cloud order by nums DESC",
        "select site, sum(jobdefCount) nums from dailylogV2 where category='E' and logDate > '%s' group by site order by nums DESC",
        "select cloud, sum(jobdefCount) nums from dailylogV2 where category='E' and logDate > '%s' group by cloud order by nums DESC",
        "select category, sum(jobdefCount) nums from dailylogV2 where category in ('A','B','C') and logDate > '%s' group by category order by category"
        ]

db = dailyDBV2()
DATEFORMAT = "%Y-%m-%d"
last_updated = db.get_last_updated_time()
query_from = time.strftime(DATEFORMAT,time.localtime(time.time()-interval_days*24*60*60))
# get cloud name
fjson = open('panda_queues.json','r')
data = fjson.read()
dic = json.loads(data)
fjson.close()

def get_cloud_name(site):
    cloud = site
    for site_dic in dic:
        if site_dic['agis_ssb_site_name']==site:
            cloud = site_dic['cloud']
            break
    return cloud

def parse_document_category(idx):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[0][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    for row in rs:
        series_data = "%s %s ['%s', %d]"%(series_data,comm,CATENAME[row[0]],row[1])
        comm = ","
    # data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return series_data

def parse_document_site(idx,show_others=True,nTop=10):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    limit = 0
    others = 0
    for row in rs:
        limit += 1
        if limit <= nTop:
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
    # data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return series_data

def parse_document_cloud(idx):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    for row in rs:
        color = ADC_COLOR[row[0]]
        series_data = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data,comm,row[0],row[1],color)
        comm = ","
    # data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return series_data

def parse_document_user(idx, nTop=10):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = SQLS[idx]
    rs = db.query(sql%query_from)
    limit = 0
    for row in rs:
        limit += 1
        if limit <= nTop:
            series_data = "%s %s ['%s', %d]"%(series_data,comm,row[0],row[1])
            comm = ","
        else:
            break
    # data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return series_data

def write_document(document, FILENAME='weeklyV2.html'):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()

def run():
    data = open('template/CHART_brokerageV2.html').read()
    data = data.replace('#LAST_UPDATED#',last_updated)

    data = data.replace('#TITLE_TEXT1#',CHARTS[0][1])
    data = data.replace('#TITLE_TEXT2#',CHARTS[1][1])
    data = data.replace('#TITLE_TEXT3#',CHARTS[2][1])
    data = data.replace('#TITLE_TEXT4#',CHARTS[3][1])
    data = data.replace('#TITLE_TEXT5#',CHARTS[4][1])
    data = data.replace('#TITLE_TEXT6#',CHARTS[5][1])
    data = data.replace('#TITLE_TEXT7#',CHARTS[6][1])
    data = data.replace('#TITLE_TEXT8#',CHARTS[7][1])
    
    series_data1 = parse_document_category(0)   
    series_data8 = parse_document_category(7)   
    series_data2 = parse_document_site(1)
    series_data3 = parse_document_cloud(2)
    series_data4 = parse_document_site(3,True,20)
    series_data5 = parse_document_cloud(4)
    series_data6 = parse_document_site(5,True,20)
    series_data7 = parse_document_cloud(6)
    # document = parse_document_user(5)
    
    data = data.replace('#SERIES_DATA1#',series_data1)
    data = data.replace('#SERIES_DATA8#',series_data8)
    data = data.replace('#SERIES_DATA2#',series_data2)
    data = data.replace('#SERIES_DATA3#',series_data3)
    data = data.replace('#SERIES_DATA4#',series_data4)
    data = data.replace('#SERIES_DATA5#',series_data5)
    data = data.replace('#SERIES_DATA6#',series_data6)
    data = data.replace('#SERIES_DATA7#',series_data7)

    write_document(data)

    print u'DEBUG: Done'
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run()
    


