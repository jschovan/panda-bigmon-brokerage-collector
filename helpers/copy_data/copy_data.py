import cx_Oracle
import ConfigParser
from copy_data_logger import logger
import sys
import simplejson as json
from datetime import datetime
from time import mktime

### Production
#TABLE_DAILYLOG = "dailyLogV2"
TABLE_DAILYLOG = "dailyLogV3"
TABLE_LASTUPDATED = "LastUpdatedV2"

### Development/tests
#TABLE_DAILYLOG="dailyLogV2T1"
#TABLE_LASTUPDATED="lastUpdatedV2T1"


class copy_data(object):
    _TIMESTAMP = None
    _db_READER = None
    _db_WRITER = None
    #before 2012-10-13#_connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11'
    #after 2012-10-13#_connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2new@devdb11'
    _configfileDB = '/data/adcpbm1/PandaBrokerageMonitor/helpers/copy_data/copy_data_DB.conf'
    _configfile = '/data/adcpbm1/PandaBrokerageMonitor/helpers/copy_data/copy_data.conf'
    
    ### DB connection
    _connect_READER = 'DBuser/DBpassword@DBhost'
    _DB_HOST_READER = 'DBhost'
    _DB_USER_READER = 'DBuser'
    _DB_PASSWORD_READER = 'DBpassword'
    _connect_WRITER = 'DBuser/DBpassword@DBhost'
    _DB_HOST_WRITER = 'DBhost'
    _DB_USER_WRITER = 'DBuser'
    _DB_PASSWORD_WRITER = 'DBpassword'
    
    _logger = None
    _LOGGER_NAME = 'dashb_pd2p_dq2_collector'
    _LOGGER_FILE = '/data/adcpbm1/PandaBrokerageMonitor/helpers/copy_data/logs/copy_data.log'
    _LOGGER_LEVEL = 'info'
    
    _NOT_INSERTED_DATA = {}
    _NOT_INSERTED_DATA_FILE = '/data/adcpbm1/PandaBrokerageMonitor/helpers/copy_data/logs/not_inserted_data.json'
    
    def __init__(self):
        # global TABLE_DAILYLOG, TABLE_LASTUPDATED
        self._TIMESTAMP = self.unixtimestamp(datetime.utcnow())
        self._NOT_INSERTED_DATA_FILE = '/data/adcpbm1/PandaBrokerageMonitor/helpers/copy_data/logs/not_inserted_data.%s.json' % (self._TIMESTAMP)
        self.dbConfig()
        self.config_logger()
    
    def dbConfig(self):
        """
        dbConfig(self)
        Configure the database. 
        Config file: self._configfile
        """
        #self._logger.info('Inside dbConfig()')
        configDB = ConfigParser.ConfigParser()
        configDB.read(self._configfileDB)
        
        self._DB_HOST_READER = configDB.get("DB_collector_READER", "DB_HOST")
        self._DB_USER_READER = configDB.get("DB_collector_READER", "DB_USER")
        self._DB_PASSWORD_READER = configDB.get("DB_collector_READER", "DB_CRED")
        self._connect_READER = '%s/%s@%s' % (self._DB_USER_READER, self._DB_PASSWORD_READER, self._DB_HOST_READER)
        self._db_READER = cx_Oracle.connect(self._connect_READER)
        
        self._DB_HOST_WRITER = configDB.get("DB_collector_WRITER", "DB_HOST")
        self._DB_USER_WRITER = configDB.get("DB_collector_WRITER", "DB_USER")
        self._DB_PASSWORD_WRITER = configDB.get("DB_collector_WRITER", "DB_CRED")
        self._connect_WRITER = '%s/%s@%s' % (self._DB_USER_WRITER, self._DB_PASSWORD_WRITER, self._DB_HOST_WRITER)
        self._db_WRITER = cx_Oracle.connect(self._connect_WRITER)
    
    
    def config_logger(self):
        """
        config_logger
        """
        self._config = ConfigParser.ConfigParser()
        self._config.read(self._configfile)
        self._LOGGER_NAME = self._config.get("logger", "log_name")
        self._LOGGER_FILE = self._config.get("logger", "log_file")
        self._LOGGER_LEVEL = self._config.get("logger", "log_level")
        self._logger = logger(self._LOGGER_NAME, self._LOGGER_LEVEL, self._LOGGER_FILE)
        self._logger.info('Exiting loggerConfig()')
    ### END config_logger
    
    
    def copy_from_table(self, TABLE_SRC, TABLE_DST, COLUMNS_SRC, COLUMNS_DST):
        cursor_READER = self._db_READER.cursor()
        cursor_WRITER = self._db_WRITER.cursor()
        
        #self._NOT_INSERTED_DATA = {}
        
        CHUNKSIZE = 10000
        
        #DATA_TABLE = 'DAILYLOGV2'
        
        if TABLE_DST not in self._NOT_INSERTED_DATA:
            self._NOT_INSERTED_DATA[TABLE_DST] = []
        
        #columns = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
        columns = COLUMNS_SRC
        db_columns = str(columns).strip('[').strip(']').replace("'", "")
        self._logger.info('db_columns=%s' % (db_columns))
        sql = '''
            select count(*) as CNT 
            from %s
        ''' % (TABLE_SRC)
        cursor_READER.execute(sql)
        NROWS = int(cursor_READER.fetchone()[0])
        self._logger.info('maxID=%s' % (NROWS))
        
        intervals = NROWS / CHUNKSIZE
        
        for i in xrange(intervals + 1):
        #for i in xrange(5):
            imin = i * CHUNKSIZE
            imax = (i + 1) * CHUNKSIZE
            self._logger.info(u'Processing chunk %d/%d [%d; %d]' % (i, intervals, imin, imax))
            rsql = '''
                SELECT ''' + db_columns + '''
                FROM (
                    SELECT      ROWNUM r, 
                                ''' + db_columns + ''' 
                    FROM ''' + TABLE_SRC + '''
                ) 
                WHERE        r >= :imin AND r <:imax
            '''
            dataQ = {'imin':imin, 'imax':imax}
            self._logger.info('rsql=%s' % (rsql))
            self._logger.info('dataQ=%s' % (dataQ))
            cursor_READER.execute(rsql, dataQ)
            """
            data = [ {"DAILYLOGID" : x[0], "LOGDATE" : x[1], "CATEGORY" : x[2], \
                      "SITE" : x[3], "CLOUD" : x[4], "DNUSER" : x[5], "JOBDEFCOUNT" : x[6], \
                      "JOBCOUNT" : x[7], "COUNTRY" : x[8] , "JOBSET" : x[9] } for x in cursor_READER.fetchall() ]
            """
            
            data = []
            for x in cursor_READER.fetchall():
                mdict = {}
                for i in xrange(len(columns)):
                    mdict[columns[i]] = x[i]
                data.append(mdict)
            self._logger.debug('|data|=%d' % (len(data)))
           
           
            if len(data) > 0:
                db_values = str(columns).strip(']').replace("'", "").replace('[', ':').replace(', ', ', :')
                self._logger.info('db_values=%s' % (db_values))
                try:
                    wsql = '''
                            INSERT INTO ''' + TABLE_DST + ''' 
                            ( ''' + db_columns + ''' )
                             VALUES (''' + db_values + ''') 
                    '''
                    self._logger.info('wsql=%s' % (wsql))
                    #self._logger.debug('data=%s' % (data))
                    cursor_WRITER.executemany(wsql, data)
                    self._logger.info('executed many: data[0]=%s' % (data[0]))
                except:
                    self._db_WRITER.rollback()
                    LEN = len(data)
                    cnt = 0
                    for II in data:
                        self._logger.info('Processing line %d of %d' % (cnt + 1, LEN))
                        try:
                            sql = '''
                                    INSERT INTO ''' + TABLE_DST + ''' (''' + db_columns + ''')
                                   VALUES (''' + db_values + ''')
                            '''
                            cursor_WRITER.execute(sql, II)
                            self._db_WRITER.commit()
                        except cx_Oracle.IntegrityError, exc:
                            code = exc.args[0].code
                            message = exc.args[0].message
                            self._logger.warning('Encountered ORA error: %s with DATA=%s ' % ((code, message), II))
                            if TABLE_DST not in self._NOT_INSERTED_DATA:
                                self._NOT_INSERTED_DATA[TABLE_DST] = []
                            JJ = {}
                            JJ.update(II)
                            logdate = JJ['LOGDATE']
                            logdate_str = logdate.strftime('%Y-%m-%d')
                            JJ['LOGDATE'] = logdate_str
                            self._NOT_INSERTED_DATA[TABLE_DST].append(JJ)
                            self._logger.error('DOING NOTHING Encountered ORA error: %s with DATA=%s. ' % ((code, message), II))
                        self._logger.info('DONE Processing line %d of %d' % (cnt + 1, LEN))
                        cnt += 1
                        #except:
                        #    self._logger.info('PROBLEM!!!!  Data: %s' % (i))
        
        cursor_READER.close()
        
        self._db_WRITER.commit()
        cursor_WRITER.close()
        
        self.dump_json(self._NOT_INSERTED_DATA, self._NOT_INSERTED_DATA_FILE)
        
    
    def copy_from_table_change_LOGDATE_format(self, TABLE_SRC, TABLE_DST, COLUMNS_SRC, COLUMNS_DST):
        cursor_READER = self._db_READER.cursor()
        cursor_WRITER = self._db_WRITER.cursor()
        
        #self._NOT_INSERTED_DATA = {}
        
        CHUNKSIZE = 10000
        
        #DATA_TABLE = 'DAILYLOGV2'
        
        if TABLE_DST not in self._NOT_INSERTED_DATA:
            self._NOT_INSERTED_DATA[TABLE_DST] = []
        
        #columns = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
        columns = COLUMNS_SRC
        db_columns = str(columns).strip('[').strip(']').replace("'", "")
        self._logger.info('db_columns=%s' % (db_columns))
        sql = '''
            select count(*) as CNT 
            from %s
        ''' % (TABLE_SRC)
        cursor_READER.execute(sql)
        NROWS = int(cursor_READER.fetchone()[0])
        self._logger.info('maxID=%s' % (NROWS))
        
        intervals = NROWS / CHUNKSIZE
        
        for i in xrange(intervals + 1):
        #for i in xrange(5):
            imin = i * CHUNKSIZE
            imax = (i + 1) * CHUNKSIZE
            self._logger.info(u'Processing chunk %d/%d [%d; %d]' % (i, intervals, imin, imax))
            rsql = '''
                SELECT ''' + db_columns + '''
                FROM (
                    SELECT      ROWNUM r, 
                                ''' + db_columns + ''' 
                    FROM ''' + TABLE_SRC + '''
                ) 
                WHERE        r >= :imin AND r <:imax
            '''
            dataQ = {'imin':imin, 'imax':imax}
            self._logger.info('rsql=%s' % (rsql))
            self._logger.info('dataQ=%s' % (dataQ))
            cursor_READER.execute(rsql, dataQ)
            """
            data = [ {"DAILYLOGID" : x[0], "LOGDATE" : x[1], "CATEGORY" : x[2], \
                      "SITE" : x[3], "CLOUD" : x[4], "DNUSER" : x[5], "JOBDEFCOUNT" : x[6], \
                      "JOBCOUNT" : x[7], "COUNTRY" : x[8] , "JOBSET" : x[9] } for x in cursor_READER.fetchall() ]
            """
            
            data = []
            for x in cursor_READER.fetchall():
                mdict = {}
                for i in xrange(len(columns)):
                    mdict[columns[i]] = x[i]
                data.append(mdict)
            self._logger.debug('|data|=%d' % (len(data)))
           
           
            if len(data) > 0:
                db_values = str(columns).strip(']').replace("'", "").replace('[', ':').replace(', ', ', :')
                db_values = db_values.replace(":LOGDATE", "TO_DATE(:LOGDATE, 'YYYY-MM-DD')")
                self._logger.info('db_values=%s' % (db_values))
                try:
                    wsql = '''
                            INSERT INTO ''' + TABLE_DST + ''' 
                            ( ''' + db_columns + ''' )
                             VALUES (''' + db_values + ''') 
                    '''
                    self._logger.info('wsql=%s' % (wsql))
                    #self._logger.debug('data=%s' % (data))
                    cursor_WRITER.executemany(wsql, data)
                    self._logger.info('executed many: data[0]=%s' % (data[0]))
                except:
                    self._db_WRITER.rollback()
                    LEN = len(data)
                    cnt = 0
                    for II in data:
                        self._logger.info('Processing line %d of %d' % (cnt + 1, LEN))
                        try:
                            sql = '''
                                    INSERT INTO ''' + TABLE_DST + ''' (''' + db_columns + ''')
                                   VALUES (''' + db_values + ''')
                            '''
                            cursor_WRITER.execute(sql, II)
                            self._db_WRITER.commit()
                        except cx_Oracle.IntegrityError, exc:
                            code = exc.args[0].code
                            message = exc.args[0].message
                            self._logger.warning('Encountered ORA error: %s with DATA=%s ' % ((code, message), II))
                            if TABLE_DST not in self._NOT_INSERTED_DATA:
                                self._NOT_INSERTED_DATA[TABLE_DST] = []
                            JJ = {}
                            JJ.update(II)
                            logdate = JJ['LOGDATE']
                            logdate_str = logdate.strftime('%Y-%m-%d')
                            JJ['LOGDATE'] = logdate_str
                            self._NOT_INSERTED_DATA[TABLE_DST].append(JJ)
                            self._logger.error('DOING NOTHING Encountered ORA error: %s with DATA=%s. ' % ((code, message), II))
                        self._logger.info('DONE Processing line %d of %d' % (cnt + 1, LEN))
                        cnt += 1
                        #except:
                        #    self._logger.info('PROBLEM!!!!  Data: %s' % (i))
        
        cursor_READER.close()
        
        self._db_WRITER.commit()
        cursor_WRITER.close()
        
        self.dump_json(self._NOT_INSERTED_DATA, self._NOT_INSERTED_DATA_FILE)
        
    
    def insert_from_file(self, TABLE_SRC, TABLE_DST, COLUMNS_SRC, COLUMNS_DST):
        
        from data_aa import DAILYLOGV2
        #from data_ab import DAILYLOGV2
        #from data_ac import DAILYLOGV2
        #from data_ad import DAILYLOGV2
        #from data_ae import DAILYLOGV2
        #from data_af import DAILYLOGV2
        #from data_ag import DAILYLOGV2
        #from data_ah import DAILYLOGV2
        #from data_ai import DAILYLOGV2
        #from data_aj import DAILYLOGV2
        #from data_ak import DAILYLOGV2
        #from data_al import DAILYLOGV2
        #from data_am import DAILYLOGV2
        #from data_an import DAILYLOGV2
        #from data_ao import DAILYLOGV2
        #from data_ap import DAILYLOGV2
        #from data_aq import DAILYLOGV2
        #from data_ar import DAILYLOGV2
        #from data_as import DAILYLOGV2
        #from data_at import DAILYLOGV2
        #from data_au import DAILYLOGV2
        #from data_av import DAILYLOGV2
        #from data_aw import DAILYLOGV2
        #from data_ax import DAILYLOGV2
        #from data_ay import DAILYLOGV2
        #from data_az import DAILYLOGV2
        #from data_ba import DAILYLOGV2
        
        cursor_WRITER = self._db_WRITER.cursor()
        
        #self._NOT_INSERTED_DATA = {}
        
        CHUNKSIZE = 10000
        # CHUNKSIZE = 5
        
        #DATA_TABLE = 'DAILYLOGV2'
        
        if TABLE_DST not in self._NOT_INSERTED_DATA:
            self._NOT_INSERTED_DATA[TABLE_DST] = []
        
        #columns = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
        columns = COLUMNS_SRC
        db_columns = str(columns).strip('[').strip(']').replace("'", "")
        self._logger.info('db_columns=%s' % (db_columns))
        
        NROWS = len(DAILYLOGV2)
        self._logger.info('maxID=%s' % (NROWS))
        
        intervals = NROWS / CHUNKSIZE
        
        for i in xrange(intervals + 1):
        #for i in xrange(2):
            imin = i * CHUNKSIZE
            imax = min((i + 1) * CHUNKSIZE  , NROWS)
            self._logger.info(u'Processing chunk %d/%d [%d; %d]' % (i, intervals, imin, imax))
            
            data = []
            for x in DAILYLOGV2[imin:imax]:
                mdict = {}
                for i in xrange(len(columns)):
                    mdict[columns[i]] = x[i]
                data.append(mdict)
            self._logger.debug('|data|=%d' % (len(data)))
           
           
            if len(data) > 0:
                db_values = str(columns).strip(']').replace("'", "").replace('[', ':').replace(', ', ', :')
                db_values = db_values.replace(":LOGDATE", "TO_DATE(:LOGDATE, 'YYYY-MM-DD')")
                self._logger.info('db_values=%s' % (db_values))
                try:
                    wsql = '''
                            INSERT INTO ''' + TABLE_DST + ''' 
                            ( ''' + db_columns + ''' )
                             VALUES (''' + db_values + ''') 
                    '''
                    self._logger.info('wsql=%s' % (wsql))
                    #self._logger.debug('data=%s' % (data))
                    cursor_WRITER.executemany(wsql, data)
                    self._logger.info('executed many: data[0]=%s' % (data[0]))
                except:
                    self._db_WRITER.rollback()
                    LEN = len(data)
                    cnt = 0
                    for II in data:
                        self._logger.info('Processing line %d of %d' % (cnt + 1, LEN))
                        try:
                            sql = '''
                                    INSERT INTO ''' + TABLE_DST + ''' (''' + db_columns + ''')
                                   VALUES (''' + db_values + ''')
                            '''
                            cursor_WRITER.execute(sql, II)
                            self._db_WRITER.commit()
                        except cx_Oracle.IntegrityError, exc:
                            code = exc.args[0].code
                            message = exc.args[0].message
                            self._logger.warning('Encountered ORA error: %s with DATA=%s ' % ((code, message), II))
                            if TABLE_DST not in self._NOT_INSERTED_DATA:
                                self._NOT_INSERTED_DATA[TABLE_DST] = []
                            JJ = {}
                            JJ.update(II)
                            logdate = JJ['LOGDATE']
                            logdate_str = logdate.strftime('%Y-%m-%d')
                            JJ['LOGDATE'] = logdate_str
                            self._NOT_INSERTED_DATA[TABLE_DST].append(JJ)
                            self._logger.error('DOING NOTHING Encountered ORA error: %s with DATA=%s. ' % ((code, message), II))
                        self._logger.info('DONE Processing line %d of %d' % (cnt + 1, LEN))
                        cnt += 1
                        #except:
                        #    self._logger.info('PROBLEM!!!!  Data: %s' % (i))
        
        self._db_WRITER.commit()
        cursor_WRITER.close()
        
        self.dump_json(self._NOT_INSERTED_DATA, self._NOT_INSERTED_DATA_FILE)
        
    
    
    def dump_json(self, data, filename):
        jsonstr = json.dumps(data, sort_keys=True, indent=2)
        f = open(filename, 'w')
        f.write(jsonstr)
        f.close()
    
    def unixtimestamp(self, dt):
        return int(mktime(dt.timetuple()))
    
