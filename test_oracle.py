import cx_Oracle
con = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
cursor = con.cursor()
cursor.execute("select * from dailyLog")
rows = cursor.fetchall()
print len(rows)
for row in rows:
   print row[1], row[6]
cursor.close()
con.close()
