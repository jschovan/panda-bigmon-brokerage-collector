# -*- coding: utf-8 -*-

### get it from: http://www.crummy.com/software/BeautifulSoup/
import re
import sys
import os
import pycurl
import time
import datetime
import simplejson as json

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
          ["P1_Logfile","Category A,B,C Analy - Logfile"],
          ["P2_Logfile","Top 10 sites of Category A - Logfile"],
          ["P3_Logfile","Cloud Analy of Category B - Logfile"],
          ["P4_Logfile","Top 20 sites of Category C - Logfile"],
          ["P5_Logfile","Cloud Analy of Category C - Logfile"],
          ["P6_Logfile","Top 20 sites of Category E - Logfile"],
          ["P7_Logfile","Cloud Analy of Category E - Logfile"]
          ]

# get cloud name
fjson = open('panda_queues.json','r')
data = fjson.read()
dic = json.loads(data)
fjson.close()

def get_document(logfile):
    fjson = open(logfile,'r')
    data = fjson.read()
    contents = json.loads(data)
    fjson.close()
    
    return contents

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

def get_cloud_name(site):
    global dic_dic_merged
    cloud = site
    
    try: 
        cloud=dic_dic_merged[site]['cloud']
        #print u'ln153', u'site', site, 'cloud', cloud
    except KeyError:
        cloud=site
    return cloud

def get_sitecloud_name(dic, siteID):
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

def is_in_buf(records, logDate, category, site, dnUser):
    found = False
    idx = 0
    for record in records:
        if record[1]==logDate and record[2]==category and record[3]==site and record[5]==dnUser:
            found = True
            break
        idx += 1
    if not found:
        return None
    else:
        return idx

def parse_document(document):
    P_category = {'A':0,'B':0,'C':0,'E':0}
    P_site = {'A':{},'B':{},'C':{},'E':{}}
    P_cloud = {'A':{},'B':{},'C':{},'E':{}}
    
    processed_rows = 0
    from_date = None
    to_date = None
    
    for row in document:
        cell_message = document[row]['message']
        if from_date is None:
            from_date = document[row]['timestamp']
        if to_date is None:
            to_date = document[row]['timestamp']
        if document[row]['timestamp']<from_date:
            from_date = document[row]['timestamp']
        if document[row]['timestamp']>to_date:
            to_date = document[row]['timestamp']
        
        message_category="no.category"
        message_dn = ""
        message_jobset ="no.jobset"
        message_jobdef = "no.jobdef"
        message_action = ""
        message_site="no.site"
        message_reason="no.reason"
        message_weight="no.weight"
                       
        # print 'Debug:',message_date,message_time,row_counter,cell_message
        processed_rows += 1
        
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

        ## skip
        if is_this_category(cell_message, ' action=skip '):
            # continue # try to speed up
            message_category = "D"
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
            message_reason = message_skip[2].split('=')[1].strip()
            if re.search('=',message_skip[4]):
                message_weight = message_skip[4].split('=')[1].strip()
            else:
                message_reason = '_'.join(message_skip[3:]).strip('_')
        
        # exclude : add at 2011-10-26
        elif is_this_category(cell_message, ' action=exclude '):
            message_category = "E"
            message_skip = tmp_message[2].split(' ')
            message_action = message_skip[0].split('=')[1].strip()
            message_site = message_skip[1].split('=')[1].strip()
            message_reason = message_skip[2].split('=')[1].strip()
            if re.search('=',message_skip[4]):
                message_weight = message_skip[4].split('=')[1].strip()
            else:
                message_reason = '_'.join(message_skip[3:]).strip('_')
        
        ## choose
        elif is_this_category(cell_message, ' action=choose '):
            message_category = "C"
            message_choose = tmp_message[2].split(' ')
            message_action = message_choose[0].split('=')[1].strip()
            message_site = message_choose[1].split('=')[1].strip()
            message_reason = message_choose[2].split('=')[1].strip()
            if re.search('=',message_choose[5]):
                message_weight = message_choose[5].split('=')[1].strip()
            else:
                message_reason = '_'.join(message_choose[3:]).strip('_')
        
        ## action=use: add at 2011-10-26
        elif is_this_category(cell_message, ' action=use '):
            #message_category = "C"
            message_choose = tmp_message[2].split(' ')
            message_action = message_choose[0].split('=')[1].strip()
            message_site = message_choose[1].split('=')[1].strip()
            # message_reason = message_choose[2].split('=')[1].strip()
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
        
        ## append to records it belong to
        if message_category in ['A','B','C','E']:
            site_name,cloud = get_sitecloud_name(dic,message_site)
            P_category[message_category] += 1
            if site_name not in P_site[message_category]:
                P_site[message_category][site_name] = 1
            else:
                P_site[message_category][site_name] += 1
            if cloud not in P_cloud[message_category]:
                P_cloud[message_category][cloud] = 1
            else:
                P_cloud[message_category][cloud] += 1
                
        # print "INFOR: category=%s user=%s action=%s site=%s jobset=%s jobdef=%s reason=%s"%(message_category,message_dn,message_action,message_site,message_jobset,message_jobdef,message_reason)
        
    return (processed_rows, from_date, to_date, P_category, P_site, P_cloud)

