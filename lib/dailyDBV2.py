import cx_Oracle

class dailyDBV2(object):
    
    _db = None
    _connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11'
    
    def __init__(self):       
        # self._db = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
        self._db = cx_Oracle.connect(self._connect)
        
    def get_max_id(self):
        cursor = self._db.cursor()
        sql = "SELECT MAX(dailyLogId) as maxID from dailyLogV2"
        cursor.execute(sql)
        maxID = cursor.fetchone()[0]
        cursor.close()
        return maxID
    
    def get_logdate_by_id(self, id):
        cursor = self._db.cursor()
        sql = "SELECT logDate from dailyLogV2 where dailyLogId=%d"%id
        cursor.execute(sql)
        rs = cursor.fetchone()
        if rs is not None:
            logDate = rs[0]
        else:
            logDate = None;
        cursor.close()
        return logDate
    
    def get_last_updated_time(self):
        cursor = self._db.cursor()
        sql = "SELECT LastUpdatedTime from LastUpdatedV2 ORDER By LastUpdatedTime DESC"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if rs is not None:
            lastUpdatedTime = rs[0]
        else:
            lastUpdatedTime = None;
        cursor.close()
        return lastUpdatedTime
    
    def set_last_updated_time(self, lastUpdated):
        cursor = self._db.cursor()
        sql = "UPDATE LastUpdatedV2 SET LastUpdatedTime='%s'"%lastUpdated
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def first_last_updated_time(self):
        cursor = self._db.cursor()
        sql = "INSERT INTO LastUpdatedV2 (LastUpdatedTime) VALUES ('2011-10-10 12:00')"
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def is_exist_item(self, logDate, jobSet, category, site, dnUser):
        cursor = self._db.cursor()
        sql = "SELECT dailyLogId FROM dailyLogV2 WHERE logDate='%s' AND jobSet='%s' AND category='%s' AND site='%s' AND dnUser='%s'"%(logDate,jobSet,category,site,dnUser)
        cursor.execute(sql)
        rs = cursor.fetchone()
        if rs is not None:
            dailyLogId = rs[0]
        else:
            dailyLogId = None
        cursor.close()
        return dailyLogId
        
    def add_logs(self,logs):
        cursor = self._db.cursor()
        sql = "INSERT INTO dailyLogV2 ( dailyLogId, logDate, jobSet, category, site, cloud, dnUser, jobdefCount, jobCount, country) " + \
                  "VALUES ( :1, :2, :3, :4, :5, :6, :7, :8, :9, :10 )"
        cursor.executemany(sql, logs)
        self._db.commit()
        cursor.close()
        return True
        
    def increase_logs_count(self,logIds):
        cursor = self._db.cursor()
        sql = "UPDATE dailyLogV2 SET jobdefCount = jobdefCount + 1, jobCount = jobCount + :1 WHERE dailyLogId = :2 "
        cursor.executemany(sql, logIds)
        self._db.commit()
        cursor.close()
        return True
        
    def increase_buf_count(self,logs):
        cursor = self._db.cursor()
        sql = "UPDATE dailyLogV2 SET jobdefCount = jobdefCount + 1, jobCount = jobCount + :1 WHERE logDate = :2 AND jobSet=:3 AND category = :4 AND site = :5 AND dnUser = :6 "
        cursor.executemany(sql, logs)
        self._db.commit()
        cursor.close()
        return True
    
    def query(self,sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        cursor.close()
        return rs
