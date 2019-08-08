#coding=utf-8
import os

#file = open(r"C:\Users\Administrator\Desktop\新建文本文档.txt","w+")
#file.write("hello")
#file.write("\nworld")
#print(file.tell())
#file.seek(0, 0)
#f = file.read(5)
#print(f)
#file.close()
print("欢迎进入学生管理系统".center(30))
print("*"*30)
print("输入1：添加学生信息")
print("输入2：查看所有学生信息")
print("输入5：退出系统")
stus = []
while True:
    choice = input("输入你的选择:")
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice ==5:
        print("退出系统")
        exit(0)
        pass





