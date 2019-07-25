#coding=utf-8
class Person(object):
    def __init__(self,name):
        self.name=name
    @staticmethod
    def getName(self):
        return self.name
if __name__=="__main__":
    p=Person("sh")
    print(p.getName())
    
