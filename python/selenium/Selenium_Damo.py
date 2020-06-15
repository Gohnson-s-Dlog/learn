from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time#注意:一定要考虑加载时间,否则可能会报各种定位元素找不到 的异常


options=Options()#创建options对象  无界面模式打开前的条件
options.add_argument('--headless')#
'''
options.add_argument('--user-agent=""')  # 设置请求头的User-Agent
options.add_argument('--window-size=1280x1024')  # 设置浏览器分辨率（窗口大小）
options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
options.add_argument('--incognito')  # 隐身模式（无痕模式）
options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('--disable-javascript')  # 禁用javascript
options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
options.add_argument('--headless')  # 浏览器不提供可视化页面
options.add_argument('--ignore-certificate-errors')  # 禁用扩展插件并实现窗口最大化
options.add_argument('--disable-gpu')  # 禁用GPU加速
options.add_argument('–disable-software-rasterizer')
options.add_argument('--disable-extensions')
options.add_argument('--start-maximized')
'''
driver=webdriver.Chrome()#创建驱动对象 chrome_options=options
driver.maximize_window()#窗口最大化
driver.get('http://www.baidu.com')#出现错误原因未加http://
time.sleep(0.3)
print(driver.title) #打印网页标题
# driver.quit()#退出浏览器
# driver.find_element_by_id('username').clear()#情况输入框
# driver.find_element_by_id('username').send_keys('13800138006')
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('password').send_keys('123456')
# driver.find_element_by_id('verify_code').clear()
# driver.find_element_by_id('verify_code').send_keys('1')
# driver.find_element_by_name('sbtbutton').click()
#自动化测试元素定位
in_put=driver.find_element_by_id(id_='kw')#通过id选择器找到输入框
# in_put=driver.find_element_by_xpath('//*[@id="kw"]')
time.sleep(0.9)
in_put.send_keys('James')#输入James
button=driver.find_element_by_id(id_='su')#通过id选择器找到按钮
# button=driver.find_element_by_xpath('//*[@id="su"]')
button.click()#点击按钮
time.sleep(2)
driver.find_element_by_partial_link_text('Jame').click()

# driver.find_element_by_xpath()          #
# driver.find_element_by_css_selector()   #
# driver.find_element_by_id()             #
# driver.find_element_by_link_text()      #
# driver.find_element_by_partial_link_text()  #
# driver.find_element_by_name()               #
# driver.find_element_by_class_name()         #
# driver.find_element_by_tag_name()           #
