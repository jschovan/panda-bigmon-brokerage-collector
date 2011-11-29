# -*- coding: utf-8 -*-
from dailyDBV2 import dailyDBV2

import re
import sys
import pycurl
import time
import simplejson as json

from ADC_colors import ADC_COLOR

interval_days = [7,30,90,365] # Weekly,monthly,seasonly,and yearly
pnames = ["Weekly","Monthly","Seasonly","Yearly"]
fnames = ["weeklyV2.html","monthlyV2.html","seasonlyV2.html","yearlyV2.html"]
NTOP = 20
PLOW = 1 # percentage lower than this belong to "others"
tabname = "dailylogV2"
db = dailyDBV2()
DATEFORMAT = "%Y-%m-%d"

COUNTRY_CLOUD = {
                 'au':'CA',
                 'ca':'CA',
                 'ch':'CERN', # 'CERN ND DE',
                 'cn':'FR',
                 'cz':'DE',
                 'de':'DE',
                 'dk':'ND',
                 'es':'ES',
                 'fr':'FR',
                 'il':'NL',
                 'it':'IT',
                 'jp':'FR',
                 'no':'ND',
                 'pl':'DE',
                 'pt':'ES',
                 'ru':'NL',
                 'se':'ND',
                 'tr':'NL',
                 'tw':'TW',
                 'uk':'UK',
                 'us':'US',
                 'za':'IT',
                 'None':'NONE'
                 }

CATENAME = {
            'A': 'User selected a site',
            'B': 'User selected a cloud',
            'C': 'Panda decides destination',
            'D': 'Skip by Panda',
            'E': 'User excluded a site'
            }

