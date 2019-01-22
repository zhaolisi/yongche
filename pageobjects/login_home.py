#coding=utf-8
from framework.base_page import BasePage

class LoginPage(BasePage):
    usernameinputbox = 'id=>J_login'
    passwordinputbox = 'id=>J_pwd'
    submitbtn = 'id=>id_submit'

    def username_input(self,username):
        self.type(self.usernameinputbox,username)
    def password_input(self,password):
        self.type(self.passwordinputbox,password)
    def submit_btn(self):
        self.click(self.submitbtn)