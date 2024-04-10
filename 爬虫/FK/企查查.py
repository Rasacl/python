import pprint
import random
import re
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# 登陆 需要自己扫码
def login():
    driver.find_element(By.CLASS_NAME, 'login-nav-btn').click()  # 点击登录
    driver.implicitly_wait(100)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="activity-modal"]//*[@ class="close"]').click()


# 打开搜索以页面
def get_search_page():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="searchKey"]').send_keys('重庆格林医院有限公司')
    driver.find_element(By.XPATH, '//*[@class="input-group-btn"]//*[@class="btn btn-primary"]').click()
    driver.implicitly_wait(20)
    aEle = driver.find_element(By.XPATH, '//*[@class="copy-title"]/a')
    href = aEle.get_attribute('href')
    driver.get(href)


def search_key_list():
    time.sleep(2)
    business_info_list = []
    register_info_list = []
    basic_info_list = []
    hospital_list = pd.read_excel('三级医院爬取目录.xlsx')
    hospital_list = hospital_list['医疗机构名称'].tolist()
    a = ['泰州姜堰华大医院', "重庆格林医院有限公司", "徐州矿务集团总医院徐州医学院第二附属医院"]
    for key in hospital_list:
        info = search_key_info(key)
        if info:
            if info['类型'] == '工商信息':
                business_info_list.append(info)
            elif info['类型'] == '登记信息':
                register_info_list.append(info)
            else:
                basic_info_list.append(info)
    return business_info_list, register_info_list, basic_info_list


def search_key_info(keywords):
    print(keywords, '搜索关键词')
    search_input = driver.find_element(By.XPATH,
                                       '//input[@placeholder="请输入企业名、人名、产品名，或地址电话/经营范围等"]')
    search_input.clear()
    search_input.send_keys(keywords)
    time.sleep(2)
    try:
        element = driver.find_elements(By.XPATH, '//*[@class="col-wrap"]')[0]
    except:
        element = driver.find_element(By.XPATH, '//*[@class="col-wrap"]')

    sub_elements = element.find_elements(By.XPATH, './/*[@class="list-group-item keyMoveItem"]')[0]
    sub_elements.click()
    time.sleep(1)
    random_scroll()  # 随机滑动页面
    try:
        titleEle = driver.find_element(By.XPATH,
                                       '//*[@class="cominfo-section data-section"]//*[@class="title-container"]/span')
        if titleEle and titleEle.text == '工商信息':
            print('工商信息查询成功')
            return get_info()
        elif titleEle and titleEle.text == '基本信息':
            return {
                "类型": '基本信息',
                "企业名称": keywords,
                "社会组织类型": '-',
                "登记管理机关": '-',
                "所属地区": '-',
                "住所": '-'
            }
    except:
        try:
            registerEle = driver.find_element(By.XPATH,
                                              '//*[@class="data-tabs container"]//*[@class="data-section"]//*[@class="title-container"]/span')
            if registerEle and registerEle.text == '登记信息':
                print('登记信息查询成功')
                return get_rgeister_info(keywords)
            elif registerEle and registerEle.text == '基本信息':
                return {
                    "类型": '基本信息',
                    "企业名称": keywords,
                    "社会组织类型": '-',
                    "登记管理机关": '-',
                    "所属地区": '-',
                    "住所": '-'
                }
        except:
            pass


def get_info():
    name = driver.find_elements(By.XPATH,
                                '//*[@class="cominfo-section data-section"]//*[@class="app-copy-box copy-hover-item"]//*[@class="copy-value"]')[
        1].text
    elements = driver.find_elements(By.XPATH, '//*[@class="cominfo-section data-section"]//*[@class="tb"]')
    types = elements[10].find_element(By.XPATH, 'following-sibling::*[1]').text
    registration = driver.find_elements(By.XPATH,
                                        '//*[@class="cominfo-section data-section"]//*[@class="app-copy-box copy-hover-item"]//*[@class="copy-value"]')[
        7].text
    address = driver.find_element(By.XPATH,
                                  '//*[@class="cominfo-section data-section"]//*[@class="text-dk copy-value"]').text
    info = {
        "类型": '工商信息',
        "企业名称": name,
        "企业类型": types,
        "登记机关": registration,
        "注册地址": address
    }
    print(info, "工商信息")
    return info


def get_rgeister_info(keywords):
    elements = driver.find_elements(By.XPATH, '//*[@class="ntable"]//*[@class="tb"]')
    types = elements[5].find_element(By.XPATH, 'following-sibling::*[1]').text
    registration = elements[7].find_element(By.XPATH, 'following-sibling::*[1]').text
    belong = driver.find_elements(By.XPATH,
                                  '//*[@class="ntable"]//*[@class="app-copy-box copy-hover-item"]//*[@class="copy-value"]')[
        1].text
    address = driver.find_element(By.XPATH,
                                  '//*[@class="ntable"]//*[@class="app-copy-box copy-hover-item"]//*[@class="copy-value text-dk"]').text
    info = {
        "类型": '登记信息',
        "企业名称": keywords,
        "社会组织类型": types,
        "登记管理机关": registration,
        "所属地区": belong,
        "住所": address
    }

    print(info, "登记信息")
    return info


# 随机延时
def random_sleep(min_seconds, max_seconds):
    time.sleep(random.randint(min_seconds, max_seconds))


# 随机滑动页面
def random_scroll():
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {random.randint(0, scroll_height)})")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://www.qcc.com/'
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    login()
    get_search_page()
    business_info_list, register_info_list, basic_info_list = search_key_list()
    combined_list = business_info_list + register_info_list + basic_info_list
    print(combined_list, '合并')
    time.sleep(10)
    driver.quit()
