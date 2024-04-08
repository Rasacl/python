"""
  强制等待 time.sleep(3)  强制等待，不管网页是否加载完都会等待
  隐式等待  driver.implicitly_wait(10)  如果页面元素加载出来就继续往下执行，否则继续等待 直到达到最大等待时间 ，如果超过最大等待时间，抛出异常
  显示等待  设置等待条件  当条件成立时，继续执行下面的代码  当条件一直未成立，抛出异常
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
time.sleep(2)  # 强制等待
url = 'https://wx.mail.qq.com/login/loginpage?auth_type=3&login_exception=true'
driver.get(url)

# 隐式等待
# driver.implicitly_wait(10)

# 显示等待
# WebDriverWait 等待类 接收参数 1. 驱动对象 2. 最大等待时间 3. 多少毫秒检查一次条件
WebDriverWait(driver, 30, 0.3).until(
    # 等待元素可见
    # EC.visibility_of_element_located((By.XPATH, '//*[@id="switcher_plogin"]'))
    # 等待元素可点击
    EC.element_to_be_clickable((By.XPATH, '//*[@id="switcher_plogin"]'))

)

driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()

time.sleep(10)
driver.quit()
