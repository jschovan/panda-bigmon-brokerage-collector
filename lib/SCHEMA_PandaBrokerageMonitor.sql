/*
SQL> SELECT * FROM cat;

TABLE_NAME                     TABLE_TYPE
------------------------------ -----------
DAILYLOGV2                     TABLE
DAILYLOGV2T1                   TABLE
LASTUPDATEDV2                  TABLE
LASTUPDATEDV2T1                TABLE
SEQUENCE_DAILY                 SEQUENCE
SEQUENCE_JOBSCOUNT             SEQUENCE

6 rows selected.



SQL> describe DAILYLOGV2;
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 DAILYLOGID                                NOT NULL NUMBER
 LOGDATE                                   NOT NULL VARCHAR2(10)
 CATEGORY                                  NOT NULL VARCHAR2(1)
 SITE                                               VARCHAR2(100)
 CLOUD                                              VARCHAR2(100)
 DNUSER                                             VARCHAR2(100)
 JOBDEFCOUNT                                        NUMBER
 JOBCOUNT                                           NUMBER(38)
 COUNTRY                                            VARCHAR2(100)
 JOBSET                                             VARCHAR2(100)



SQL> describe DAILYLOGV2T1;
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 DAILYLOGID                                NOT NULL NUMBER
 LOGDATE                                   NOT NULL VARCHAR2(10)
 CATEGORY                                  NOT NULL VARCHAR2(1)
 SITE                                               VARCHAR2(100)
 CLOUD                                              VARCHAR2(100)
 DNUSER                                             VARCHAR2(100)
 JOBDEFCOUNT                                        NUMBER
 JOBCOUNT                                           NUMBER(38)
 COUNTRY                                            VARCHAR2(100)
 JOBSET                                             VARCHAR2(100)

SQL> describe LASTUPDATEDV2;
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 LASTUPDATEDTIME                                    VARCHAR2(20)
 LASTUPDATEDID                                      NUMBER(14)

SQL> describe LASTUPDATEDV2T1;
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 LASTUPDATEDTIME                                    VARCHAR2(20)
 LASTUPDATEDID                                      NUMBER(14)


*/


CREATE TABLE DAILYLOGV2  (
    "DAILYLOGID"   NUMBER            NOT NULL ENABLE,
    "LOGDATE"      VARCHAR2(10)      NOT NULL ENABLE,
    "CATEGORY"     VARCHAR2(1)       NOT NULL ENABLE,
    "SITE"         VARCHAR2(100),
    "CLOUD"        VARCHAR2(100),
    "DNUSER"       VARCHAR2(100),
    "JOBDEFCOUNT"  NUMBER,
    "JOBCOUNT"     NUMBER(38),
    "COUNTRY"      VARCHAR2(100),
    "JOBSET"       VARCHAR2(100)
);


CREATE TABLE LASTUPDATEDV2  (
    "LASTUPDATEDTIME"   VARCHAR2(20),
    "LASTUPDATEDID"     NUMBER(14)
);


CREATE TABLE LASTUPDATEDV2T1  (
    "LASTUPDATEDTIME"   VARCHAR2(20),
    "LASTUPDATEDID"     NUMBER(14)
);





-- update DAILYLOGV2 set DAILYLOGID = DAILYLOGID + 13156751;


--- 2012-12-17 adding indexes
CREATE TABLE DAILYLOGV3  (
    "DAILYLOGID"   NUMBER            NOT NULL ENABLE,
--     "LOGDATE"      VARCHAR2(10)      NOT NULL ENABLE,
    "LOGDATE" DATE DEFAULT TO_DATE('1970-01-01', 'yyyy-mm-dd') NOT NULL ENABLE,
    "CATEGORY"     VARCHAR2(1)       NOT NULL ENABLE,
    "SITE"         VARCHAR2(100),
    "CLOUD"        VARCHAR2(100),
    "DNUSER"       VARCHAR2(100),
    "JOBDEFCOUNT"  NUMBER,
    "JOBCOUNT"     NUMBER(38),
    "COUNTRY"      VARCHAR2(100),
    "JOBSET"       VARCHAR2(100),
CONSTRAINT "DAILYLOGV3_UC" UNIQUE ("DAILYLOGID", "LOGDATE", "JOBSET", "DNUSER")
    )    
    partition by range( "LOGDATE" ) INTERVAL (NUMTODSINTERVAL(1, 'DAY'))
    (
      PARTITION part_01 values LESS THAN (to_date('2011-06-01', 'yyyy-mm-dd'))
      );

CREATE INDEX "DL3_LD_JS_CAT_SIT_DNU" ON DAILYLOGV3 ("LOGDATE", "JOBSET", "CATEGORY", "SITE", "DNUSER") LOCAL;
CREATE INDEX "DL3_LD_JS_CAT_CLD_DNU" ON DAILYLOGV3 ("LOGDATE", "JOBSET", "CATEGORY", "CLOUD", "DNUSER") LOCAL;
CREATE INDEX "DL3_LD_JS_CAT_CTR_DNU" ON DAILYLOGV3 ("LOGDATE", "JOBSET", "CATEGORY", "COUNTRY", "DNUSER") LOCAL;
CREATE INDEX "DL3_DLID" ON DAILYLOGV3 ("DAILYLOGID") LOCAL;
CREATE INDEX "DL3_LD" ON DAILYLOGV3 ("LOGDATE") LOCAL;
CREATE INDEX "DL3_CAT" ON DAILYLOGV3 ("CATEGORY") LOCAL;
CREATE INDEX "DL3_CLD" ON DAILYLOGV3 ("CLOUD") LOCAL;
CREATE INDEX "DL3_SIT" ON DAILYLOGV3 ("SITE") LOCAL;
CREATE INDEX "DL3_CTR" ON DAILYLOGV3 ("COUNTRY") LOCAL;
CREATE INDEX "DL3_DNU" ON DAILYLOGV3 ("DNUSER") LOCAL;


-- AS OWNER: ATLAS_PANDABROMON
grant select, insert, update, delete on DAILYLOGV3 to ATLAS_PANDABROMON_W;
grant select on DAILYLOGV3 to ATLAS_PANDABROMON_R;
grant select, insert, update, delete on LASTUPDATEDV2 to ATLAS_PANDABROMON_W;
grant select on LASTUPDATEDV2 to ATLAS_PANDABROMON_R;

-- AS WRITER: ATLAS_PANDABROMON_W
CREATE SYNONYM DAILYLOGV3 FOR ATLAS_PANDABROMON.DAILYLOGV3;
CREATE SYNONYM LASTUPDATEDV2 FOR ATLAS_PANDABROMON.LASTUPDATEDV2;

-- AS READER: ATLAS_PANDABROMON_R
CREATE SYNONYM DAILYLOGV3 FOR ATLAS_PANDABROMON.DAILYLOGV3;
CREATE SYNONYM LASTUPDATEDV2 FOR ATLAS_PANDABROMON.LASTUPDATEDV2;


