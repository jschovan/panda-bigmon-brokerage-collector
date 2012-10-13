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


