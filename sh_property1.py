#coding=utf-8
class Test(object):
    def __init__(self):
        self._num=100
    def getNum(self):
        return self._num
    def setNum(self,num):
        self._num=num
    num=property(getNum,setNum)
if __name__=="__main__":
    t=Test()
    t.num=20
    print(t.num)

