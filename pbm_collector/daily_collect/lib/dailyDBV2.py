#import cx_Oracle
try:
    import cx_Oracle
except:
    import MySQLdb as cx_Oracle
try:
    import MySQLdb
except:
    import cx_Oracle as MySQLdb
import ConfigParser
import re

### Production
TABLE_DAILYLOG = "dailyLogV3"
TABLE_LASTUPDATED = "LastUpdatedV2"


class dailyDBV2(object):
    
    _db = None
    _configfile = '/data/adcpbm1/lib/python2.6/site-packages/pbm_collector/settings/PandaBrokerageMonitorDB.conf'
    
    ### DB connection
    _connect = 'DBuser/DBpassword@DBhost'
    _DB_PORT = '4444'
    _DB_HOST = 'DBhost'
    _DB_USER = 'DBuser'
    _DB_PASSWORD = 'DBpassword'
    _DB_BACKEND = 'oracle'
    _DB_SCHEMA = 'ATLAS_PANDABROMON'
    
    def __init__(self):
        global TABLE_DAILYLOG, TABLE_LASTUPDATED
        self.dbConfig()
        
    def get_max_id(self):
        cursor = self._db.cursor()
        sql = "SELECT MAX(dailyLogId) as maxID from %s" % (TABLE_DAILYLOG)
        cursor.execute(sql)
        maxID = cursor.fetchone()[0]
        cursor.close()
        return maxID
    
    def dbConfig(self):
        """
        dbConfig(self)
        Configure the database. 
        Config file: self._configfile
        """
        config = ConfigParser.ConfigParser()
        config.read(self._configfile)

        self._DB_BACKEND = config.get("DB_collector", "DB_BACKEND")
        self._DB_HOST = config.get("DB_collector", "DB_HOST")
        self._DB_USER = config.get("DB_collector", "DB_USER")
        self._DB_PASSWORD = config.get("DB_collector", "DB_CRED")

        if self._DB_BACKEND == 'mysql':
            self._DB_PORT = int(config.get("DB_collector", "DB_PORT"))
            self._DB_SCHEMA = config.get("DB_collector", "DB_SCHEMA")
            self._connect = '%s/%s@%s:%s' % (self._DB_USER, self._DB_PASSWORD, \
                                             self._DB_HOST, self._DB_PORT)
            self._db = MySQLdb.connect(host=self._DB_HOST, port=self._DB_PORT, \
                                       user=self._DB_USER, \
                                       passwd=self._DB_PASSWORD, \
                                       db=self._DB_SCHEMA)
        else:
            self._connect = '%s/%s@%s' % (self._DB_USER, self._DB_PASSWORD, self._DB_HOST)
            self._db = cx_Oracle.connect(self._connect)
    

    def mysqlize_query_bindvars(self, sql, varMap):
        for k in varMap:
            k_sql = ':%s' % k
            k_mysql = '%%(%s)s' % k
            sql = re.sub(k_sql, k_mysql, sql)
        return sql


    def get_logdate_by_id(self, id):
        cursor = self._db.cursor()
        sql = "SELECT TO_CHAR(logDate, 'YYYY-MM-DD') from %s where dailyLogId=:dailyLogId" % (TABLE_DAILYLOG)
        dataQ = {'dailyLogId': id}
        if self._DB_BACKEND == 'mysql':
            sql = re.sub('TO_CHAR\(logDate, \'YYYY-MM-DD\'\)', "logDate", sql)
            sql = self.mysqlize_query_bindvars(sql, dataQ)
        cursor.execute(sql, dataQ)
        rs = cursor.fetchone()
        if rs is not None:
            logDate = rs[0]
        else:
            logDate = None;
        cursor.close()
        return logDate
    
    def get_last_updated_time(self):
        cursor = self._db.cursor()
        sql = "SELECT LastUpdatedTime from %s ORDER By LastUpdatedTime DESC" % (TABLE_LASTUPDATED)
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
        sql = "UPDATE %s SET LastUpdatedTime='%s'" % (TABLE_LASTUPDATED, lastUpdated)
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def first_last_updated_time(self):
        cursor = self._db.cursor()
        sql = "INSERT INTO %s (LastUpdatedTime) VALUES ('2011-10-10 12:00')" % (TABLE_LASTUPDATED)
        cursor.execute(sql)
        self._db.commit()
        cursor.close()
        return True
    
    def is_exist_item(self, logDate, jobSet, category, site, dnUser):
        cursor = self._db.cursor()
        dataQ = {'logDate': logDate, \
               'jobSet': jobSet, \
               'category':category, \
               'site':site,
               'dnUser':dnUser}
        sql = "SELECT dailyLogId FROM %s WHERE logDate=TO_DATE(:logDate, 'YYYY-MM-DD') AND jobSet=:jobSet AND category=:category AND site=:site AND dnUser=:dnUser" % (TABLE_DAILYLOG)
        if self._DB_BACKEND == 'mysql':
            sql = re.sub('logDate=TO_DATE\(:logDate, \'YYYY-MM-DD\'\)', "logDate=:logDate", sql)
            sql = self.mysqlize_query_bindvars(sql, dataQ)
        cursor.execute(sql, dataQ)
        rs = cursor.fetchone()
        if rs is not None:
            dailyLogId = rs[0]
        else:
            dailyLogId = None
        cursor.close()
        return dailyLogId
        
    def add_logs(self, logs):
        cursor = self._db.cursor()
        sql = "INSERT INTO %s ( dailyLogId, logDate, jobSet, category, site, cloud, dnUser, jobdefCount, jobCount, country) " % (TABLE_DAILYLOG)
        if self._DB_BACKEND != 'mysql':
            sql += "VALUES ( :1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5, :6, :7, :8, :9, :10 )"
            cursor.executemany(sql, logs)
            self._db.commit()
        else:
            sql_base = sql
            for log_tuple in logs:
                dataQ = {}
                for i in xrange(len(log_tuple)):
                    dataQ['%d' % (i + 1)] = log_tuple[i]
                sql = sql_base
                sql += "VALUES ( :1, :2, :3, :4, :5, :6, :7, :8, :9, :10 )"
                sql = self.mysqlize_query_bindvars(sql, dataQ)
                cursor.execute(sql, dataQ)
                self._db.commit()
        cursor.close()
        return True
        
    def increase_logs_count(self, logIds):
        cursor = self._db.cursor()
        sql = "UPDATE %s SET jobdefCount = jobdefCount + 1, jobCount = jobCount + :1 WHERE dailyLogId = :2 " % (TABLE_DAILYLOG)
        if self._DB_BACKEND != 'mysql':
            cursor.executemany(sql, logIds)
            self._db.commit()
        else:
            sql_base = sql
            for log_tuple in logIds:
                dataQ = {}
                for i in xrange(len(log_tuple)):
                    dataQ['%d' % (i + 1)] = log_tuple[i]
                sql = sql_base
                sql = self.mysqlize_query_bindvars(sql, dataQ)
                cursor.execute(sql, dataQ)
                self._db.commit()
        cursor.close()
        return True
        
    def increase_buf_count(self, logs):
        cursor = self._db.cursor()
        sql = "UPDATE %s SET jobdefCount = jobdefCount + 1, jobCount = jobCount + :1 WHERE logDate = TO_DATE(:2, 'YYYY-MM-DD') AND jobSet=:3 AND category = :4 AND site = :5 AND dnUser = :6 " % (TABLE_DAILYLOG)
        if self._DB_BACKEND != 'mysql':
            cursor.executemany(sql, logs)
            self._db.commit()
        else:
            sql_base = sql
            for log_tuple in logs:
                dataQ = {}
                for i in xrange(len(log_tuple)):
                    dataQ['%d' % (i + 1)] = log_tuple[i]
                sql = sql_base
                sql = self.mysqlize_query_bindvars(sql, dataQ)
                cursor.execute(sql, dataQ)
                self._db.commit()
        cursor.close()
        return True
    
    def query(self, sql, bindvarsdict):
        cursor = self._db.cursor()
        print u'DEBUG: SQL query to be executed: %s' % (sql)
        if len(bindvarsdict.keys()) > 0:
            cursor.execute(sql, bindvarsdict)
        else:
            cursor.execute(sql)
        rs = cursor.fetchall()
        cursor.close()
        return rs
