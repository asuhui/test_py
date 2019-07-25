#coding=utf-8
class Test(object):
    name="su"#类属性
    def __init__(self,name):
        self.name=name
    @classmethod #装饰器
    def getName(cls):#类属性
        return cls.name
if __name__=="__main__":
    print(Test.getName())
