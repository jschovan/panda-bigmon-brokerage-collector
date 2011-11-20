import sys
from datetime import datetime
from operator import itemgetter, attrgetter

from DAILYLOGV2 import DAILYLOGV2
"""
# COLUMNS: [
0 ... ('DAILYLOGID', <type 'cx_Oracle.NUMBER'>, 127, 22, 0, -127, 0), 
1 ... ('LOGDATE', <type 'cx_Oracle.STRING'>, 10, 10, 0, 0, 0), 
2 ... ('CATEGORY', <type 'cx_Oracle.STRING'>, 1, 1, 0, 0, 0), 
3 ... ('SITE', <type 'cx_Oracle.STRING'>, 100, 100, 0, 0, 1), 
4 ... ('CLOUD', <type 'cx_Oracle.STRING'>, 100, 100, 0, 0, 1), 
5 ... ('DNUSER', <type 'cx_Oracle.STRING'>, 100, 100, 0, 0, 1), 
6 ... ('JOBDEFCOUNT', <type 'cx_Oracle.NUMBER'>, 127, 22, 0, -127, 1), 
7 ... ('JOBCOUNT', <type 'cx_Oracle.NUMBER'>, 39, 22, 38, 0, 1), 
8 ... ('COUNTRY', <type 'cx_Oracle.STRING'>, 100, 100, 0, 0, 1), 
9 ... ('JOBSET', <type 'cx_Oracle.STRING'>, 100, 100, 0, 0, 1)
]

VALUES: [

(12, '2011-11-14', 'C', 'INFN-MILANO-ATLASC', 'IT', 'Keita_Hanawa', 1, 104, 'jp', '20007'),

]

"""

COLUMNID={
    'CATEGORY': 2,
    'DATE': 1,
    'JOBSETID': 9,
    'JOBDEFCOUNT': 6,
    'JOBCOUNT': 7, 
    'CLOUD': 4,
    'SITE': 3,
    'USERDN': 5,
    'COUNTRY': 8
}

LEGEND={
    'A': 'User selects SITE',
    'B': 'User selects CLOUD',
    'C': 'Panda brokerage',
    'E': 'User excludes SITE(s)'
}

#ROW_LIMIT=50000
ROW_LIMIT=-1
DATA_A=[x for x in DAILYLOGV2[:ROW_LIMIT] if x[2]=='A']
DATA_B=[x for x in DAILYLOGV2[:ROW_LIMIT] if x[2]=='B']
DATA_C=[x for x in DAILYLOGV2[:ROW_LIMIT] if x[2]=='C']
DATA_E=[x for x in DAILYLOGV2[:ROW_LIMIT] if x[2]=='E']


def get_exclusion_dates():
    global DATA_E
    
    print u'DEBUG: |DAILYLOGV2|=', len(DAILYLOGV2)
    
    exclusion_dates=list(set([x[1] for x in DATA_E   ]))
    exclusion_dates.sort()
    
    return exclusion_dates


def category_distribution_jobset():
    global DATA_A, DATA_B, DATA_C, DATA_E, \
        COLUMNID
    
    jobset_A=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_A ]))
    jobset_B=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_B ]))
    jobset_C=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_C ]))
    jobset_E=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_E ]))
    jobset_sum=len(jobset_A)+len(jobset_B)+len(jobset_C)+len(jobset_E)
    
    print u'category_distribution_jobset:'
    print u'\t A: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (len(jobset_A), 100.0*len(jobset_A)/jobset_sum)
    print u'\t B: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (len(jobset_B), 100.0*len(jobset_B)/jobset_sum)
    print u'\t C: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (len(jobset_C), 100.0*len(jobset_C)/jobset_sum)
    print u'\t E: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (len(jobset_E), 100.0*len(jobset_E)/jobset_sum)


def category_distribution_jobs():
    global DATA_A, DATA_B, DATA_C, DATA_E, \
        COLUMNID
    
    list_jobs_A=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_A ]))
    list_jobs_B=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_B ]))
    list_jobs_C=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_C ]))
    #list_jobs_E=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSET'], x[ COLUMNID['JOBDEFCOUNT'], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_E ]))
    
    jobs_A=sum(  [ x[3] for x in list_jobs_A]  )
    jobs_B=sum(  [ x[3] for x in list_jobs_B]  )
    jobs_C=sum(  [ x[3] for x in list_jobs_C]  )
    #jobs_E=sum(  [ x[3] for x in list_jobs_E]  )
    
    jobs_sum=jobs_A+jobs_B+jobs_C #+jobs_E
    
    print u'category_distribution_jobs:'
    print u'\t A: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (jobs_A, 100.0*jobs_A/jobs_sum)
    print u'\t B: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (jobs_B, 100.0*jobs_B/jobs_sum)
    print u'\t C: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (jobs_C, 100.0*jobs_C/jobs_sum)
    #print u'\t E: EVENTS: %8d\tPERCENTAGE: %4.2f%%' % (len(jobs_E), 100.0*len(jobs_E)/jobs_sum)


