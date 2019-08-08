#coding = utf-8
from selenium import webdriver
import time

wb = webdriver.Firefox()
wb.get("https://www.baidu.com")
wb.maximize_window()#浏览器最大化
#wb.set_window_size(800,400)#设置浏览器的长度与宽度
time.sleep(2)
#wb.find_element_by_link_text("网易").click()
#wb.find_element_by_xpath("//*[@id='kw']").send_keys("123")
wb.find_element_by_css_selector("#kw").send_keys("123")
size=wb.find_element_by_css_selector("#kw").size
print(size)
t=wb.find_element_by_css_selector("#kw").text
print(t)
attribute=wb.find_element_by_css_selector("#kw").get_attribute("type")
print(attribute)
time.sleep(2)
wb.close()