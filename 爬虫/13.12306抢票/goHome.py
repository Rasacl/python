import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from password import account, Password
# ...

def get_train(num, from_station, to_station, date):
    driver = webdriver.Chrome()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})

    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '#J-userName'))
        )
    except:
        print("元素未找到")
    finally:
        driver.quit()
    driver.find_element(By.ID, '#J-userName').send_keys(account)  # 输入账号
    driver.find_element(By.ID, '#J-password').send_keys(Password)  # 输入密码
    driver.find_element(By.ID, '#J-login').click()  # 点击登陆
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, '.modal-ft .btn ').click()
    driver.find_element(By.ID, '#link_for_ticket').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, '#fromStationText').send_keys(Keys.ENTER)
    driver.find_element(By.ID, '#fromStationText').clear()
    driver.find_element(By.ID, '#fromStationText').click()
    driver.find_element(By.ID, '#fromStationText').send_keys(from_station)
    driver.find_element(By.ID, '#fromStationText').send_keys(Keys.ENTER)
    driver.find_element(By.ID, '#toStationText').clear()
    driver.find_element(By.ID, '#toStationText').click()
    driver.find_element(By.ID, '#toStationText').send_keys(to_station)
    driver.find_element(By.ID, '#toStationText').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.ID, '#train_date').clear()
    driver.find_element(By.ID, '#train_date').click()
    driver.find_element(By.ID, '#train_date').send_keys(date)
    driver.find_element(By.ID, '#train_date').send_keys(Keys.ENTER)
    driver.find_element(By.ID, '#query_ticket').click()
    if num % 2 == 0:
        driver.find_element(By.ID, f'#queryLeftTable tr:nth-child({num + 1}) .btn72').click()
    else:
        driver.find_element(By.ID, f'#queryLeftTable tr:nth-child({num}) .btn72').click()
    driver.find_element(By.ID, '#normalPassenger_0').click()
    driver.find_element(By.ID, '#submitOrder_id').click()
    driver.find_element(By.ID, '#erdeng1 > ul:nth-child(4) li:nth-child(2) a').click()
