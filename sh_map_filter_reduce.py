#coding=utf-8
from functools import reduce #python2为内置函数，python3为functools模块函数

def square(x):
    return x*x

def add(x,y):
    return x+y
if __name__ == "__main__":
    mp=map(square,range(5))#映射,python3返回可迭代对象
    fter=filter(lambda x:x%2==0,range(10))#过滤，python3返回可迭代对象
    rd=reduce(add,range(5))#累加

    for i in mp:
        print(i)

    for i in fter:
        print(i)
    print(rd)
