import cx_Oracle

class dailyDB(object):
    
    _db = None
    
    def __init__(self):       
        self._db = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
        
    def get_max_id(self):
        cursor = self._db.cursor()
        sql = "SELECT MAX(dailyLogId) as maxID from dailyLog"
        cursor.execute(sql)
        maxID = cursor.fetchone()[0]
        cursor.close()
        return maxID
    
    def get_last_updated_time(self):
        cursor = self._db.cursor()
        sql = "SELECT LastUpdatedTime from LastUpdated ORDER By LastUpdatedTime DESC"
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
        sql = "UPDATE LastUpdated SET LastUpdatedTime='%s'"%lastUpdated
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def first_last_updated_time(self):
        cursor = self._db.cursor()
        sql = "INSERT INTO LastUpdated (LastUpdatedTime) VALUES ('2011-10-10 12:00')"
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def is_exist_item(self, logDate, category, site, dnUser):
        cursor = self._db.cursor()
        sql = "SELECT dailyLogId FROM dailyLog WHERE logDate='%s' AND category='%s' AND site='%s' AND dnUser='%s'"%(logDate,category,site,dnUser)
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
        sql = "INSERT INTO dailyLog ( dailyLogId, logDate, category, site, cloud, dnUser, count) " + \
                  "VALUES ( :1, :2, :3, :4, :5, :6, :7)"
        cursor.executemany(sql, logs)
        self._db.commit()
        cursor.close()
        return True
        
    def increase_logs_count(self,logIds):
        cursor = self._db.cursor()
        sql = "UPDATE dailyLog SET count = count + 1 WHERE dailyLogId = :1 "
        cursor.executemany(sql, logIds)
        self._db.commit()
        cursor.close()
        return True
        
    def increase_buf_count(self,logs):
        cursor = self._db.cursor()
        sql = "UPDATE dailyLog SET count = count + 1 WHERE logDate = :1 AND category = :2 AND site = :3 AND dnUser = :4 "
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
