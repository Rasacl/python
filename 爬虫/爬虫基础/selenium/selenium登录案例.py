import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://liuyan.people.com.cn/login'

driver.get(url)

time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="userInput"]/input').send_keys("17702335386")
driver.find_element(By.XPATH, '//*[@id="55"]').send_keys("@Chen991029")

driver.find_element(By.ID, 'index_logonid').click()

time.sleep(2)

driver.quit()




