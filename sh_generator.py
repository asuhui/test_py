#coding=utf-8
def fib(times):#斐波拉切函数实现合成器
    n=0
    a,b=0,1
    while(n<times):
        yield a
        a,b=b,a+b
        n=n+1
    return "done"
if __name__=="__main__":
    fi=fib(5)
    print(fi)
    print(fi.__next__())
    print(fi.send(None))
    print(next(fi))
