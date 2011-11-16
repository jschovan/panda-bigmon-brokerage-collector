# -*- coding: utf-8 -*-
from dailyDBV2 import dailyDBV2

import re
import sys
import pycurl
import time
import simplejson as json

interval_days = [7,30,90,365] # Weekly,monthly,seasonly,and yearly
pnames = ["Weekly","Monthly","Seasonly","Yearly"]
fnames = ["weeklyV2.html","monthlyV2.html","seasonlyV2.html","yearlyV2.html"]
nTop = 20
tabname = "dailylogV2"
db = dailyDBV2()
DATEFORMAT = "%Y-%m-%d"

CATENAME = {
            'A': 'A-User selected a site',
            'B': 'B-User selected a cloud',
            'C': 'C-Panda decides destination',
            'D': 'D-Skip by Panda',
            'E': 'E-User excluded a site'
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
          [
            ["Category A,B,C on Jobs - %s",
             "select category,sum(jobCount) from %s where  logDate > '%s' and category in ('A','B','C') group by category order by category"],
            ["Category A,B,C on jobDef - %s",
             "select category,sum(jobDefCount) from %s where  logDate > '%s' and category in ('A','B','C') group by category order by category"],
            ["Category A,B,C on jobSet - %s",
             "select category,count(distinct jobSet) from %s where  logDate > '%s' and category in ('A','B','C') group by category order by category"]
          ],
          [
            ["Category A (User selected a site) on Jobs - Top %d Sites - %s",
             "select site, sum(jobCount) nums from %s where category='A' and logDate > '%s' group by site order by nums DESC"],
            ["Category A (User selected a site) on jobDef - Top %d Sites - %s",
             "select site, sum(jobDefCount) nums from %s where category='A' and logDate > '%s' group by site order by nums DESC"],
            ["Category A (User selected a site) on jobSet - Top %d Sites - %s",
             "select site, count(distinct jobSet) nums from %s where category='A' and logDate > '%s' group by site order by nums DESC"]
          ],
          [
            ["Category A (User selected a site) on Jobs - Per Cloud - %s",
             "select cloud, sum(jobCount) nums from %s where category='A' and logDate > '%s' group by cloud order by nums DESC"],
            ["Category A (User selected a site) on jobDef - Per Cloud - %s",
             "select cloud, sum(jobdefCount) nums from %s where category='A' and logDate > '%s' group by cloud order by nums DESC"],
            ["Category A (User selected a site) on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='A' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          [
            ["Category B (User selected a cloud) on Jobs - Top %d Sites - %s",
             "select site, sum(jobCount) nums from %s where category='B' and logDate > '%s' group by site order by nums DESC"],
            ["Category B (User selected a cloud) on jobDef - Top %d Sites - %s",
             "select site, sum(jobDefCount) nums from %s where category='B' and logDate > '%s' group by site order by nums DESC"],
            ["Category B (User selected a cloud) on jobSet - Top %d Sites - %s",
             "select site, count(distinct jobSet) nums from %s where category='B' and logDate > '%s' group by site order by nums DESC"]
          ],
          [
            ["Category B (User selected a cloud) on Jobs - Per Cloud - %s",
             "select cloud, sum(jobCount) nums from %s where category='B' and logDate > '%s' group by cloud order by nums DESC"],
            ["Category B (User selected a cloud) on jobDef - Per Cloud - %s",
             "select cloud, sum(jobdefCount) nums from %s where category='B' and logDate > '%s' group by cloud order by nums DESC"],
            ["Category B (User selected a cloud) on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='B' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          [
            ["Category C (Panda decides destination) on Jobs - Top %d Sites - %s",
             "select site, sum(jobCount) nums from %s where category='C' and logDate > '%s' group by site order by nums DESC"],
            ["Category C (Panda decides destination) on jobDef - Top %d Sites - %s",
             "select site, sum(jobDefCount) nums from %s where category='C' and logDate > '%s' group by site order by nums DESC"],
            ["Category C (Panda decides destination) on jobSet - Top %d Sites - %s",
             "select site, count(distinct jobSet) nums from %s where category='C' and logDate > '%s' group by site order by nums DESC"]
          ],
          [
            ["Category C (Panda decides destination) on Jobs - Per Cloud - %s",
             "select cloud, sum(jobCount) nums from %s where category='C' and logDate > '%s' group by cloud order by nums DESC"],
            ["Category C (Panda decides destination) on jobDef - Per Cloud - %s",
             "select cloud, sum(jobdefCount) nums from %s where category='C' and logDate > '%s' group by cloud order by nums DESC"],
            ["Category C (Panda decides destination) on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='C' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          [
            ["Category E (User excluded a site) on distinct jobSet - Excluded / Non-Excluded - %s",
             "select count(distinct jobSet) nums from %s where category='E' and logDate > '%s'",
             "select count(distinct jobSet) nums from %s where category!='E' and logDate > '%s' and jobSet not in (select distinct jobSet from %s where category='E' and logDate > '%s')"]
          ],
          [
            ["Category E (User excluded a site) on jobSet - Top %d Sites - %s",
             "select site, count(distinct jobSet) nums from %s where category='E' and logDate > '%s' group by site order by nums DESC"]
          ],
          [
            ["Category E (User excluded a site) on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='E' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          [
            ["Jobs submitted by Country - %s",
             "select country, sum(jobCount) nums from %s where category in ('A','B','C') and logDate > '%s' group by country order by nums DESC"],
            ["jobDef submitted by Country - %s",
             "select country, sum(jobdefCount) nums from %s where category in ('A','B','C') and logDate > '%s' group by country order by nums DESC"],
            ["jobSet submitted by Country - %s",
             "select country, count(distinct jobSet) nums from %s where category in ('A','B','C') and logDate > '%s' group by country order by nums DESC"]
          ]
          ]

last_updated = db.get_last_updated_time()
query_from = time.strftime(DATEFORMAT,time.localtime(time.time()-interval_days[0]*24*60*60))
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

def parse_document_category(idx1,idx2):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[0][1]
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    for row in rs:
        series_data = "%s %s ['%s', %d]"%(series_data,comm,CATENAME[row[0]],row[1])
        comm = ","
    return series_data

def parse_document_site(idx1,idx2,show_others=True):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
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

def parse_document_cloud(idx1,idx2):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[idx][1]
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    for row in rs:
        color = ADC_COLOR[row[0]]
        series_data = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data,comm,row[0],row[1],color)
        comm = ","
    # data = data.replace('#TITLE_TEXT#',title_text).replace('#LAST_UPDATED#',last_updated).replace('#SERIES_DATA#',series_data)
    return series_data

def parse_document_excluded(idx1,idx2):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[idx][1]
    series_data = ""
    sql1 = CHARTS[idx1][idx2][1]
    sql2 = CHARTS[idx1][idx2][2]
    rs1 = db.query(sql1%(tabname,query_from))
    rs2 = db.query(sql2%(tabname,query_from,tabname,query_from))
    excluded = rs1[0][0]
    nonexcluded = rs2[0][0]
    series_data = "['Excluded', %s ],['Non-Excluded', %s]"%(excluded,nonexcluded)

    return series_data

def parse_document_country(idx1,idx2):
    # data = open('template/P1_week.html').read()
    # title_text = CHARTS[0][1]
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    for row in rs:
        series_data = "%s %s ['%s', %d]"%(series_data,comm,row[0],row[1])
        comm = ","
    return series_data

def write_document(document, FILENAME='weeklyV2.html'):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()

def run(fidx):
    data = open('template/CHART_brokerageV2.html').read()
    data = data.replace('#LAST_UPDATED#',last_updated)

    data = data.replace('#TITLE_TEXT00#',CHARTS[0][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT01#',CHARTS[0][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT02#',CHARTS[0][2][0]%pnames[fidx])
    
    data = data.replace('#TITLE_TEXT10#',CHARTS[1][0][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT11#',CHARTS[1][1][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT12#',CHARTS[1][2][0]%(nTop,pnames[fidx]))

    data = data.replace('#TITLE_TEXT20#',CHARTS[2][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT21#',CHARTS[2][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT22#',CHARTS[2][2][0]%pnames[fidx])
    
    data = data.replace('#TITLE_TEXT30#',CHARTS[3][0][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT31#',CHARTS[3][1][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT32#',CHARTS[3][2][0]%(nTop,pnames[fidx]))

    data = data.replace('#TITLE_TEXT40#',CHARTS[4][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT41#',CHARTS[4][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT42#',CHARTS[4][2][0]%pnames[fidx])
    
    data = data.replace('#TITLE_TEXT50#',CHARTS[5][0][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT51#',CHARTS[5][1][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT52#',CHARTS[5][2][0]%(nTop,pnames[fidx]))

    data = data.replace('#TITLE_TEXT60#',CHARTS[6][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT61#',CHARTS[6][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT62#',CHARTS[6][2][0]%pnames[fidx])
    
    data = data.replace('#TITLE_TEXT70#',CHARTS[7][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT80#',CHARTS[8][0][0]%(nTop,pnames[fidx]))
    data = data.replace('#TITLE_TEXT90#',CHARTS[9][0][0]%pnames[fidx])

    data = data.replace('#TITLE_TEXT100#',CHARTS[10][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT101#',CHARTS[10][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT102#',CHARTS[10][2][0]%pnames[fidx])
    
    series_data00 = parse_document_category(0,0)
    series_data01 = parse_document_category(0,1)
    series_data02 = parse_document_category(0,2)
    
    series_data10 = parse_document_site(1,0)
    series_data11 = parse_document_site(1,1)
    series_data12 = parse_document_site(1,2)
    
    series_data20 = parse_document_cloud(2,0)
    series_data21 = parse_document_cloud(2,1)
    series_data22 = parse_document_cloud(2,2)
    
    series_data30 = parse_document_site(3,0)
    series_data31 = parse_document_site(3,1)
    series_data32 = parse_document_site(3,2)
    
    series_data40 = parse_document_cloud(4,0)
    series_data41 = parse_document_cloud(4,1)
    series_data42 = parse_document_cloud(4,2)
    
    series_data50 = parse_document_site(5,0)
    series_data51 = parse_document_site(5,1)
    series_data52 = parse_document_site(5,2)
    
    series_data60 = parse_document_cloud(6,0)
    series_data61 = parse_document_cloud(6,1)
    series_data62 = parse_document_cloud(6,2)
    
    series_data70 = parse_document_excluded(7,0)
    series_data80 = parse_document_site(8,0)
    series_data90 = parse_document_cloud(9,0)
    
    series_data100 = parse_document_country(10,0)
    series_data101 = parse_document_country(10,1)
    series_data102 = parse_document_country(10,2)
    
    data = data.replace('#SERIES_DATA00#',series_data00)
    data = data.replace('#SERIES_DATA01#',series_data01)
    data = data.replace('#SERIES_DATA02#',series_data02)
    
    data = data.replace('#SERIES_DATA10#',series_data10)
    data = data.replace('#SERIES_DATA11#',series_data11)
    data = data.replace('#SERIES_DATA12#',series_data12)
    
    data = data.replace('#SERIES_DATA20#',series_data20)
    data = data.replace('#SERIES_DATA21#',series_data21)
    data = data.replace('#SERIES_DATA22#',series_data22)
    
    data = data.replace('#SERIES_DATA30#',series_data30)
    data = data.replace('#SERIES_DATA31#',series_data31)
    data = data.replace('#SERIES_DATA32#',series_data32)
    
    data = data.replace('#SERIES_DATA40#',series_data40)
    data = data.replace('#SERIES_DATA41#',series_data41)
    data = data.replace('#SERIES_DATA42#',series_data42)
    
    data = data.replace('#SERIES_DATA50#',series_data50)
    data = data.replace('#SERIES_DATA51#',series_data51)
    data = data.replace('#SERIES_DATA52#',series_data52)
    
    data = data.replace('#SERIES_DATA60#',series_data60)
    data = data.replace('#SERIES_DATA61#',series_data61)
    data = data.replace('#SERIES_DATA62#',series_data62)
    
    data = data.replace('#SERIES_DATA70#',series_data70)
    data = data.replace('#SERIES_DATA80#',series_data80)
    data = data.replace('#SERIES_DATA90#',series_data90)

    data = data.replace('#SERIES_DATA100#',series_data100)
    data = data.replace('#SERIES_DATA101#',series_data101)
    data = data.replace('#SERIES_DATA102#',series_data102)

    write_document(data,fnames[fidx])

    print u'DEBUG: Done'
    


if __name__ == "__main__":
    
    #if len(sys.argv) < 2:
    #    print "ERROR: too few input parameters"
    #    print "USAGE: python   parse_table_pd2p_log.py   OUTPUT_FILENAME_PREFIX"
    #    exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run(0) # weekly
    run(1) # monthly
    run(2) # seasonly
    run(3) # yearly
    


