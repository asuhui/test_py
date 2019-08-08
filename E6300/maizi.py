#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import userData
from loginfo import Loginfo,Xlloginfo

def get_ele_times(driver,times,func):#设置发现元素时间
    return WebDriverWait(driver,times).until(func)
def openBrower():
    #返回句柄，浏览器对象
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle

def loadUrl(handle,url):
    #返回url
    handle.get(url)
    handle.maximize_window()

def findElement(handle,args):
    #查找元素
    #parm:handle(句柄)，args(文件中保存的元素参数)
    if "text_id" in args:
        #点击登录按钮，进入登录窗口
        ele_login=get_ele_times(handle,10,lambda d: handle.find_element_by_link_text(args["text_id"]))
        ele_login.click()
    #parm:user_Ele(登录用户账户id元素值),pwd_Ele(登录密码id元素值)，login_Ele(登录窗口id元素值)
    user_Ele=handle.find_element_by_id(args["user_id"])
    pwd_Ele=handle.find_element_by_id(args["pwd_id"])
    login_Ele=handle.find_element_by_id(args["login_id"])
    return user_Ele,pwd_Ele,login_Ele
def sendVals(ele_tuple,args):
    #parm:ele_tuple元素值对象，args:元素值对象输入的值
    #发送值
    time.sleep(2)
    list_keys=["uname","pwd"]
    i=0
    for key in list_keys:
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(args[key])
        i+=1
    ele_tuple[2].click()
    time.sleep(1)
def checkResult(handle,err_id,args,log):
    #检查结果，输出日志
    #parm:handle:句柄，err_id:错误的class元素值,args:错误或者正确信息的输入值，log:错误日志信息
    result=False
    try:
        #账号或者密码错误
        err=handle.find_element_by_id(err_id)
        print("Account and PWD Error!")
        print(err.text)
        #msg="%s:%s error %s\n"%(arg["uname"],arg["pwd"],err.text)
        log.Xl_write(args["uname"],args["pwd"],"Error",err.text)
        #log.log_write(msg)
    except:
        #账号或者密码正确
        print("Account and PWD Right!")
        #msg = "%s:%s pass\n" % (arg["uname"], arg["pwd"])
        log.Xl_write(args["uname"], args["pwd"], "PASS")
        result=True
    #handle.close()
    return result
def login_out(handle,ele_dict):
    #注销登录
    handle.find_element_by_class_name(ele_dict["login_out"]).click()

def login_test(ele_dict,user_list):
    #主函数测试登录
    wb=openBrower()
    loadUrl(wb,ele_dict["url"])
    #log=Loginfo()
    log=Xlloginfo()
    log.Xl_init("sheet1","uname","pwd","result","msg")
    ele_tuple=findElement(wb,ele_dict)
    for arg in user_list:
        sendVals(ele_tuple,arg)
        result=checkResult(wb,ele_dict["error_id"],arg,log)
        if result:
            login_out(wb,ele_dict)
            ele_tuple = findElement(wb, ele_dict)
    #log.log_close()
    log.Xl_close()
    wb.close()
if __name__=="__main__":
    ele_dict=userData.get_webinfo("webinfo.txt")
    #ele_dict={"url":info["url"],"text_id":info["text_id"],"user_id":info["user_id"],"password_id":info["pwd_id"],\
    #        "login_id":info["login_id"],"uname":acount,"pwd":password,"error_id":info["error_id"]}
    #user_list=userData.get_userinfo("userinfo.txt")
    xl=userData.XlUserinfo("userinfo.xls")
    user_list=xl.get_sheetinfo_by_index(0)
    login_test(ele_dict,user_list)
