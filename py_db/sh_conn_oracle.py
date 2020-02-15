#coding=utf-8
import cx_Oracle as oracle
try:
    conn = oracle.connect("E6300/E6300@192.1.31.189:1521/orcl")
    cursor = conn.cursor()
    ndate=[]
    x = cursor.execute("select * from est_pw_statdeviceinfo order by id desc")
    data = list(x.fetchone())
    #print(data)
    #print(type(data[0]))
    i=0
    for value in data:
        #print(value)
        if i == 0:
            ndate.append(value+1)
        elif i == 1:

            ndate.append()
        else:
            ndate.append(value)
        i=i+1
    #print(ndate)
    ndate = tuple(ndate)
    print(len(ndate))
    sql = "insert into EST_PW_STATDEVICEINFO (ID, STDATE, STTYPE, \
OBJTYPE, OBJID, ACTIONTIMES, COMPENSATIONRATE, ACTUAL_CAPACITY, MONITORRATE, \
TERMONLINERATE, INPUTTIMES, FAULTPROCESSDURATION, FAULTPROCESSTIMES, DEVICEAVAILABILITY, \
FAULTCAPACITYHOURS, SAVEINGQE, TERMNUM, RUNNUM, BACKUPNUM, REPAIRNUM ,FAULTSTARTTIME,FAULTENDTIME) \
values (%d,%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%ndate
    print(sql)
    cursor.execute(sql)
    cursor.execute("commit")
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()