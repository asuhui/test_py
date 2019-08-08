#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


br=webdriver.Chrome()
url="http://192.1.1.67:8080/E6300/"
br.get(url)


#登录模块
def login(username,password):
    print("浏览器最大化")
    br.maximize_window()#将浏览器最大化显示
    time.sleep(1)
    #用户名，密码
    br.find_element_by_id("username").send_keys(username)
    time.sleep(1)
    br.find_element_by_id("password").send_keys(password)
    time.sleep(1)
    #登录按钮
    ActionChains(br).click_and_hold(br.find_element_by_id("ext-gen75").click()).perform()

login("admin","admin")
   
#ele=br.find_element_by_id("ext-comp-1040")
#print(ele.text)
time.sleep(3)
ActionChains(br).move_to_element(br.find_element_by_id("ext-comp-1074")).perform()
time.sleep(2)
print("1")
br.find_element_by_id("ext-comp-1074").click()
print("2")

#br.quit()
