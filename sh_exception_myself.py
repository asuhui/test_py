#coding=utf-8
class PasswordException(Exception):#自定义异常类
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
    def __str__(self):
        return ("密码%s长度不正确。"%(self.pwd))
def reg(uname,pwd):
    if len(pwd)<6:
        raise PasswordException(uname.pwd)
    else:
        print("用户名为：%s,密码为%s"%(uname,pwd))
try:
    reg("su","123")
except Exception as e:
    print(e)

