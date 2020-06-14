# _*_coding:UTF-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.maximize_window()#窗口最大化

driver.get('http://www.testingedu.com.cn:8000/Home/User/login.html')

#实现登录
driver.find_element_by_id('username').clear()#情况输入框
driver.find_element_by_id('username').send_keys('13800138006')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('verify_code').clear()
driver.find_element_by_id('verify_code').send_keys('1')
driver.find_element_by_name('sbtbutton').click()

print(driver.title)#打印标题
