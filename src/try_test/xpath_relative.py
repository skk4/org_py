# -*- coding:utf-8 -*-
'''
百度新闻xpath相对路径方法
'''
from selenium import webdriver
import time
url = 'http://news.baidu.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(url)
driver.find_element_by_xpath('//*[@id="ww"]').send_keys(u'互联网金融')
driver.find_element_by_xpath('//*/label[@for="newstitle"]/../input[2]').click()
driver.find_element_by_xpath('//*/input[@value="百度一下"]').click()
time.sleep(8)
driver.quit()