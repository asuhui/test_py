 # coding=utf-8
class testcase(object):
     def get_add(self, a, b):
        return a+b

class Subject(object):
     def __init__(self, subject):
        self.subject1 = subject
        self.subject2 = 'cpp'

     def __getattribute__(self, item):
        if item=="subject1":
            return "review python"
        else:
            return object.__getattribute__(self, item)
def square(x):
    return x * x
m = map(square , (1, 2, 3)) #map内置函数会根据提供的函数对指定序列做映射。

n=filter(lambda x:x%2==1,(1,2,3,4,5,6))#filter内置函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
from functools import  reduce
#在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 functools 模块里，
 # 如果想要使用它，则需要通过引入 functools 模块来调用 reduce() 函数
def add(x, y):
    return x+y

h=reduce(add, range(1,10))

if __name__ == "__main__":
    t = testcase().get_add(1, 2)
    print(t)
    print("hello")
    s = Subject("subject")
    print(s.subject1)
    print(s.subject2)
    for i in n:
        print(i)
    print(h)