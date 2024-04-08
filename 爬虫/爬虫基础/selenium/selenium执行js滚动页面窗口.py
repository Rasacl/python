import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://liuyan.people.com.cn/threads/list?fid=5055&formName=%E5%B7%A5%E4%B8%9A%E5%92%8C%E4%BF%A1%E6%81%AF%E5%8C%96%E9%83%A8%E5%85%9A%E7%BB%84%E4%B9%A6%E8%AE%B0%E3%80%81%E9%83%A8%E9%95%BF%E9%87%91%E5%A3%AE%E9%BE%99&position=1'

driver.get(url)
# 设置隐式等待，最大等待时间为10秒
driver.implicitly_wait(10)

for i in range(5):
    time.sleep(random.random())
    js = 'window.scrollBy(0,{})'.format(random.randint(100, 300))
    # 通过driver对象执行js代码
    driver.execute_script(js)

time.sleep(5)

driver.quit()