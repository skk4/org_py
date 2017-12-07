# coding:utf-8 -*-
'''
优芽互动电影测试
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class Movi_Try(object):
    def __init__(self, driver):
        self.driver = driver

    def movi_try(self):
        url = 'http://www.yoya-dev.com/'
        #self.driver = webself.driver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        self.driver.find_element_by_xpath('//*/a[text()="登录"]').click()
        time.sleep(3)
        #切换到新弹出的网页窗口windows
        nowhandle = self.driver.current_window_handle
        #print nowhandle
        #print self.driver.title
        allhandles = self.driver.window_handles
        #print type(allhandles)
        #print allhandles
        for handle in allhandles:
            if handle != nowhandle: 
                self.driver.switch_to_window(handle)
                #print self.driver.title       
                self.driver.find_element_by_xpath('//*[@id="u_user_name"]').send_keys('xiesj')
                self.driver.find_element_by_xpath('//*[@id="u_password"]').send_keys('123456')
                self.driver.find_element_by_xpath('//*[@id="user_login"]').click()
                time.sleep(5)
                #self.driver.find_element_by_xpath('//*/span[text()="新建"]').click()
                #active 需要鼠标移动过去才能可点击
                create_button = self.driver.find_element_by_xpath('//*/a[@class="btn btn-icon-text pull-left new-moive-btn active"]')
                webdriver.ActionChains(self.driver).move_to_element(create_button).perform()
                self.driver.find_element_by_xpath('//*/i[@class="icon icon-newly-built"]').click()   
                time.sleep(15)
                allhandles = self.driver.window_handles
                self.driver.switch_to_window(allhandles[-1])
                print self.driver.title
                time.sleep(3)
                #iframe不用切换，但需层层切
                current_frame = self.driver.find_element_by_xpath('//*/iframe[contains(@id, "iframe2")]')       
                self.driver.switch_to_frame(current_frame)
                #self.driver.switch_to.frame(1)
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="movieName"]').send_keys('hellobike')
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="newMovie"]').click()
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="sc_role"]').click()
                time.sleep(3) 
                       
        #self.driver.switch_to_window(nowhandle)
        #time.sleep(3)     
        self.driver.quit() 
       
if __name__=='__main__':
    driver = webdriver.Chrome()
    test_movi_try = Movi_Try(driver)
    test_movi_try.movi_try()        
