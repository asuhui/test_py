#coding=utf-8
class User(object):
    def __init__(self,name):
        self.name=name
    def get_instance(cls,name):
        if not cls.__instance:
            cls.__instance=User(name)
        return cls.__instance
u1=User.get_instance("zs")
u2=User.get_instance("ls")
print(u1==u2)
