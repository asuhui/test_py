#coding=utf-8
class Person(object):
    def __init__(self,name):
        self.name=name
    def work(self,type):
        alex=Factory.get_alex(type)
        alex.cut_tree()
class Alex(object):
    def __init__(self,name):
        self.name=name
    def cut_tree(self):
        print("斧头砍树")
class StoneAlex(Alex):
    def cut_tree(self):
        print("石斧砍树")
class SteelAlex(Alex):
    def cut_tree(self):
        print("钢斧砍树")
class Factory(object):
    @staticmethod
    def get_alex(cls,type):
        if type=="stone":
            return cls.StoneAlex("石斧")
        elif type=="steel":
            return cls.SteelAlex("钢斧")
        else:
            print("输入错误")
        
p=Person("zs")
p.work("stone")
