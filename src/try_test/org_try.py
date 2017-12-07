# coding:utf-8 -*-
'''
优芽机构测试
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def org_try(driver):
    url = 'http://school.yoya-dev.com'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(url)
    #通过节点元素属性定位元素@，登录
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('xiesj')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="login_button"]').click()
    time.sleep(3)
    #通过contains(@, '')定位元素，切换到课程菜单
    driver.find_element_by_xpath('//*/a[contains(@href, "start=courses")]').click()
    #通过text()定位元素
    #driver.find_element_by_xpath('//*/span[text()="课程管理"]').click()
    time.sleep(3)
    #创建课程
    driver.find_element_by_xpath('//*[@id="add_course"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@name="course_name"]').send_keys(u'小学二年级数学')
    driver.find_element_by_xpath('//*[@id="btn_next"]').click()
    time.sleep(3)
    #完成
    driver.find_element_by_xpath('//*[@id="btn_finish"]').click()
    time.sleep(3)
    #driver.find_element_by_xpath('//*/a[@title="小学一年级数学"]/../../../div[@class="title"]//*[@name="select"]').click()
    #time.sleep(3)
    #通过定位小学二年级数学元素，../../找到共同的父节点，然后再往下找需要的元素
    driver.find_element_by_xpath('//*/a[@title="小学二年级数学"]/../../../div[@class="opts"]/a[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*/h2[@class="p-title"]/a[text()="课程管理"]').click()
    time.sleep(3)
    #鼠标移动动作ActionChains()，移动到下拉button
    course_menu = driver.find_element_by_xpath('//*/a[@title="小学二年级数学"]/../../../div[@class="title"]//*[@name="select"]')
    webdriver.ActionChains(driver).move_to_element(course_menu).perform()
    time.sleep(3)
    #删除课程
    driver.find_element_by_xpath('//*/a[@title="小学二年级数学"]/../../../div[@class="title"]//*[@name="select"]/div/a[@name="btn_del"]').click()
    time.sleep(3)
    #确定课程
    driver.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()
    '''网页对话框操作
    alter = driver.switch_to_alert()
    time.sleep(3)
    print alter.text
    alter.accept()
    '''
    time.sleep(3)
    driver.quit()
