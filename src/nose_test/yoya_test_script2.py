# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from try_test import movi_try2
from try_test import org_try


class Test_Script2(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
 
    #一定要以test开头
    def test_run_movi(self):
        movi_try2.movi_try(self.driver)
        
        
    def test_run_org(self):
        org_try.org_try(self.driver)    

       
    def tearDown(self):
        self.driver.quit()    
        
if __name__=='__main__' :
    unittest.main()       