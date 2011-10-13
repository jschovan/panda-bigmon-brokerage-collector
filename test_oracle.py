from dailyDB import dailyDB
import time
import cx_Oracle
import os

def multi_result():
    rec1 = []
    rec2 = []
    for i in range(1,10):
        rec1.append((i,i))
    for j in range(11,20):
        rec2.append((j,j))
    return (rec1,rec2)

def get_sitecloud_name(siteID):
    cloud = siteID
    site_name = siteID
    for site in dic:
        if site['panda_siteID']==siteID:
            cloud = site['cloud']
            site_name = site['agis_ssb_site_name']
            break
    return (site_name,cloud)

data = open('panda_queues.json').read()
dic = eval(data)
# print dic[10]['cloud'],dic[10]['panda_siteID']

con = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
print con.version
print "====="
cursor = con.cursor()
cursor1 = con.cursor()
cursor1.execute("select * from dailyLog")
"""
for result in cursor1:
    # print result
    dailyLogId = result[0]
    site_name, cloud = get_sitecloud_name(result[3])
    if cloud is not None:
        sql = "UPDATE dailyLog SET site='%s',cloud='%s' WHERE dailyLogId=%d"%(site_name,cloud,dailyLogId)
        cursor.execute(sql)
        con.commit()
"""
DATEFORMAT = "%Y-%m-%d"
t1 = time.time()
t2 = t1 - 7*24*60*60
print time.strftime(DATEFORMAT,time.localtime(t2))
print "=====" 
"""
cursor.execute("select * from dailyLog where logDate>'2011-10-06' order by dailyLogId DESC")
rows = cursor.fetchall()
print cursor.rowcount
for result in rows:
    print result
cursor.execute("select MAX(dailyLogId) as MaxId from dailyLog")
maxId = cursor.fetchone()[0]
print "MAXID=",maxId
cursor.close()
con.close()
"""
db = dailyDB()
maxId = db.get_max_id()
if maxId is None:
    maxId = 0


""" Test Adding
logs = []
for i in range(1,20):
    maxId = maxId+1
    logDate = str('2011-10-%02d'%i)
    logs.append((maxId,logDate,'A','TW','TW','Ookey',1))
db.add_logs(logs)
"""
"""
#logIds = [[1],[3],[5],[7],[9]]
logIds = []
for i in range(1,20,2):
    logDate = str('2011-10-%02d'%i)
    logId = db.is_exist_item(logDate,'A','TW','Ookey')
    if logId is not None:
        logIds.append([logId])
db.increase_logs_count(logIds)

print "MAXID from class=",db.get_max_id()

rec1,rec2 = multi_result()
print(rec1)[3][1]
print(rec2)[5][1]
"""
# os.system("wget http://adc-ssb.cern.ch/SITE_EXCLUSION/panda_queues.json")
cursor.close()
cursor1.close()
con.close()


