# -*- coding:utf-8 -*-
from selenium import webdriver
import time
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
#driver = webdriver.Ie()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
driver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(3)
#driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()
driver.quit()