#coding=utf-8
class Test(object):
    def __init__(self,func):
        print("func:%s"%func.__name__)
        self.func=func
    def __call__(self): #类装饰器调用方法
        print("附加功能...")
        self.func()
if __name__=="__main__":
    @Test #生成Test的一个对象，所以会调用__init__方法，并且把下面装饰的函数作为参数传进去
    def fun():
        print("fun")
    fun() #调用Test的一个对象的__call__方法
