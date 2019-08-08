#coding=utf-8
class Test(object):
    name="su" #类属性
    def __init__(self,name):#实例方法（魔术方法）
        self.name=name#实例属性
    @classmethod
    def getName(cls):#类方法
        return  cls.name
def wl(func):
    def wrap():
        print("...1...")
        func()
    return wrap
class Person(object):
    def __init__(self,name):
        self.name=name
    def __call__(self, *args, **kwargs):#类装饰器
        print("123")

import datetime

def dayofyear():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    date2 = datetime.date(year=int(year),month=int(month),day=int(day))
    print ((date2 - date1).days+1)

if __name__=="__main__":
    dayofyear()
    #print(Test.getName())
    @wl
    def f1():
        print("f1")
    p=Person("su")
    #p()#类装饰器调用