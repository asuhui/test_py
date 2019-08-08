#import sys
#from imp import reload
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
# 解决中文转码python2
#reload(sys)
#sys.setdefaultencoding( "utf-8" )

wb=webdriver.Chrome()
wb.get("http://192.1.8.49:8080/E6300")
wb.maximize_window()
time.sleep(1)
wb.find_element_by_id("username").send_keys("admin")
time.sleep(1)
wb.find_element_by_id("password").send_keys("admin")
time.sleep(1)
wb.find_element_by_id("ext-gen75").click()

#time.sleep(3)
#加载到页面找到元素ext-comp-1093
wait = ui.WebDriverWait(wb, 20)
wait.until(lambda wb: wb.find_element_by_id("ext-comp-1093"))
wb.find_element_by_id("ext-comp-1093").click()
on=wb.find_element_by_id("ext-comp-1093")
time.sleep(1)
#ActionChains(wb).context_click(on).perform()#右击
#dagl=wb.find_element_by_css_selector('pwsb.dagl')
#ActionChains(wb).move_to_element(dagl)
dagl=on.find_element_by_xpath('//*[@id="pwsb.dagl"]')
ActionChains(wb).move_to_element(dagl).perform()
time.sleep(1)
dagl.find_element_by_xpath('//*[@id="pwsb.dagl.wgsbtzgl"]').click()

time.sleep(2)
wb.close()
