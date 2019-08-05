#coding=utf-8
import os
#该程序只可在Linux系统或者mac中运行
pid=os.fork()

if pid < 0:
    print("fork()调用失败。")
elif pid == 0:
    print("子进程为%d,父进程为%d."%(os.getpid(),os.getppid()))
else:
    print("父进程为%d,子进程为%d."%(os.getpid(),pid))

