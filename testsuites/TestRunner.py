#coding=utf-8
import unittest
import sys
import os
import time
import HTMLTestRunner
from testsuites.TestCase import LoginFuc

reload(sys)
sys.setdefaultencoding("utf-8")

suit = unittest.TestSuite()
suit.addTest(LoginFuc('test_loginyidaohome'))
suit.addTest(LoginFuc('test_loginERP'))

if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    report_path = os.path.dirname(os.path.abspath('.')) + '/testreports/'
    currenttime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    reportfile = report_path + currenttime + 'reports.html'
    tempfile = open(reportfile, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=tempfile,title=u'ERP登录功能测试报告',description=u'测试用例执行情况')
    runner.run(suit)
    tempfile.close()
