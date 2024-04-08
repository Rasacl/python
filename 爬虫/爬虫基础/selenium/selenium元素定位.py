from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# 创建一个driver对象(启动浏览器)
driver = webdriver.Chrome()

# 打开一个网页
driver.get("https://www.baidu.com")

time.sleep(5)

# 根据class获取元素
driver.find_element(By.CLASS_NAME, "s_ipt").send_keys('hhhhhhhhh')
"""
获取标签名 tagname
获取标签文本 text
获取父级标签 parent
获取属性 get_attribute
判断元素是否可见 is_displayed
"""
time.sleep(2)
"""
点击元素 click
输入文本 send_keys
清空文本 clear
"""
# 根据id获取元素
driver.find_element(By.ID, 'su').click()

time.sleep(5)
# 退出浏览器
driver.quit()
