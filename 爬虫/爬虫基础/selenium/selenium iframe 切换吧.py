
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

# 切换到要操作的iframe中
driver.switch_to.frame(1)
driver.switch_to.frame('ptlogin_iframe')
'''
driver.switch_to.default_content()  # 切换到默认的HTML页面中
driver.switch_to.parent_frame()  # 切换到父级的iframe中
'''
# 点击密码登录
driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()
driver.find_element(By.ID, 'u').send_keys('32E4342342@qq.com')
driver.find_element(By.ID, 'p').send_keys('112234324')
driver.find_element(By.ID, 'login_button').click()


time.sleep(10)
driver.quit()
