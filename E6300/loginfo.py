#coding=utf-8
import time
import xlsxwriter
class Loginfo(object):
    #file日志处理方法
    def __init__(self,path="",mode="w"):
        fname=path+time.strftime("%Y-%m-%d",time.gmtime())
        self.log=open(path+fname+".txt",mode)

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()
class Xlloginfo(object):
    #Excel处理日志方法
    def __init__(self,path=""):
        frame=path+time.strftime("%Y-%m-%d",time.gmtime())
        self.row=0
        self.xl=xlsxwriter.Workbook(path+frame+".xls")
    def Xl_write(self,*args):
        col=0
        for val in args:
            self.sheet.write_string(self.row,col,val)
            col+=1
        self.row+=1
    def Xl_init(self,sheetname,*title):
        self.sheet=self.xl.add_worksheet(sheetname)
        self.sheet.set_column("A:E",30)
        self.Xl_write(*title)
    def Xl_Write(self,*args):
        self.Xl_write(*args)
    def Xl_close(self):
        self.xl.close()
if __name__=="__main__":
    #log=Loginfo()
    #log.log_write("test Loginfo 测试")
    #log.log_close()
    log=Xlloginfo()
    log.Xl_init("test","uname","pwd","result","info")
    log.Xl_close()