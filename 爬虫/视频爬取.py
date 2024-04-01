import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# 初始化浏览器为chrome浏览器
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 禁用沙盒模式
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)


def open_target_browser():
    ''''
    初始化浏览器
    '''
    # 目标网址
    url = r'https://study.thingjs.com/course/detail/course-internal/159/3602'

    # 打开网址
    browser.get(url)

    time.sleep(2)
    # 根据CSS类名获取元素并点击
    login_btn = browser.find_element(By.CSS_SELECTOR, '.login_btn__sboiv')
    login_btn.click()
    time.sleep(2)
    # 根据CSS类名获取input元素并输入内容
    input_element = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/ul/li[1]/input')
    input_element.send_keys('17702335386')

    input_element = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/ul/li[2]/input')
    input_element.send_keys('@Chen991029')

    label_element = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[3]/form/div[2]/label')
    label_element.click()

    loginBtn = browser.find_element(By.CSS_SELECTOR, '.submitBtn')
    loginBtn.click()

    time.sleep(7)

def get_m3u8_list():
    blob_url = 'https://study.thingjs.com/course/detail/course-internal/159/3602'
    # 使用JavaScript来读取blob数据并转换为Base64编码的字符串
    blob_to_base64 = """  
      function(blobUrl) {  
          return new Promise((resolve, reject) => {  
              const xhr = new XMLHttpRequest();  
              xhr.open('GET', blobUrl, true);  
              xhr.responseType = 'blob';  
              xhr.onload = function() {  
                  if (this.status === 200) {  
                      const reader = new FileReader();  
                      reader.readAsDataURL(this.response);  
                      reader.onloadend = function() {  
                          resolve(reader.result);  
                      }  
                  } else {  
                      reject(new Error('XHR failed with status ' + this.status));  
                  }  
              };  
              xhr.send();  
          });  
      }  
      """
    # 转换blob_url_to_base64函数为Python可以执行的函数
    blob_to_base64_func = browser.execute_script(blob_to_base64)

    # 执行转换并获取结果
    base64_data = blob_to_base64_func(blob_url)
    print(base64_data)



if __name__ == '__main__':
    open_target_browser()
    get_m3u8_list()
    input()
