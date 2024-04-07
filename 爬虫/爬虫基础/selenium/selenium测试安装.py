from selenium import webdriver

# selenium打开浏览器
driver = webdriver.Chrome()
url = 'https://www.baidu.com'
driver.get(url)


input()