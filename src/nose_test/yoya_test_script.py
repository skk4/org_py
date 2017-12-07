# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from try_test import movi_try
import time

class Test_Script(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
       
    def test_run_movi(self):
        '''
                    类
        '''
        mm = movi_try.Movi_Try(self.driver)
        mm.movi_try()        
        
    def tearDown(self):
        self.driver.quit()    
        
if __name__=='__main__' :
    unittest.main()       