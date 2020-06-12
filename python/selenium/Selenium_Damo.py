from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options=Options()#创建options对象  无界面模式打开前的条件
options.add_argument('--headless')#

driver=webdriver.Chrome(chrome_options=options)

driver.get('http://www.baidu.com')
print(driver.title)
driver.quit()

#自动化测试元素定位

in_put=driver.find_element_by_id(id_='kw')#通过id选择器找到输入框
in_put.send_keys('James')#输入James
button=driver.find_element_by_id(id_='su')#通过id选择器找到按钮
button.click()#点击按钮