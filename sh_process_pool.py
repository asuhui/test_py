from multiprocessing import Pool
import time
import os

def work(msg):
    print("子进程PID:%d"%os.getpid())
    startTime=time.time()
    time.sleep(2)
    stopTime=time.time()
    print("子进程msg：%s,花费的时间%d"%(msg,stopTime-startTime))

if __name__=="__main__":
    #创建进程池
    pool=Pool(3)

    for x in range(10):
        pool.apply(work,args=(x,)) #同步请求

    #关闭进程池
    pool.close()
    #父进程等待进程池的结束
    pool.join()
    print("进程池已结束")
