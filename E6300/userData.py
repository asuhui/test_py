#conding=utf-8
import codecs
import xlrd

def get_webinfo(path):
    #txt文件获取web页面元素信息
    web_info={}
    config=codecs.open(path,"r","GBK")
    for line in config:
        result=(line.strip()).split("=")
        web_info.update(dict([result]))
    config.close()
    return web_info
def get_userinfo(path):
    #txt文件获取userinfo信息
    user_info=[]
    config=codecs.open(path,"r","utf-8")
    for line in config:
        user_info1={}
        result=(line.strip()).split(";")
        for res in result:
            user_info1.update(dict([res.split("=")]))
        user_info.append(user_info1)
    config.close()
    return user_info
class XlUserinfo(object):
    #定义接口，excel中获取用户信息
    def __init__(self,path=""):
        self.x1=xlrd.open_workbook(path)
    def flaottostr(self,val):#Excel中数字float转换成str类型
        if isinstance(val,float):
            val=str(int(val))
        return val
    #get_sheet_info:获取Excel文件内容
    #parm:none
    #return:Excel文件内容信息列表
    def get_sheet_info(self):
        listkey=["uname","pwd"]
        infolist=[]
        for row in range(1,self.sheet.nrows):
            info=[self.flaottostr(val) for val in self.sheet.row_values(row)]
            #info = self.sheet.row_values(row)
            #print(info)
            tmp=zip(listkey,info)
            infolist.append(dict(tmp))
        return infolist
    #get_sheetinfo_by_name:通过excelsheet名称获取excel内容
    #parm：name(sheet名)
    #return：
    def get_sheetinfo_by_name(self,name):
        self.sheet=self.x1.sheet_by_name(name)
        return self.get_sheet_info()
    def get_sheetinfo_by_index(self,index):
        self.sheet=self.x1.sheet_by_index(index)
        return  self.get_sheet_info()

if __name__=="__main__":
    #web_info=get_webinfo('webinfo.txt')
    #user_info=get_userinfo(r"userinfo.txt")
    #print(user_info)
    #for key in web_info:
     #  print(key,web_info[key])
    x1=XlUserinfo("userinfo.xls")
    print(x1.get_sheetinfo_by_index(0))
    print(x1.get_sheetinfo_by_name("Sheet1"))

