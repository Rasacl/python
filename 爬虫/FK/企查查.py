import time

import pandas as pd
from selenium import webdriver
import pandas as ps
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://www.qcc.com/'

# hospital_list = pd.read_excel(r'D:\PycharmProjects\pythonProject\企查查经营性质\三级医院爬取目录.xlsx')
# hospital_list = hospital_list['医疗机构名称'].tolist()
driver.get(url)
time.sleep(2)

driver.find_element(By.CLASS_NAME,'login-nav-btn').click()


wait = WebDriverWait(driver, 10)


element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginModal"]/div/div/div/div[3]')))

element.click()



# driver.find_element(By.XPATH,'//*[@id="loginModal"]/div/div/div/div[3]').click()

# driver.find_element(By.ID, 'searchKey').send_keys(hospital_list[0])
# driver.find_element(By.CLASS_NAME,'input-group-btn').click()

# print(hospital_list)
input('modeng')