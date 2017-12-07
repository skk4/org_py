# -*- coding:utf-8 -*-
import unittest
from testsuits.yoya_test_script2 import Test_Script2
from testsuits.yoya_test_script import Test_Script
#testsuits路径下加载所有用例
#suite = unittest.TestLoader().discover("testsuits")

#一次 加载一个类下所有用例到suite
suite = unittest.TestSuite(unittest.makeSuite(Test_Script2))

'''#单个添加
suite = unittest.TestSuite()
suite.addTest(Test_Script2('test_run_movi'))
suite.addTest(Test_Script2('test_run_org'))
suite.addTest(Test_Script('test_run_movi'))
'''
if __name__=='__main__':
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
