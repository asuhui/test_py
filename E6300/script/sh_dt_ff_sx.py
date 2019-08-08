#coding=utf-8
import types
class Person(object):
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

if __name__=="__main__":
    p=Person("sh",25)
    p.sex="male"
    print(p.sex)
    def showInfo(self):
        print(self.name)
        print(self.age)
    p.showInfo=types.MethodType(showInfo,p)
    p.showInfo()