#coding=utf-8
#coding=utf-8
import os
#从/home/python目录下找到包含有hello的py文件是那些
list_filepy=[]#存储内容含有hello的py文件
def read_file(parent_dir,file_name):#
    abs_file_dir=os.path.join(parent_dir,file_name)
    if os.path.isdir(abs_file_dir):
        for file in os.listdir(abs_file_dir):
            read_file(abs_file_dir,file)
    else:
        if abs_file_dir.endswith(".py"):
            if read_find_hello(abs_file_dir):
                list_filepy.append(abs_file_dir)

def read_find_hello(file_name):
    f=open(file_name,'r', encoding='UTF-8')
    flag=False
    while True:
        if "hello" in f.readline():
            flag=True
            break
        elif f.readline()=="":
            break
    f.close()
    return flag



if __name__=="__main__":
    read_file(r"C:\Users\Administrator\PycharmProjects","E6300")
    print(list_filepy)