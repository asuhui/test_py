#coding=utf-8
class Test(object):
    def __init__(self):
        self._num=100
    @property
    def getNum(self):
        return self._num
    @num.setter
    def setNum(self,num):
        self.num=num
if __name__=="__main__":
    t=Test()
    t.num=20
    print(t.num)
        
