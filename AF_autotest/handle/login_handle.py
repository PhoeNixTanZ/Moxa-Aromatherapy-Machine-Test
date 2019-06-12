# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/11 0:57'
from page.login_page import LoginPage


class LoginHandle(object):
    # 操作登录页面元素
    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    # 输入用户名
    def send_username(self,user):
        self.login_page.get_username_element().send_keys(user)

    # 输入用户密码
    def send_password(self,password):
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        self.login_page.get_login_button_element().click()

    def click_ciphertext(self):
        self.login_page.get_ciphertext_button_element().click()

    def click_forget_password(self):
        self.login_page.get_forget_password_button().click()

    # 获取tost,根据返回信息进行返回数据
    def get_tost(self,message):
        tost_element = self.login_page.get_tost_element(message)
        if tost_element:
            return True
        else:
            return False