def sort_by_value(dic):
    lists = dic.items()
    backitems = [[v[1],v[0]] for v in lists]
    backitems.sort(reverse=True)
    return [ backitems[i][1] for i in range(0,len(backitems))]

def write_document(from_date, to_date, P_category,P_site,P_cloud,doc_file="logfile.html"):
    data = open('template/CHART_logfile.html').read()
    data = data.replace('#FROM_DATE#',from_date)
    data = data.replace('#TO_DATE#',to_date)
    data = data.replace('#TITLE_TEXT1#',CHARTS[0][1])
    data = data.replace('#TITLE_TEXT2#',CHARTS[1][1])
    data = data.replace('#TITLE_TEXT3#',CHARTS[2][1])
    data = data.replace('#TITLE_TEXT4#',CHARTS[3][1])
    data = data.replace('#TITLE_TEXT5#',CHARTS[4][1])
    data = data.replace('#TITLE_TEXT6#',CHARTS[5][1])
    data = data.replace('#TITLE_TEXT7#',CHARTS[6][1])
    
    comm = ""
    series_data1 = ""
    for c in P_category:
        series_data1 = "%s %s ['%s', %d]"%(series_data1,comm,c,P_category[c])
        comm = ","
    data = data.replace('#SERIES_DATA1#',series_data1)
    
    comm = ""
    series_data2 = ""
    sorted = sort_by_value(P_site['A'])
    cnt = 0
    for k in sorted:
        cloud = get_cloud_name(k)
        color = ADC_COLOR[cloud]
        series_data2 = "%s %s {name: '%s (%s)', y: %d, color: '%s'}"%(series_data2,comm,k,cloud,P_site['A'][k],color)
        comm = ","
        cnt += 1
        if cnt>= 10:
            break
    data = data.replace('#SERIES_DATA2#',series_data2)
    
    comm = ""
    series_data3 = ""
    sorted = sort_by_value(P_cloud['B'])
    for k in sorted:
        color = ADC_COLOR[k]
        series_data3 = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data3,comm,k,P_cloud['B'][k],color)
        comm = ","
    data = data.replace('#SERIES_DATA3#',series_data3)
    
    comm = ""
    series_data4 = ""
    sorted = sort_by_value(P_site['C'])
    cnt = 0
    for k in sorted:
        cloud = get_cloud_name(k)
        color = ADC_COLOR[cloud]
        series_data4 = "%s %s {name: '%s (%s)', y: %d, color: '%s'}"%(series_data4,comm,k,cloud,P_site['C'][k],color)
        comm = ","
        cnt += 1
        if cnt>=20:
            break
    data = data.replace('#SERIES_DATA4#',series_data4)
    
    comm = ""
    series_data5 = ""
    sorted = sort_by_value(P_cloud['C'])
    for k in sorted:
        color = ADC_COLOR[k]
        series_data5 = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data5,comm,k,P_cloud['C'][k],color)
        comm = ","
    data = data.replace('#SERIES_DATA5#',series_data5)
    
    comm = ""
    series_data6 = ""
    sorted = sort_by_value(P_site['E'])
    cnt = 0
    for k in sorted:
        cloud = get_cloud_name(k)
        color = ADC_COLOR[cloud]
        series_data6 = "%s %s {name: '%s (%s)', y: %d, color: '%s'}"%(series_data6,comm,k,cloud,P_site['E'][k],color)
        comm = ","
        cnt += 1
        if cnt>=20:
            break
    data = data.replace('#SERIES_DATA6#',series_data6)
    
    comm = ""
    series_data7 = ""
    sorted = sort_by_value(P_cloud['E'])
    for k in sorted:
        color = ADC_COLOR[k]
        series_data7 = "%s %s {name: '%s', y: %d, color: '%s'}"%(series_data7,comm,k,P_cloud['E'][k],color)
        comm = ","
    data = data.replace('#SERIES_DATA7#',series_data7)
    
    of = open(doc_file, 'w')
    print >>of, data
    of.close()
    return True

def run(logfile):
    #t1 = time.time()
    document = get_document(logfile)
    t2 = time.time()
    processed_rows,from_date,to_date,P_category,P_site,P_cloud = parse_document(document)
    t3 = time.time()
    
    #time_get = t2-t1
    time_parse = t3-t2
    
    write_document(from_date,to_date,P_category,P_site,P_cloud)
    
    #time_db = t4-t3
    print u'INFOR: Rows: %d Done(A/B/C/E: %d/%d/%d/%d). ParsingTime: %d'%(processed_rows,P_category['A'],P_category['B'],P_category['C'],P_category['E'],time_parse)
    


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print "ERROR: too few input parameters"
        print "USAGE: python   parse_logfile.py   <input logfile>"
        sys.exit(1) # before Python 2.5, after: exit(1)
    #else:
    #    OUTPUT_FILENAME_PREFIX = sys.argv[1]

    run(sys.argv[1])
    


