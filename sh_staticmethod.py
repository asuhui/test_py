#coding=utf-8
class Person(object):
    name="su"#类属性
    def __init__(self,name):
        self.name=name
    @staticmethod
    def getName(self):#静态方法
        return self.name
if __name__=="__main__":
    
    print(Person.getName())
    
