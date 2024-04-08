from selenium import webdriver
import time
"""
当前url地址 current_url
页面标题 title
页面源代码 page_source
获取浏览器所有的窗口句柄 window_handler
获取当前窗口句柄 current_window_handle
"""
# 创建一个driver对象(启动浏览器)
driver = webdriver.Chrome()

# 打开一个网页
driver.get("https://www.baidu.com")

time.sleep(1)

# 窗口最大化
driver.maximize_window()

time.sleep(1)
# 刷新页面
driver.refresh()

# 获取页面源码
with open('百度.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

# 对当前页面截图
driver.save_screenshot('百度.png')

# 获取当前页面访问地址
print(driver.current_url)

# 获取页面标题
print(driver.title)

time.sleep(5)

# 退出浏览器
driver.quit()
