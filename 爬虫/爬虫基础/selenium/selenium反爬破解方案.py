import time

from selenium import webdriver

url = 'https://www.creditchina.gov.cn/'
opt = webdriver.ChromeOptions()
# 添加防检测的参数

opt.add_argument('--disable-infobars')  # 禁用信息栏
opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 不使用扩展程序
opt.add_experimental_option('useAutomationExtension', False)  # 禁用自动化
driver = webdriver.Chrome(options=opt)

# 在每次打开页面之前，执行该脚本 去除selenium浏览器生成的相关属性
with open('stealth.min.js') as f:
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': f.read()})
driver.get(url)

time.sleep(10)
driver.quit()