def avg_size_jobset_jobdef():
    global DATA_A, DATA_B, DATA_C, DATA_E, \
        COLUMNID
    
    list_jobs_A=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_A ]))
    list_jobs_B=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_B ]))
    list_jobs_C=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_C ]))
    #list_jobs_E=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSET'], x[ COLUMNID['JOBDEFCOUNT'], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_E ]))
    
    #Njobs
    jobs_A=sum(  [ x[3] for x in list_jobs_A]  )
    jobs_B=sum(  [ x[3] for x in list_jobs_B]  )
    jobs_C=sum(  [ x[3] for x in list_jobs_C]  )
    jobs_sum=jobs_A+jobs_B+jobs_C
    
    #Njobdefs
    list_jobdefs_A=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_A ]))
    list_jobdefs_B=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_B ]))
    list_jobdefs_C=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ]) for x in DATA_C ]))
    jobdefs_A=sum(  [ x[2] for x in list_jobdefs_A]  )
    jobdefs_B=sum(  [ x[2] for x in list_jobdefs_B]  )
    jobdefs_C=sum(  [ x[2] for x in list_jobdefs_C]  )
    jobdefs_sum=jobdefs_A+jobdefs_B+jobdefs_C
    
    #Njobsets
    jobset_A=len(  list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_A ]))  )
    jobset_B=len(  list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_B ]))  )
    jobset_C=len(  list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ]) for x in DATA_C ]))  )
    
    
    print u'avg_size_jobset_jobdef:'
    print u'\t A: JOBSETS: %8d\tAVG. NJOBS per JOBSET: %4.2f \t\tJOBDEFS: %8d\tAVG. NJOBS per JOBDEF: %4.2f  \tJOBS: %8d  \tAVG JOBDEFS per JOBSET: %4.15f  ' % (\
        jobset_A, 1.0*jobs_A/jobset_A, jobdefs_A, 1.0*jobs_A/jobdefs_A, jobs_A, 1.0*jobdefs_A/jobset_A)
    print u'\t B: JOBSETS: %8d\tAVG. NJOBS per JOBSET: %4.2f \t\tJOBDEFS: %8d\tAVG. NJOBS per JOBDEF: %4.2f  \tJOBS: %8d  \tAVG JOBDEFS per JOBSET: %4.7f  ' % (\
        jobset_B, 1.0*jobs_B/jobset_B, jobdefs_B, 1.0*jobs_B/jobdefs_B, jobs_B, 1.0*jobdefs_B/jobset_B)
    print u'\t C: JOBSETS: %8d\tAVG. NJOBS per JOBSET: %4.2f \t\tJOBDEFS: %8d\tAVG. NJOBS per JOBDEF: %4.2f  \tJOBS: %8d  \tAVG JOBDEFS per JOBSET: %4.7f  ' % (\
        jobset_C, 1.0*jobs_C/jobset_C, jobdefs_C, 1.0*jobs_C/jobdefs_C, jobs_C, 1.0*jobdefs_C/jobset_C)


