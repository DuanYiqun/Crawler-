import selenium
import re
from selenium import webdriver
import urllib
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyquery import PyQuery as pq
import sys
import time
import pandas as pd

filePath = "/Users/duanyiqun/Downloads/download.jpeg"

chromedriver = "/Users/duanyiqun/anaconda3/envs/crawler/chromedriver"
browser = webdriver.Chrome(chromedriver)
outputSet = set()

OUTPUT_DIR = '/Users/duanyiqun/Downloads/testfile.txt'
repeateNum = 0
preLen = 0

def searchbylocalfile():
    try:
        PAGE_NUM =5
        browser.get('https://www.google.com/imghp?hl=en')
        wait = WebDriverWait(browser, 10)
        ele = browser.find_element_by_class_name("gsst_a")
        ele.click()
        browser.execute_script("google.qb.ti(true);return false")
        #location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_SiteNavBdL"]/li[1]')))
        #location.click()
        location = browser.find_element_by_id("qbfile")
        #location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qbfile"]')))
        #location.click()
        location.send_keys(filePath)
        location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="imagebox_bigimages"]/g-section-with-header/div[1]/h3/a')))
        location.click()
        #total_img = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="rg"]/div/div/a/img')))
        pos = 0
        m = 0 # 图片编号
        for i in range(PAGE_NUM):
            pos += i*600
            js = "document.documentElement.scrollTop=%d" % pos
            browser.execute_script(js)
            time.sleep(1)
            #browser.execute_script("arguments[0].scrollIntoView(false);", element);
            for element in browser.find_elements_by_xpath('//div[@id="rg"]/div/div/a/img'):
                img_url = element.get_attribute('src')
                if img_url is not None and img_url.startswith('http'):
                    outputSet.add(img_url)
        
        print('writing' + str(filePath) + 'image links')
        file = open(OUTPUT_DIR, 'w')
        for val in outputSet:
            file.write(val + '\n')
        file.close()
    
    except TimeoutException:
        return searchbylocalfile()

searchbylocalfile()

def searchbyurl():
    browser.get('https://www.google.com/imghp?hl=en')
    wait = WebDriverWait(browser, 10)
    ele = browser.find_element_by_class_name("gsst_a")
