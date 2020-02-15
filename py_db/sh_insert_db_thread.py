#coding=utf-8
'''test packege'''
__author__ = "sallen"

# 工具库导入
import random
import datetime
import time
import cx_Oracle
import threading
# 注：设置环境编码方式，可解决读取数据库乱码问题
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class myTread(threading.Thread):
    def __init__(self, threadID, name, year, month, day):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.year = year
        self.month = month
        self.day = day

    def run(self):
        print("开启线程:" + self.name)
        time.ctime(time.time())
        # 获取锁， 用于线程同步
        threadLock.acquire()
        all_data(self.year, self.month, self.day)
        # 释放锁，开启下一个线程
        threadLock.release()


def input_to_powerdata(year, month, day, m, table):
    host = "192.1.1.29"  # 数据库ip
    port = "1521"  # 端口
    sid = "ORCL"  # 数据库名称
    dsn = cx_Oracle.makedsn(host, port, sid)

    conn = cx_Oracle.connect("E6300", "E6300", dsn)
    cur = conn.cursor()
    min_m = date_fif_min(year, month, day)
    for j in range(0, 96*3):
        print("power" + str(m) + str(j))
        ua = round(random.uniform(1.8, 2.6) * 100, 2)
        ub = round(random.uniform(1.8, 2.6) * 100, 2)
        uc = round(random.uniform(1.8, 2.6) * 100, 2)
        data = [100000 + j, 10000 + m, min_m[j], ua, ub, uc]

        query = "insert into " + table + "(ID, MPID, DATATIME, UA, UB, UC)\
        values('%s', '%s', to_date('%s', 'yyyy-mm-dd hh24:mi:ss'), '%s', '%s', '%s')"
        cur.execute(query % (data[0], data[1], data[2], data[3], data[4], data[5]))
    conn.commit()
    cur.close()
    conn.close()


def date_fif_min(year, month, day):
    # 15分钟时刻
    start_dt = datetime.datetime(year, month, day)
    interval = datetime.timedelta(seconds=300)
    fif_min = []
    for i in range(96):
        fif_min.append((start_dt + interval * i).strftime("%Y-%m-%d %H:%M:%S"))
    return fif_min


def all_data(year, month, day):

    for m in range(1840, 2001):
        print('power_data' + str(m))
        input_to_powerdata(year, month, day, m, "est_pw_powerflowdata")


if __name__ == "__main__":
    threadLock = threading.Lock()
    threads = []

    # 创建新线程
    thread1 = myTread(1, 'Thread-1', 2019, 1, 1)
    # thread2 = myTread(2, 'Thread-2', 2019, 1, 4)
    # thread3 = myTread(3, 'Thread-3', 2019, 1, 7)
    # 开启新线程
    thread1.start()
    # thread2.start()
    # thread3.start()
    # 添加线程到线程列表
    threads.append(thread1)
    # threads.append(thread2)
    # threads.append(thread3)
    # 等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")
