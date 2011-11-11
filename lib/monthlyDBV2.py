import cx_Oracle

class monthlyDBV2(object):
    
    _db = None
    _connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11'
    
    def __init__(self):       
        # self._db = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
        self._db = cx_Oracle.connect(self._connect)
        
    def get_max_id(self):
        cursor = self._db.cursor()
        sql = "SELECT MAX(monthlyLogId) as maxID from monthlyLogV2"
        cursor.execute(sql)
        maxID = cursor.fetchone()[0]
        cursor.close()
        return maxID
    
    def get_last_updated_id(self):
        cursor = self._db.cursor()
        sql = "SELECT LastUpdatedID from LastUpdatedV2"
        cursor.execute(sql)
        rs = cursor.fetchone()
        if rs is not None:
            lastUpdatedID = rs[0]
        else:
            lastUpdatedID = None;
        cursor.close()
        return lastUpdatedID
    
    def set_last_updated_id(self, lastUpdated):
        cursor = self._db.cursor()
        sql = "UPDATE LastUpdatedV2 SET lastUpdatedID='%s'"%lastUpdated
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def is_exist_item(self, logMonth, category, site, dnUser):
        cursor = self._db.cursor()
        sql = "SELECT monthlyLogId FROM monthlyLogV2 WHERE logMonth='%s' AND category='%s' AND site='%s' AND dnUser='%s'"%(logMonth,category,site,dnUser)
        cursor.execute(sql)
        rs = cursor.fetchone()
        if rs is not None:
            monthlyLogId = rs[0]
        else:
            monthlyLogId = None
        cursor.close()
        return monthlyLogId
        
    def add_log(self,monthlyLogId,logMonth,category,site,cloud,dnUser,count):
        cursor = self._db.cursor()
        sql = "INSERT INTO monthlyLogV2 ( monthlyLogId, logMonth, category, site, cloud, dnUser, jobdefCount) " + \
                  "VALUES ( %d, '%s', '%s', '%s', '%s', '%s', %d)" % (monthlyLogId,logMonth,category,site,cloud,dnUser,count)
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
        
    def increase_log_count(self,logId,byCount):
        cursor = self._db.cursor()
        sql = "UPDATE monthlyLogV2 SET jobdefCount = jobdefCount + %d WHERE monthlyLogId = %d "%(byCount,logId)
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
        
    
    def query(self,sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        cursor.close()
        return rs
