#coding=utf-8
import unittest
import os
import json
from framework.base_page import BasePage
from framework.browser_engine import BrowserEngine
from pageobjects.login_home import LoginPage
from pageobjects.yidao_home import YiDaoHome

class LoginFuc(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
    @classmethod
    def tearDown(self):
        browser = BrowserEngine(self)
        browser.quit_browser()
        self.driver.quit()
    def test_loginyidaohome(self):
        user = LoginPage(self.driver)
        exituser = YiDaoHome(self.driver)
        testdatapath = os.path.dirname(os.path.abspath('.')) + '/testdata/users.json'
        with open(testdatapath, 'r') as file:
            f = file.read().decode('utf-8-sig')
            temp = json.loads(f)
        for tester in temp.values():
            user.username_input(tester['username'])
            BasePage.sleep(1)
            user.password_input(tester['password'])
            BasePage.sleep(1)
            user.submit_btn()
            currenturl = user.get_page_url()
            print currenturl
            if currenturl == 'https://sso.yongche.org/my/securecenter':
                exituser.exit()
                BasePage.sleep(1)
                user.clear(user.usernameinputbox)
                BasePage.sleep(1)
                user.clear(user.passwordinputbox)
                BasePage.sleep(1)
            else:
                user.clear(user.usernameinputbox)
                BasePage.sleep(1)
                user.clear(user.passwordinputbox)
                BasePage.sleep(1)
            try:
                assert currenturl == 'https://sso.yongche.org/my/securecenter'
                print ('Test Pass')
            except Exception as e:
                print ('Test Fail',format(e))

    def test_loginERP(self):
        user = LoginPage(self.driver)
        user.username_input('zhaolisi')
        user.password_input('Zls@8891')
        user.submit_btn()
        loginuser = YiDaoHome(self.driver)
        BasePage.sleep(1)
        loginuser.enter_firstpage()
        BasePage.sleep(1)
        loginuser.enter_ERP()
        BasePage.sleep(1)
        currentwinhandler = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != currentwinhandler:
                self.driver.switch_to.window(handle)
        currenturl = user.get_currentpageurl()
        try:
            assert currenturl == 'https://testing.be.yongche.org/'
            print ('Test Pass')
        except Exception as e:
            print ('Test Fail', format(e))


if __name__ == '__main__':
    unittest.main()