def main():
    cp = copy_data()
    # COLUMNS_SRC = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
    # cp.copy_from_table('DAILYLOGV2', 'DAILYLOGV2', COLUMNS_SRC, COLUMNS_SRC)
    # cp.copy_from_table('DAILYLOGV3', 'DAILYLOGV3_jsdev11', COLUMNS_SRC, COLUMNS_SRC)
    #
    COLUMNS_SRC = [ "LASTUPDATEDTIME", "LASTUPDATEDID" ]
    # cp.copy_from_table('LASTUPDATEDV2', 'LASTUPDATEDV2', COLUMNS_SRC, COLUMNS_SRC)
    cp.copy_from_table('LASTUPDATEDV2T1', 'LASTUPDATEDV2T1', COLUMNS_SRC, COLUMNS_SRC)
    
    #COLUMNS_SRC = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
    ##cp.insert_from_file('', 'DAILYLOGV2_ookeydata', COLUMNS_SRC, COLUMNS_SRC)
    #cp.insert_from_file('', 'DAILYLOGV3', COLUMNS_SRC, COLUMNS_SRC)
    
    # COLUMNS_SRC = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
    # cp.copy_from_table_change_LOGDATE_format('DAILYLOGV2', 'DAILYLOGV3', COLUMNS_SRC, COLUMNS_SRC)
    
    #COLUMNS_SRC = [ "DAILYLOGID", "LOGDATE", "CATEGORY", "SITE", "CLOUD", "DNUSER", "JOBDEFCOUNT", "JOBCOUNT", "COUNTRY" , "JOBSET" ]
    #cp.copy_from_table('DAILYLOGV3_JSDEV11', 'DAILYLOGV3', COLUMNS_SRC, COLUMNS_SRC)

if __name__ == '__main__':
    main()


