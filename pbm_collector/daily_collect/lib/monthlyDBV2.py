import cx_Oracle

### Production
TABLE_MONTHLYLOG="monthlyLogV2"
TABLE_LASTUPDATED="LastUpdatedV2"


class monthlyDBV2(object):
    
    _db = None
    #_connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11'
    _connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2new@devdb11'
    
    def __init__(self):       
        global TABLE_MONTHLYLOG, TABLE_LASTUPDATED
        # self._db = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
        self._db = cx_Oracle.connect(self._connect)
        
    def get_max_id(self):
        cursor = self._db.cursor()
        sql = "SELECT MAX(monthlyLogId) as maxID from %s" % (TABLE_MONTHLYLOG)
        cursor.execute(sql)
        maxID = cursor.fetchone()[0]
        cursor.close()
        return maxID
    
    def get_last_updated_id(self):
        cursor = self._db.cursor()
        sql = "SELECT LastUpdatedID from %s" % (TABLE_LASTUPDATED)
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
        sql = "UPDATE %s SET lastUpdatedID='%s'" % (TABLE_LASTUPDATED, lastUpdated)
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def is_exist_item(self, logMonth, category, site, dnUser):
        cursor = self._db.cursor()
        sql = "SELECT monthlyLogId FROM %s WHERE logMonth='%s' AND category='%s' AND site='%s' AND dnUser='%s'" % (TABLE_MONTHLYLOG, logMonth,category,site,dnUser)
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
        sql = "INSERT INTO %s ( monthlyLogId, logMonth, category, site, cloud, dnUser, jobdefCount) " + \
                  "VALUES ( %d, '%s', '%s', '%s', '%s', '%s', %d)" % (TABLE_MONTHLYLOG, monthlyLogId,logMonth,category,site,cloud,dnUser,count)
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
        
    def increase_log_count(self,logId,byCount):
        cursor = self._db.cursor()
        sql = "UPDATE %s SET jobdefCount = jobdefCount + %d WHERE monthlyLogId = %d "%(TABLE_MONTHLYLOG, byCount,logId)
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
