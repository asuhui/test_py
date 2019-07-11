#coding=utf-8
class User(object):
    __instance=None
    def __init__(self,name):
        self.name=name
    def __new__(cls,name):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
        return cls.__instance
u1=User("sh")
u2=User("su")
print(u1==u2)
print("u1:%s,u2:%s"%(id(u1),id(u2)))
