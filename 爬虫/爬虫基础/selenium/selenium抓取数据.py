import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://liuyan.people.com.cn/threads/list?fid=5055&formName=%E5%B7%A5%E4%B8%9A%E5%92%8C%E4%BF%A1%E6%81%AF%E5%8C%96%E9%83%A8%E5%85%9A%E7%BB%84%E4%B9%A6%E8%AE%B0%E3%80%81%E9%83%A8%E9%95%BF%E9%87%91%E5%A3%AE%E9%BE%99&position=1'

driver.get(url)

time.sleep(5)
# 1 先定位到包含所有数据的li列表
li_list = driver.find_elements(By.XPATH, '//ul[@class="replyList"]/li')

# 2 遍历页面上所有的li标签
for item in li_list:
    title = item.find_element(By.XPATH, './div[@class="tabList fl"]/h1').text
    t = item.find_element(By.XPATH,'.//div[@class="headMainS fl"]/p').text
    content = item.find_element(By.XPATH,'./p[@class="replyContent"]/span').text

    print('标题' + title + '时间' + t + '内容' + content)


driver.quit()