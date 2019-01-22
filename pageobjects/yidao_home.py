#coding=utf-8
from framework.base_page import BasePage

class YiDaoHome(BasePage):
    exitlink = "xpath=>//*/div[@class='col-lg-4 col-md-4 col-xs-12 col-sm-12 text-right links pull-right']/a[2]"
    firstpagelink="link_text=>首页"
    ERPlink="xpath=>//*[contains(text(),'ERP')]"

    def enter_firstpage(self):
        self.click(self.firstpagelink)
    def enter_ERP(self):
        self.click(self.ERPlink)
    def exit(self):
        self.click(self.exitlink)