import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# hospital_list = pd.read_excel(r'D:\pythonProject\pythonProject\piChaCha\三级医院爬取目录.xlsx')
# hospital_list = hospital_list['医疗机构名称'].tolist()

# driver.find_element(By.XPATH,'//*[@id="loginModal"]/div/div/div/div[3]').click()

# driver.find_element(By.ID, 'searchKey').send_keys(hospital_list[0])
# driver.find_element(By.CLASS_NAME,'input-group-btn').click()

# print(hospital_list)



def login():
    driver.find_element(By.CLASS_NAME, 'login-nav-btn').click()  # 点击登录
    driver.implicitly_wait(100)
    driver.find_element(By.XPATH, '//*[@class="activity-modal"]//*[@ class="close"]').click()

    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="login-change"]'))).click()  # 点击其他方式登录
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="login-tab"][2]'))).click()  # 点击用户名密码登录
    #
    # # 等待输入框可见并且可交互
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="请输入手机号码/用户名"]'))).send_keys('15304038874')
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="请输入密码"]'))).send_keys('chen991029')
    #
    # driver.implicitly_wait(10)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="password-login_wrapper"]//*[@class="btn btn-primary login-btn"]'))).click()  # 点击登录

def search_key():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="searchKey"]').send_keys('重庆格林医院有限公司')
    driver.find_element(By.XPATH, '//*[@class="input-group-btn"]//*[@class="btn btn-primary"]').click()
    driver.implicitly_wait(20)
    aEle = driver.find_element(By.XPATH, '//*[@class="copy-title"]/a')
    href = aEle.get_attribute('href')
    # 根据链接打开新的网页
    driver.get(href)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://www.qcc.com/'
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    login()
    # Captcha()
    search_key()
    input()
    time.sleep(10)
    driver.quit()