def sites_per_category(category):
    global LEGEND
    
    DATA_CATEGORY=[x for x in DAILYLOGV2 if x[2]==category]
    
    print u'Category %s (%s)' % (category, LEGEND[category])
    
    sites_jobset={}
    list_jobset_category=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['SITE'] ]) for x in DATA_CATEGORY ]))
    sites=list(set([x[2] for x in list_jobset_category]))
    sites.sort()
    for site in sites:
        jobsets_at_site=[x for x in list_jobset_category if x[2]==site]
        #sites_jobset[site]={'len':len(jobsets_at_site), 'val': jobsets_at_site}
        sites_jobset[site]=len(jobsets_at_site)
    jobset_total=sum([ sites_jobset[x] for x in sites_jobset ])
    jobset_sites=[ (sites_jobset[x], x) for x in sites_jobset ]
    jobset_sites=sorted(jobset_sites, key=itemgetter(0), reverse=True)
    print u'DEBUG', u'sites_jobset', jobset_sites, u'\n', jobset_total
    print u'Order by NJobsSets per site (Category %s: %s)' % (category, LEGEND[category])
    for site in [ x[1] for x in jobset_sites ]:
        print u'CATEGORY: %s \tSITE: %25s \t NJOBSETS %5d \t\t NJOBSET/NTOTALJOBSETS \t%3.3f%%' % (category, site, sites_jobset[site], 100.0*sites_jobset[site]/jobset_total)
    
    # Njobdef and Njobs does not make sense when user decides to exclude on jobset level
    if category!='E':
        sites_jobdefs={}
        list_jobdefs_category=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['SITE'] ]) for x in DATA_CATEGORY ]))
        sites=list(set([x[3] for x in list_jobdefs_category]))
        sites.sort()
        for site in sites:
            jobdefs_at_site=sum([x[2] for x in list_jobdefs_category if x[3]==site])
            sites_jobdefs[site]=jobdefs_at_site
        jobdef_total=sum([ sites_jobdefs[x] for x in sites_jobdefs ])
        jobdef_sites=[ (sites_jobdefs[x], x) for x in sites_jobdefs ]
        jobdef_sites=sorted(jobdef_sites, key=itemgetter(0), reverse=True)
        print u'DEBUG', u'sites_jobdefs', jobdef_sites, u'\n', jobdef_total
        print u'Order by NJobDefs per site (Category %s: %s)' % (category, LEGEND[category])
        for site in [ x[1] for x in jobdef_sites ]:
            print u'CATEGORY: %s \tSITE: %25s \t NJOBDEFS %5d \t\t NJOBDEFS/NTOTALJOBDEFS \t%3.3f%%' % (category, site, sites_jobdefs[site], 100.0*sites_jobdefs[site]/jobdef_total)
        
        sites_jobs={}
        list_jobs_category=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ], x[ COLUMNID['SITE'] ]) for x in DATA_CATEGORY ]))
        sites=list(set([x[4] for x in list_jobs_category]))
        sites.sort()
        for site in sites:
            jobs_at_site=sum([x[3] for x in list_jobs_category if x[4]==site])
            sites_jobs[site]=jobs_at_site
        job_total=sum([ sites_jobs[x] for x in sites_jobs ])
        job_sites=[ (sites_jobs[x], x) for x in sites_jobs ]
        job_sites=sorted(job_sites, key=itemgetter(0), reverse=True)
        print u'DEBUG', u'sites_jobs', job_sites, u'\n', job_total
        print u'Order by NJobs per site (Category %s: %s)' % (category, LEGEND[category])
        for site in [ x[1] for x in job_sites ]:
            print u'CATEGORY: %s \tSITE: %25s \t NJOBS %5d \t\t NJOBS/NTOTALJOBS \t%3.3f%%' % (category, site, sites_jobs[site], 100.0*sites_jobs[site]/job_total)
    ### end if category!='E'


def sites_per_categories():
    print u'sites_per_category(A)'
    sites_per_category('A')
    print u'sites_per_category(B)'
    sites_per_category('B')
    print u'sites_per_category(C)'
    sites_per_category('C')
    print u'sites_per_category(E)'
    sites_per_category('E')


def clouds_per_category(category):
    global LEGEND
    
    DATA_CATEGORY=[x for x in DAILYLOGV2 if x[2]==category]
    
    print u'Category %s (%s)' % (category, LEGEND[category])
    
    cloud_jobset={}
    list_jobset_category=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['CLOUD'] ]) for x in DATA_CATEGORY ]))
    clouds=list(set([x[2] for x in list_jobset_category]))
    clouds.sort()
    for cloud in clouds:
        jobsets_at_cloud=[x for x in list_jobset_category if x[2]==cloud]
        cloud_jobset[cloud]=len(jobsets_at_cloud)
    jobset_total=sum([ cloud_jobset[x] for x in cloud_jobset ])
    jobset_clouds=[ (cloud_jobset[x], x) for x in cloud_jobset ]
    jobset_clouds=sorted(jobset_clouds, key=itemgetter(0), reverse=True)
    print u'DEBUG', u'clouds_jobset', jobset_clouds, u'\n', jobset_total
    print u'Order by NJobsSets per cloud (Category %s: %s)' % (category, LEGEND[category])
    for cloud in [ x[1] for x in jobset_clouds ]:
        print u'CATEGORY: %s \tCLOUD: %10s \t NJOBSETS %5d \t\t NJOBSET/NTOTALJOBSETS \t%3.3f%%' % (category, cloud, cloud_jobset[cloud], 100.0*cloud_jobset[cloud]/jobset_total)
    
    # Njobdef and Njobs does not make sense when user decides to exclude on jobset level
    if category!='E':
        clouds_jobdefs={}
        list_jobdefs_category=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['CLOUD'] ]) for x in DATA_CATEGORY ]))
        clouds=list(set([x[3] for x in list_jobdefs_category]))
        clouds.sort()
        for cloud in clouds:
            jobdefs_at_cloud=sum([x[2] for x in list_jobdefs_category if x[3]==cloud])
            clouds_jobdefs[cloud]=jobdefs_at_cloud
        jobdef_total=sum([ clouds_jobdefs[x] for x in clouds_jobdefs ])
        jobdef_clouds=[ (clouds_jobdefs[x], x) for x in clouds_jobdefs ]
        jobdef_clouds=sorted(jobdef_clouds, key=itemgetter(0), reverse=True)
        print u'DEBUG', u'clouds_jobdefs', jobdef_clouds, u'\n', jobdef_total
        print u'Order by NJobDefs per site (Category %s: %s)' % (category, LEGEND[category])
        for cloud in [ x[1] for x in jobdef_clouds ]:
            print u'CATEGORY: %s \tCLOUD: %10s \t NJOBDEFS %5d \t\t NJOBDEFS/NTOTALJOBDEFS \t%3.3f%%' % (category, cloud, clouds_jobdefs[cloud], 100.0*clouds_jobdefs[cloud]/jobdef_total)
        
        clouds_jobs={}
        list_jobs_category=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['JOBDEFCOUNT'] ], x[ COLUMNID['JOBCOUNT'] ], x[ COLUMNID['CLOUD'] ]) for x in DATA_CATEGORY ]))
        clouds=list(set([x[4] for x in list_jobs_category]))
        clouds.sort()
        for cloud in clouds:
            jobs_at_cloud=sum([x[3] for x in list_jobs_category if x[4]==cloud])
            clouds_jobs[cloud]=jobs_at_cloud
        job_total=sum([ clouds_jobs[x] for x in clouds_jobs ])
        job_clouds=[ (clouds_jobs[x], x) for x in clouds_jobs ]
        job_clouds=sorted(job_clouds, key=itemgetter(0), reverse=True)
        print u'DEBUG', u'clouds_jobs', job_clouds, u'\n', job_total
        print u'Order by NJobs per site (Category %s: %s)' % (category, LEGEND[category])
        for cloud in [ x[1] for x in job_clouds ]:
            print u'CATEGORY: %s \tCLOUD: %10s \t NJOBS %5d \t\t NJOBS/NTOTALJOBS \t%3.3f%%' % (category, cloud, clouds_jobs[cloud], 100.0*clouds_jobs[cloud]/job_total)
    ### end if category!='E'


