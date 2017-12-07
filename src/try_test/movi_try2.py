# coding:utf-8 -*-
'''
优芽互动电影测试
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def movi_try(driver):
    url = 'http://www.yoya-dev.com/'
    #driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(5)
    driver.get(url)
    driver.find_element_by_xpath('//*/a[text()="登录"]').click()
    time.sleep(5)
    #切换到新弹出的网页窗口windows
    nowhandle = driver.current_window_handle
    #print nowhandle
    #print driver.title
    allhandles = driver.window_handles
    #print type(allhandles)
    #print allhandles
    for handle in allhandles:
        if handle != nowhandle: 
            driver.switch_to_window(handle)
            #print driver.title       
            driver.find_element_by_xpath('//*[@id="u_user_name"]').send_keys('xiesj')
            driver.find_element_by_xpath('//*[@id="u_password"]').send_keys('123456')
            driver.find_element_by_xpath('//*[@id="user_login"]').click()
            time.sleep(5)
            #driver.find_element_by_xpath('//*/span[text()="新建"]').click()
            #active 需要鼠标移动过去才能可点击
            create_button = driver.find_element_by_xpath('//*/a[@class="btn btn-icon-text pull-left new-moive-btn active"]')
            webdriver.ActionChains(driver).move_to_element(create_button).perform()
            driver.find_element_by_xpath('//*/i[@class="icon icon-newly-built"]').click()   
            time.sleep(15)
            allhandles = driver.window_handles
            driver.switch_to_window(allhandles[-1])
            print driver.title
            time.sleep(3)
            #iframe不用切换，但需层层切
            current_frame = driver.find_element_by_xpath('//*/iframe[contains(@id, "iframe2")]')       
            driver.switch_to_frame(current_frame)
            #driver.switch_to.frame(1)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="movieName"]').send_keys('hellobike')
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="newMovie"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="sc_role"]').click()
            time.sleep(3) 
                   
    #driver.switch_to_window(nowhandle)
    #time.sleep(3)     
    driver.quit() 
       
if __name__=='__main__':
    driver = webdriver.Chrome()
    movi_try(driver)
