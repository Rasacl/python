# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# from selenium_stealth import stealth
#
# # 初始化浏览器选项
# options = Options()
# options.add_argument('--no-sandbox')  # 禁用沙盒模式
# options.add_argument('--disable-dev-shm-usage')  # 禁用/dev/shm的使用
#
# # 应用stealth插件的伪装设置
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
# options.add_argument(f'user-agent={user_agent}')
#
# # 初始化浏览器
# browser = webdriver.Chrome(options=options)
#
# # 使用stealth函数
# stealth(browser,
#         languages=["en-US", "en"],
#         webgl=False,
#         vendor="Google Inc.",
#         platform="Win32",
#         # 可以添加更多伪装设置...
#         )
#
# # 目标网址
# url = 'https://ybj.ahzwfw.gov.cn/hsa-pss/hallEnter/?authCode=3becc4c4-aa9b-4ed1-9428-dea386bcd32d#/search/MedicalTreatment'
#
# # 打开网址
# browser.get(url)
#
# time.sleep(2)
# input()
import base64

print(base64.b64decode('66C4C7BFBC5A59861DA6E15154A03180C9C946E9884F4259A707EBF463EBDAD619CB83F92B65EBDB5565333392C950B3AB6B4BAC3052A9AF6F8A3A42397954D7EE96CEFC5B5F63BC6EDF933E2298BFA758FE93DD77EE3127AA35581F52AA8B7BCA6030B9DF502C00B132DACA8188DC60F90C6476961CC38D81F7F844F0E0838C6A3553045B29364481309B6D66E93FEB'.encode()).decode())