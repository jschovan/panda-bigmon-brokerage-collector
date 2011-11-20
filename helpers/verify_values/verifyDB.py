import cx_Oracle, sys
from datetime import datetime

## adcmon
#WORKDIR='/data/jschovan/PandaBrokerageMon/verify_values'
## lxplus
WORKDIR='/afs/cern.ch/user/j/jschovan/scratch0/trunk/helpers/verify_values'

class dailyDB(object):
    
    _db = None
    _connect = 'PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11'
    
    def __init__(self):       
        # self._db = cx_Oracle.connect('PandaBrokerageMonitor_ookey/PandaBrokerageMonitor2@devdb11')
        self._db = cx_Oracle.connect(self._connect)
        
    def print_tables(self):
        global WORKDIR
        # dailyLogV2
        cursor = self._db.cursor()

        """
        #sql = "SELECT owner, table_name FROM all_tables"

        sql = "SELECT table_name FROM user_tables"

        #sql = "SELECT table_name FROM user_tables"
        #sql = "SELECT * FROM LastUpdated"
        #sql = "SELECT * FROM dailyLog LIMIT 10"
        cursor.execute(sql)
        res = cursor.fetchall()
        """

        """
        for tt in res[:1]:
            t=tt[0]
            print t
            sql="DESCRIBE %s" % ( t )
            #sql="DESCRIBE dailyLogV2"
            print sql
            cursor.execute(sql)
            r=cursor.fetchall()
            print t, r

        """
        """
        sql="SELECT COUNT(*) FROM dailyLogV2"
        cursor.execute(sql)
        res = cursor.fetchall()
        print u'CMD:', sql, u'\nRESULT:', res
        """
        """	
        sql="SELECT * FROM dailyLogV2 where ROWNUM<10"
        cursor.execute(sql)
        res = cursor.fetchall()
        print u'cursor.description', cursor.description
        print u'CMD:', sql, u'\nRESULT:', res
        """

        sql = "SELECT table_name FROM user_tables"
        cursor.execute(sql)
        tables_tmp= cursor.fetchall()
        tables=[x[0] for x in tables_tmp ]


        for t in tables:
            f='%s/%s.py' % (WORKDIR, t)
            print u'dump', t, f; sys.stdout.flush()
            fo=open(f,'w')
            sql="SELECT * FROM %s -- where ROWNUM<10" % t
            cursor.execute(sql)
            tab_res = cursor.fetchall()
            cur_desc=cursor.description
            
            fo.write("# CMD: \"%s\"\n#     RESULT LENGTH %d\n#     EXECUTED at %s\n" % (sql, len(tab_res), datetime.utcnow()))
            fo.write("# COLUMNS: %s\n" % cur_desc)
            fo.write("%s = %s\n" % (t, tab_res))
            fo.close()

        res=tab_res



        cursor.close()
        return res
        
    def query(self,sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        cursor.close()
        return rs


def run():
    db=dailyDB()
    
    print u'### db.print_tables()'
    print db.print_tables()
    
    print u'EOF'




def main():
    global WORKDIR
    args = sys.argv[1:]
    if len(args) < 1:
        print 'usage: verify_values.py WORKDIR'
        sys.exit(-1)
    
    WORKDIR=args[0]
    
    run()
    
    print;print;print


if __name__ == '__main__':
    main()