def clouds_per_categories():
    print u'clouds_per_category(A)'
    clouds_per_category('A')
    print u'clouds_per_category(B)'
    clouds_per_category('B')
    print u'clouds_per_category(C)'
    clouds_per_category('C')
    print u'clouds_per_category(E)'
    clouds_per_category('E')


def user_excludes_site():
    global COLUMNID
    
    DATA_E=[x for x in DAILYLOGV2 if x[2]=='E']
    
    list_user_site_alldata=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['SITE'] ]) for x in DAILYLOGV2 ]))
    
    list_user_site=list(set([ (x[ COLUMNID['USERDN'] ], x[ COLUMNID['JOBSETID'] ], x[ COLUMNID['SITE'] ]) for x in DATA_E ]))
    users=list(set( x[0] for x in list_user_site ))
    users.sort()
    
    users_sites={}
    for user in users:
        jobsets_per_user=list(set([ x[1] for x in list_user_site_alldata if x[0]==user ]))
        sites_per_user=[ x[2] for x in list_user_site if x[0]==user ]
        users_sites[user]={}
        for site in list(set(sites_per_user)):
            users_sites[user][site]=sites_per_user.count(site)
        users_sites[user]['all-jobsets']=len(jobsets_per_user)
        ###users_sites[user]=sites_per_user
    #print u'users_sites', users_sites
    
    for user in users_sites:
        print
        user_site=[(users_sites[user][x], x) for x in users_sites[user] if x != 'all-jobsets']
        user_site=sorted(user_site, key=itemgetter(0), reverse=True)
        all_jobs=users_sites[user]['all-jobsets']
        for site in [x[1] for x in user_site]:
            if site != 'all-jobsets':
                print u'User \"%s\" submitted %5d jobsets, and excluded site \"%25s\" %5d-times (%3.3f%%)' % (user, all_jobs, site, users_sites[user][site], 100.0*users_sites[user][site]/all_jobs)
    

def run():
    print u'\n######### RUN: get_exclusion_dates'
    print u'exclusion_dates:', get_exclusion_dates()
    print u'\n######### RUN: category_distribution_jobset'
    category_distribution_jobset()
    print u'\n######### RUN: category_distribution_jobs'
    category_distribution_jobs()
    print u'\n######### RUN: avg_size_jobset_jobdef'
    avg_size_jobset_jobdef()
    print u'\n######### RUN: sites_per_categories'
    sites_per_categories()
    print u'\n######### RUN: clouds_per_categories'
    clouds_per_categories()
    print u'\n######### RUN: user_excludes_site'
    user_excludes_site()
    


def main():
    global SPACETOKEN_GROUPS, PREFIX, Timestamp
    args = sys.argv[1:]
    if len(args) < 1:
        print 'usage: verify_values.py PARAMETER'
        sys.exit(-1)
    
    PREFIX=args[0]
    
    run()
    
    print;print;print


if __name__ == '__main__':
    main()



