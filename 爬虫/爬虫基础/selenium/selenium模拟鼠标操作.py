import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

url = 'https://www.runoob.com/try/try.php?filename=tryhtml5_draganddrop2'

driver.get(url)
# 设置隐式等待，最大等待时间为10秒
driver.implicitly_wait(10)

# 切换iframe
driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))

# 创建一个鼠标操作对象
ac = ActionChains(driver, 3000)
# 将鼠标移动到某个元素上
ac.move_to_element(driver.find_element(By.ID,'drag1'))
# 按下鼠标
ac.click_and_hold()
# 移动到另一个元素上
ac.move_to_element(driver.find_element(By.ID,'div2'))
# 释放鼠标
ac.release()
# 执行动作
ac.perform()

time.sleep(5)
driver.quit()