CHARTS = {
          "ABC":[
            ["[User selected a site/User selected a cloud/Panda Brokerage decision] on Jobs - %s",
             "select category,sum(jobCount) from %s where  logDate > '%s' and category in ('A','B','C') group by category order by category"],
            ["[User selected a site/User selected a cloud/Panda Brokerage decision] on jobDef - %s",
             "select category,sum(jobDefCount) from %s where  logDate > '%s' and category in ('A','B','C') group by category order by category"],
            ["[User selected a site/User selected a cloud/Panda Brokerage decision] on jobSet - %s",
             "select category,count(distinct jobSet) from %s where  logDate > '%s' and category in ('A','B','C') group by category order by category"]
          ],
          "ASite":[
            ["[User selected a site] on Jobs - Top Sites higher than %d%% - %s",
             "select site, sum(jobCount) nums from %s where category='A' and logDate > '%s' group by site order by nums DESC",
             "select sum(jobCount) nums from %s where category='A' and logDate > '%s'"],
            ["[User selected a site] on jobDef - Top Sites higher than %d%% - %s",
             "select site, sum(jobDefCount) nums from %s where category='A' and logDate > '%s' group by site order by nums DESC",
             "select sum(jobDefCount) nums from %s where category='A' and logDate > '%s'"],
            ["[User selected a site] on jobSet - Top Sites higher than %d%% - %s",
             "select site, count(distinct jobSet) nums from %s where category='A' and logDate > '%s' group by site order by nums DESC",
             "select count(distinct jobSet) nums from %s where category='A' and logDate > '%s'"]
          ],
          "ACloud":[
            ["[User selected a site] on Jobs - Per Cloud - %s",
             "select cloud, sum(jobCount) nums from %s where category='A' and logDate > '%s' group by cloud order by nums DESC"],
            ["[User selected a site] on jobDef - Per Cloud - %s",
             "select cloud, sum(jobdefCount) nums from %s where category='A' and logDate > '%s' group by cloud order by nums DESC"],
            ["[User selected a site] on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='A' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          "BSite":[
            ["[User selected a cloud] on Jobs - Top %d Sites - %s",
             "select site, sum(jobCount) nums from %s where category='B' and logDate > '%s' group by site order by nums DESC"],
            ["[User selected a cloud] on jobDef - Top %d Sites - %s",
             "select site, sum(jobDefCount) nums from %s where category='B' and logDate > '%s' group by site order by nums DESC"],
            ["[User selected a cloud] on jobSet - Top %d Sites - %s",
             "select site, count(distinct jobSet) nums from %s where category='B' and logDate > '%s' group by site order by nums DESC"]
          ],
          "BCloud":[
            ["[User selected a cloud] on Jobs - Per Cloud - %s",
             "select cloud, sum(jobCount) nums from %s where category='B' and logDate > '%s' group by cloud order by nums DESC"],
            ["[User selected a cloud] on jobDef - Per Cloud - %s",
             "select cloud, sum(jobdefCount) nums from %s where category='B' and logDate > '%s' group by cloud order by nums DESC"],
            ["[User selected a cloud] on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='B' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          "CSite":[
            ["[Panda Brokerage decision] on Jobs - Top %d Sites - %s",
             "select site, sum(jobCount) nums from %s where category='C' and logDate > '%s' group by site order by nums DESC"],
            ["[Panda Brokerage decision] on jobDef - Top %d Sites - %s",
             "select site, sum(jobDefCount) nums from %s where category='C' and logDate > '%s' group by site order by nums DESC"]
          ],
          "CCloud":[
            ["[Panda Brokerage decision] on Jobs - Per Cloud - %s",
             "select cloud, sum(jobCount) nums from %s where category='C' and logDate > '%s' group by cloud order by nums DESC"],
            ["[Panda Brokerage decision] on jobDef - Per Cloud - %s",
             "select cloud, sum(jobdefCount) nums from %s where category='C' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          "E":[
            ["[User excluded a site] on distinct jobSet - With exclude / Without exclude - %s",
             "select count(distinct jobSet) nums from %s where category='E' and logDate > '%s'",
             "select count(distinct jobSet) nums from %s where category!='E' and logDate > '%s' and jobSet not in (select distinct jobSet from %s where category='E' and logDate > '%s')"]
          ],
          "ESite":[
            ["[User excluded a site] on jobSet - Top %d Sites - %s",
             "select site, count(distinct jobSet) nums from %s where category='E' and logDate > '%s' group by site order by nums DESC"],
            ["[User excluded a site] on distinct DnUser - Top %d Sites - %s",
             "select site, count(distinct dnUser) nums from %s where category='E' and logDate > '%s' group by site order by nums DESC"]
          ],
          "ECloud":[
            ["[User excluded a site] on jobSet - Per Cloud - %s",
             "select cloud, count(distinct jobSet) nums from %s where category='E' and logDate > '%s' group by cloud order by nums DESC"],
            ["[User excluded a site] on distinct DnUser - Per Cloud - %s",
             "select cloud, count(distinct dnUser) nums from %s where category='E' and logDate > '%s' group by cloud order by nums DESC"]
          ],
          "Country":[
            ["Jobs submitted by Country - %s",
             "select country, sum(jobCount) nums from %s where category in ('A','B','C') and logDate > '%s' group by country order by nums DESC"],
            ["jobDef submitted by Country - %s",
             "select country, sum(jobdefCount) nums from %s where category in ('A','B','C') and logDate > '%s' group by country order by nums DESC"],
            ["jobSet submitted by Country - %s",
             "select country, count(distinct jobSet) nums from %s where category in ('A','B','C') and logDate > '%s' group by country order by nums DESC"]
          ]
          }

last_updated = db.get_last_updated_time()
query_from = ""
# get cloud name
fjson = open('panda_queues.json','r')
data = fjson.read()
dic = json.loads(data)
fjson.close()

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


def get_cloud_name(site):
    global dic_dic_merged
    cloud = site
    
    try: 
        cloud=dic_dic_merged[site]['cloud']
        #print u'ln153', u'site', site, 'cloud', cloud
    except KeyError:
        cloud=site
    return cloud

def parse_document_category(idx1,idx2,jsonfile,field):
    global db,tabname,query_from,CHARTS,CATENAME
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    for row in rs:
        series_data = "%s %s {name:'%s', y:%d}"%(series_data,comm,CATENAME[row[0]],row[1])
        if jsonfile['data'].has_key(CATENAME[row[0]]):
            jsonfile['data'][CATENAME[row[0]]][field] = row[1]
        else:
            jsonfile['data'][CATENAME[row[0]]] = {field: row[1]}
        comm = ","
    return series_data,jsonfile

def parse_document_site(idx1,idx2,jsonfile,field,nTop=NTOP,show_others=True):
    global db,tabname,query_from,CHARTS,ADC_COLOR
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    limit = 0
    others = 0
    cloudIdx = {}
    for row in rs:
        limit += 1
        cloud = get_cloud_name(row[0])
        if limit <= nTop:
            if ADC_COLOR.has_key(cloud):
                try:
                    cloudIdx[cloud] += 4
                except KeyError:
                    cloudIdx[cloud] = 0
                cidx = cloudIdx[cloud]%30
                color = ADC_COLOR[cloud][cidx]
            else:
                color = "#55FF55"
            series_data = "%s %s {name: '%s (%s)', y: %d, color: '%s'}"%(series_data,comm,row[0],cloud,row[1],color)
            comm = ","
        else:
            others += row[1]
            
        jkey = '%s(%s)'%(row[0],cloud)
        if jsonfile['data'].has_key(jkey):
            jsonfile['data'][jkey][field] = row[1]
        else:
            jsonfile['data'][jkey] = {field: row[1]}
            
    if others > 0 and show_others:
        series_data = "%s %s {name: 'others', y: %d, color: '#CCFFCC'}"%(series_data,comm,others)
    return series_data,jsonfile

def parse_document_site_percent(idx1,idx2,jsonfile,field,pLow=PLOW,show_others=True):
    global db,tabname,query_from,CHARTS,ADC_COLOR
    comm = ""
    series_data = ""
    sqlsum = CHARTS[idx1][idx2][2]
    rs1 = db.query(sqlsum%(tabname,query_from))
    nSum = int(rs1[0][0])
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    others = 0
    percent = 0.0
    cloudIdx = {}
    for row in rs:
        cloud = get_cloud_name(row[0])
        a = int(row[1])
        if nSum > 0:
            percent = (a * 100 )/nSum
        else:
            percent = 0
        if percent >= pLow:
            if ADC_COLOR.has_key(cloud):
                try:
                    cloudIdx[cloud] += 4
                except KeyError:
                    cloudIdx[cloud] = 0
                cidx = cloudIdx[cloud]%30
                color = ADC_COLOR[cloud][cidx]
            else:
                color = "#55FF55"
            series_data = "%s %s {name: '%s (%s)', y: %d, color: '%s'}"%(series_data,comm,row[0],cloud,row[1],color)
            comm = ","
        else:
            others += row[1]
            
        jkey = '%s(%s)'%(row[0],cloud)
        if jsonfile['data'].has_key(jkey):
            jsonfile['data'][jkey][field] = row[1]
        else:
            jsonfile['data'][jkey] = {field: row[1]}
            
    if others > 0 and show_others:
        series_data = "%s %s {name: 'others', y: %d, color: '#CCFFCC'}"%(series_data,comm,others)
    return series_data,jsonfile

def parse_document_cloud(idx1,idx2,jsonfile,field):
    global db,tabname,query_from,CHARTS,ADC_COLOR
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    for row in rs:
        if ADC_COLOR.has_key(row[0]):
            color = ADC_COLOR[row[0]][0]
        else:
            color = "#CCFFCC"
        series_data = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data,comm,row[0],row[1],color)
        comm = ","
            
        if jsonfile['data'].has_key(row[0]):
            jsonfile['data'][row[0]][field] = row[1]
        else:
            jsonfile['data'][row[0]] = {field: row[1]}
            
    return series_data,jsonfile

def parse_document_excluded(idx1,idx2,jsonfile):
    global db,tabname,query_from,CHARTS
    series_data = ""
    sql1 = CHARTS[idx1][idx2][1]
    sql2 = CHARTS[idx1][idx2][2]
    rs1 = db.query(sql1%(tabname,query_from))
    rs2 = db.query(sql2%(tabname,query_from,tabname,query_from))
    excluded = rs1[0][0]
    nonexcluded = rs2[0][0]
    series_data = "{name:'With exclude', y:%s, color:'#DD0000' },{name:'Without exclude', y:%s, color: '#0000DD'}"%(excluded,nonexcluded)
            
    jsonfile['data']['With/Without'] = {'With exclude': excluded,'Without exclude': nonexcluded}
            

    return series_data,jsonfile

def parse_document_country(idx1,idx2,jsonfile,field):
    global db,tabname,query_from,CHARTS
    comm = ""
    series_data = ""
    sql = CHARTS[idx1][idx2][1]
    rs = db.query(sql%(tabname,query_from))
    cloudIdx = {}
    for row in rs:
        if COUNTRY_CLOUD.has_key(row[0]):
            cloud = COUNTRY_CLOUD[row[0]]
        else:
            cloud = 'NONE'
        if ADC_COLOR.has_key(cloud):
            try:
                cloudIdx[cloud] += 4
            except KeyError:
                cloudIdx[cloud] = 0
            cidx = cloudIdx[cloud]%30
            color = ADC_COLOR[cloud][cidx]
        else:
            color = "#CCFFCC"
        series_data = "%s %s {name:'%s (%s)', y:%d, color: '%s'}"%(series_data,comm,row[0],cloud,row[1],color)
        comm = ","
            
        if jsonfile['data'].has_key(row[0]):
            jsonfile['data'][row[0]][field] = row[1]
        else:
            jsonfile['data'][row[0]] = {field: row[1]}
            
    return series_data,jsonfile

def write_document(document, FILENAME='weeklyV2.html'):
    of = open(FILENAME, 'w')
    print >>of, document
    of.close()
    
def write_jsonfile(jsonfile, fname):
    of = open("data/%s.json"%fname, 'w')
    json_string = json.dumps(jsonfile)
    of.write(json_string)
    of.close()

def write_tablehtml(jsonfile,fname):
    global last_updated
    htmlfile = "data/%s.html"%fname
    jfile = "%s.json"%fname
    data = open('template/TABLE_brokerageV2.html').read()
    data = data.replace('#LAST_UPDATED#',last_updated)
    data = data.replace('#JSONFILE#',jfile)
    data = data.replace('#TITLE#',fname)
    
    addcolumns = ""
    setcells = ""
    
    columns = len(jsonfile['columns'])
    for i in range(0,columns):
        fld = 'field%d'%i
        addcolumns = "%s data.addColumn('%s','%s');\n"%(addcolumns,jsonfile['columns'][fld]['type'],jsonfile['columns'][fld]['name'])
    rows = len(jsonfile['data'])
    setcells = "data.addRows(%d)\n"%rows
    i = 0
    for k,v in jsonfile['data'].items():
        setcells = "%s data.setCell(%d,0,'%s');\n"%(setcells,i,k)
        for j in range(1,columns):
            fld = 'field%d'%j
            col = jsonfile['columns'][fld]['name']
            setcells = "%s data.setCell(%d,%d,%s);\n"%(setcells,i,j,v[col])
        i += 1
    
    data = data.replace('#ADDCOLUMNS#',addcolumns)
    data = data.replace('#SETCELLS#',setcells)

    write_document(data,htmlfile)
    

def run(fidx):
    global last_updated,CHARTS,DATEFORMAT,interval_days,query_from,pnames,fnames,NTOP
    query_from = time.strftime(DATEFORMAT,time.localtime(time.time()-interval_days[fidx]*24*60*60))
    data = open('template/CHART_brokerageV2.html').read()
    data = data.replace('#LAST_UPDATED#',last_updated)

    data = data.replace('#TITLE_TEXT00#',CHARTS["ABC"][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT01#',CHARTS["ABC"][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT02#',CHARTS["ABC"][2][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF0#',"data/All_Actions_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT0#',"[Detail Table]")
    
    data = data.replace('#TITLE_TEXT10#',CHARTS["ASite"][0][0]%(PLOW,pnames[fidx]))
    data = data.replace('#TITLE_TEXT11#',CHARTS["ASite"][1][0]%(PLOW,pnames[fidx]))
    data = data.replace('#TITLE_TEXT12#',CHARTS["ASite"][2][0]%(PLOW,pnames[fidx]))
    data = data.replace('#CREDITS_HREF1#',"data/User_Selected_a_Site_on_Site_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT1#',"[Detail Table of 'User selected a site' on sites]")

    data = data.replace('#TITLE_TEXT20#',CHARTS["ACloud"][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT21#',CHARTS["ACloud"][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT22#',CHARTS["ACloud"][2][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF2#',"data/User_Selected_a_Site_on_Cloud_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT2#',"[Detail Table of 'User selected a site' on clouds]")
    
    data = data.replace('#TITLE_TEXT30#',CHARTS["BSite"][0][0]%(NTOP,pnames[fidx]))
    data = data.replace('#TITLE_TEXT31#',CHARTS["BSite"][1][0]%(NTOP,pnames[fidx]))
    data = data.replace('#TITLE_TEXT32#',CHARTS["BSite"][2][0]%(NTOP,pnames[fidx]))
    data = data.replace('#CREDITS_HREF3#',"data/User_Selected_a_Cloud_on_Site_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT3#',"[Detail Table of 'User selected a cloud' on sites]")

    data = data.replace('#TITLE_TEXT40#',CHARTS["BCloud"][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT41#',CHARTS["BCloud"][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT42#',CHARTS["BCloud"][2][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF4#',"data/User_Selected_a_Cloud_on_Cloud_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT4#',"[Detail Table of 'User selected a cloud' on clouds]")
    
    data = data.replace('#TITLE_TEXT50#',CHARTS["CSite"][0][0]%(NTOP,pnames[fidx]))
    data = data.replace('#TITLE_TEXT51#',CHARTS["CSite"][1][0]%(NTOP,pnames[fidx]))
    data = data.replace('#CREDITS_HREF5#',"data/Panda_Brokerage_Decision_on_Site_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT5#',"[Detail Table of 'Panda Brokerage decision' on sites]")

    data = data.replace('#TITLE_TEXT60#',CHARTS["CCloud"][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT61#',CHARTS["CCloud"][1][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF6#',"data/Panda_Brokerage_Decision_on_Cloud_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT6#',"[Detail Table of 'Panda Brokerage decision' on clouds]")
    
    data = data.replace('#TITLE_TEXT70#',CHARTS["E"][0][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF7#',"data/User_Excluded_a_Site_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT7#',"[Detail Table of 'User excluded a site']")
    
    data = data.replace('#TITLE_TEXT80#',CHARTS["ESite"][0][0]%(NTOP,pnames[fidx]))
    data = data.replace('#TITLE_TEXT81#',CHARTS["ESite"][1][0]%(NTOP,pnames[fidx]))
    data = data.replace('#CREDITS_HREF8#',"data/User_Excluded_a_Site_on_Site_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT8#',"[Detail Table of 'User excluded a site' on sites]")
    
    data = data.replace('#TITLE_TEXT90#',CHARTS["ECloud"][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT91#',CHARTS["ECloud"][1][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF9#',"data/User_Excluded_a_Site_on_Cloud_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT9#',"[Detail Table of 'User excluded a site' on clouds]")

    data = data.replace('#TITLE_TEXT100#',CHARTS["Country"][0][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT101#',CHARTS["Country"][1][0]%pnames[fidx])
    data = data.replace('#TITLE_TEXT102#',CHARTS["Country"][2][0]%pnames[fidx])
    data = data.replace('#CREDITS_HREF10#',"data/Country_%s.html"%pnames[fidx])
    data = data.replace('#CREDITS_TEXT10#',"[Detail Table of countries]")    
    print "Replace ",fidx
    
    ABC_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Category', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'},
                            'field3':{'name':'JobSet', 'type':'number'}
                            },
                'data': {}
                }
    series_data00,ABC_json = parse_document_category("ABC",0,ABC_json,'Jobs')
    series_data01,ABC_json = parse_document_category("ABC",1,ABC_json,'JobDef')
    series_data02,ABC_json = parse_document_category("ABC",2,ABC_json,'JobSet')
    write_jsonfile(ABC_json,"All_Actions_%s"%pnames[fidx])
    write_tablehtml(ABC_json,"All_Actions_%s"%pnames[fidx])
    print "Get series ABC"
    
    ASite_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Site', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'},
                            'field3':{'name':'JobSet', 'type':'number'}
                            },
                'data': {}
                }
    series_data10,ASite_json = parse_document_site_percent("ASite",0,ASite_json,'Jobs')
    series_data11,ASite_json = parse_document_site_percent("ASite",1,ASite_json,'JobDef')
    series_data12,ASite_json = parse_document_site_percent("ASite",2,ASite_json,'JobSet')
    write_jsonfile(ASite_json,"User_Selected_a_Site_on_Site_%s"%pnames[fidx])
    write_tablehtml(ASite_json,"User_Selected_a_Site_on_Site_%s"%pnames[fidx])
    print "Get series ASite"
    
    ACloud_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Cloud', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'},
                            'field3':{'name':'JobSet', 'type':'number'}
                            },
                'data': {}
                }
    series_data20,ACloud_json = parse_document_cloud("ACloud",0,ACloud_json,'Jobs')
    series_data21,ACloud_json = parse_document_cloud("ACloud",1,ACloud_json,'JobDef')
    series_data22,ACloud_json = parse_document_cloud("ACloud",2,ACloud_json,'JobSet')
    write_jsonfile(ACloud_json,"User_Selected_a_Site_on_Cloud_%s"%pnames[fidx])
    write_tablehtml(ACloud_json,"User_Selected_a_Site_on_Cloud_%s"%pnames[fidx])
    print "Get series ACloud"
    
    BSite_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Site', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'},
                            'field3':{'name':'JobSet', 'type':'number'}
                            },
                'data': {}
                }
    series_data30,BSite_json = parse_document_site("BSite",0,BSite_json,'Jobs')
    series_data31,BSite_json = parse_document_site("BSite",1,BSite_json,'JobDef')
    series_data32,BSite_json = parse_document_site("BSite",2,BSite_json,'JobSet')
    write_jsonfile(BSite_json,"User_Selected_a_Cloud_on_Site_%s"%pnames[fidx])
    write_tablehtml(BSite_json,"User_Selected_a_Cloud_on_Site_%s"%pnames[fidx])
    print "Get series BSite"
    
    BCloud_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Cloud', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'},
                            'field3':{'name':'JobSet', 'type':'number'}
                            },
                'data': {}
                }
    series_data40,BCloud_json = parse_document_cloud("BCloud",0,BCloud_json,'Jobs')
    series_data41,BCloud_json = parse_document_cloud("BCloud",1,BCloud_json,'JobDef')
    series_data42,BCloud_json = parse_document_cloud("BCloud",2,BCloud_json,'JobSet')
    write_jsonfile(BCloud_json,"User_Selected_a_Cloud_on_Cloud_%s"%pnames[fidx])
    write_tablehtml(BCloud_json,"User_Selected_a_Cloud_on_Cloud_%s"%pnames[fidx])
    print "Get series BCloud"
    
    CSite_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Site', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'}
                            },
                'data': {}
                }
    series_data50,CSite_json = parse_document_site("CSite",0,CSite_json,'Jobs')
    series_data51,CSite_json = parse_document_site("CSite",1,CSite_json,'JobDef')
    write_jsonfile(CSite_json,"Panda_Brokerage_Decision_on_Site_%s"%pnames[fidx])
    write_tablehtml(CSite_json,"Panda_Brokerage_Decision_on_Site_%s"%pnames[fidx])
    print "Get series CSite"
    
    CCloud_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Cloud', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'}
                            },
                'data': {}
                }
    series_data60,CCloud_json = parse_document_cloud("CCloud",0,CCloud_json,'Jobs')
    series_data61,CCloud_json = parse_document_cloud("CCloud",1,CCloud_json,'JobDef')
    write_jsonfile(CCloud_json,"Panda_Brokerage_Decision_on_Cloud_%s"%pnames[fidx])
    write_tablehtml(CCloud_json,"Panda_Brokerage_Decision_on_Cloud_%s"%pnames[fidx])
    print "Get series CCloud"
    
    E_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Exclude?', 'type': 'string'},
                            'field1':{'name':'With exclude', 'type':'number'},
                            'field2':{'name':'Without exclude', 'type':'number'}
                            },
                'data': {}
                }
    series_data70,E_json = parse_document_excluded("E",0,E_json)
    write_jsonfile(E_json,"User_Excluded_a_Site_%s"%pnames[fidx])
    write_tablehtml(E_json,"User_Excluded_a_Site_%s"%pnames[fidx])
    print "Get series E"
    
    ESite_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Site', 'type': 'string'},
                            'field1':{'name':'JobSet', 'type':'number'},
                            'field2':{'name':'DnUser', 'type':'number'}
                            },
                'data': {}
                }
    series_data80,ESite_json = parse_document_site("ESite",0,ESite_json,'JobSet')
    series_data81,ESite_json = parse_document_site("ESite",1,ESite_json,'DnUser')
    write_jsonfile(ESite_json,"User_Excluded_a_Site_on_Site_%s"%pnames[fidx])
    write_tablehtml(ESite_json,"User_Excluded_a_Site_on_Site_%s"%pnames[fidx])
    print "Get series ESite"
    
    ECloud_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Cloud', 'type': 'string'},
                            'field1':{'name':'JobSet', 'type':'number'},
                            'field2':{'name':'DnUser', 'type':'number'}
                            },
                'data': {}
                }
    series_data90,ECloud_json = parse_document_cloud("ECloud",0,ECloud_json,'JobSet')
    series_data91,ECloud_json = parse_document_cloud("ECloud",1,ECloud_json,'DnUser')
    write_jsonfile(ECloud_json,"User_Excluded_a_Site_on_Cloud_%s"%pnames[fidx])
    write_tablehtml(ECloud_json,"User_Excluded_a_Site_on_Cloud_%s"%pnames[fidx])
    print "Get series ECloud"
    
    Country_json = {'lastUpdate':last_updated,
                'columns': {
                            'field0':{'name':'Country', 'type': 'string'},
                            'field1':{'name':'Jobs', 'type':'number'},
                            'field2':{'name':'JobDef', 'type':'number'},
                            'field3':{'name':'JobSet', 'type':'number'}
                            },
                'data': {}
                }
    series_data100,Country_json = parse_document_country("Country",0,Country_json,'Jobs')
    series_data101,Country_json = parse_document_country("Country",1,Country_json,'JobDef')
    series_data102,Country_json = parse_document_country("Country",2,Country_json,'JobSet')
    write_jsonfile(Country_json,"Country_%s"%pnames[fidx])
    write_tablehtml(Country_json,"Country_%s"%pnames[fidx])
    print "Get series Countries"
    
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
    
    data = data.replace('#SERIES_DATA60#',series_data60)
    data = data.replace('#SERIES_DATA61#',series_data61)
    
    data = data.replace('#SERIES_DATA70#',series_data70)
    
    data = data.replace('#SERIES_DATA80#',series_data80)
    data = data.replace('#SERIES_DATA81#',series_data81)
    
    data = data.replace('#SERIES_DATA90#',series_data90)
    data = data.replace('#SERIES_DATA91#',series_data91)

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
    print "run 0"
    run(0) # weekly
    print "run 1"
    run(1) # monthly
    print "run 2"
    run(2) # seasonly
    print "run 3"
    run(3) # yearly
    


