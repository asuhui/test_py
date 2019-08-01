#coding=utf-8
class Subject(object):
    def __init__(self, subject):
        self.subject1 = subject
        self.subject2 = 'cpp'
    #属性拦截方法
    def __getattribute__(self, obj):
        if obj == "subject1":
            return "review python"
        else: 
            return object.__getattribute__(self, obj)
if __name__ == "__main__":
    s=Subject("subject")
    print(s.subject1)
    print(s.subject2)
