#coding=utf-8
#装饰器例子
def log(func):
    def wrapper(*args,**kwargs):
        print("%s"%func.__name__)
        return func(*args,**kwargs)
    return wrapper
@log
def now():
    print("2019-09-06")

def log1(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print("%s,%s"%(func.__name__,text))
            return func(*args,**kwargs)
        return wrapper
    return decorator
@log1("hello")
def today():
    print("2019-09-08")
now()
today()
