#coding=utf-8
#工厂方法
class Person(object):
    def __init__(self,name):
        self.name=name
    def work(self):
        alex=StoneFactory("石头")
        alex.cut_tree()
class Alex(object):
    def __init__(self,name):
        self.name=name
    def cut_tree(self):
        print("斧头砍树")
class StoneAlex(Alex):
    def cut_tree(self):
        print("石头斧头砍树")
class SteelAlex(Alex):
    def cut_tree(self):
        print("钢铁斧头砍树")
class Factory(object):
    def create_alex(self):
        pass
class StoneFactory(Factory):
    def create_alex(self):
        return StoneAlex("石斧")
class SteelFactory(Factory):
    def create_alex(self):
        return SteelAlex("钢斧")
p=Person("sh")
p.work()

