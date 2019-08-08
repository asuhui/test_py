#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

wb=webdriver.Chrome()
wb.get("http://180.101.226.58:9999/index.jsp")
wb.maximize_window()#浏览器最大化
#wb.set_window_size(300,400)#设置浏览器大小
#wb.back()#后退
#wb.forward()#前进
time.sleep(2)
user_name=wb.find_element_by_xpath("//*[@id='username']")
user_name.send_keys("624")
pass_wd=wb.find_element_by_css_selector("#password")
pass_wd.send_keys("")
wb.find_element_by_link_text("登录").click()
rcgl=wb.find_element_by_xpath("//*[@id='topnav']/li[2]/span/span")#日常管理
ActionChains(wb).move_to_element(rcgl).perform()
ribao=wb.find_element_by_xpath("//*[@id='topnav']/li[2]/ul/li[1]")#研发日报
ribao.click()
xinjian=wb.find_element_by_xpath("//*[@id='screentool']/button[1]")#新建
xinjian.click()

xuan_pro=wb.find_element_by_xpath("//*[@id='box_0_self75_gzjh']/span/button/img")#选择项目
xuan_pro.click()
#login=wb.find_element_by_class_name("button")
#ActionChains(wb).click_and_hold(login).perform()
#元素定位的8大方法
"""
c=wb.find_element_by_id()
c=wb.find_element_by_name()
c=wb.find_element_by_class_name()
c=wb.find_element_by_tag_name()
c=wb.find_element_by_link_text()
c=wb.find_element_by_partial_link_text()
c=wb.find_element_by_xpath()
c=wb.find_element_by_css_selector()
"""
#鼠标操作事件
"""
from selenium.webdriver.common.action_chains import ActionChains
#ActionChains(wb).context_click(c).perform()#右击在元素上
#ActionChains(wb).move_to_element(baidu).perform()#鼠标悬停在一个元素上
#ActionChains(wb).click_and_hold(baidu).perform()#按下鼠标左键在一个元素上(不是左击，左击用click（）)
#ActionChains(wb).double_click(baidu).perform()##双击
#ActionChains(wb).drag_and_drop(baidu).peiform()##拖动
"""
#键盘操作事件
"""
from selenium.webdriver.common.keys import Keys

"""
time.sleep(3)

wb.close()
