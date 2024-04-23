import time

import pandas as pd
from selenium import webdriver
import pandas as ps
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://code.nhsa.gov.cn/jbzd/public/dataWesterSearch.html?batchNumber=https://code.nhsa.gov.cn/'

driver.get(url)
time.sleep(5)
result = driver.find_elements(By.XPATH, '//*[@id="treeDemo1"]/li/span')
for index, drvier_son in enumerate(result):
    # 点开最外层
    if index != 0:
        drvier_son.click()
    time.sleep(2)
    # 获取每一大章节中的小节
    data = drvier_son.find_elements(By.XPATH, '//*[@id="treeDemo1_' + f'{index + 1}' + '_ul"]/li/span')
    for index_2, drvier_son_2 in enumerate(data):
        time.sleep(2)
        drvier_son_2.click()
        # text = drvier_son_2.find_element(By.XPATH, './/a/span[@class="node_name"]').text
        # print(text)
        try:
            drvier_child = drvier_son.find_elements(By.XPATH, '//*[@id="treeDemo1_' + f'{index + 1}' + '_ul"]/li/ul/li')
            for child in drvier_child:
                time.sleep(2)
                child.click()
        except:
            print('没有数据')
        # print(data)
