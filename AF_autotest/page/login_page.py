# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/10 23:51'
from util.get_by_local import GetBylocal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(object):
    # 获取登录页面所有的页面元素信息
    def __init__(self,driver):
        self.get_by_local = GetBylocal(driver)

    # 获取用户名元素信息
    def get_username_element(self):
        input_elements_username = self.get_by_local.get_element('username','login_elements')
        return input_elements_username[0]

    # 获取用户密码元素信息
    def get_password_element(self):
        input_element_password = self.get_by_local.get_element('password','login_elements')
        return input_element_password[1]

    # 获取登录按钮元素信息
    def get_login_button_element(self):
        return self.get_by_local.get_element('login_button','login_elements')

    # 获取明密文切换元素信息
    def get_ciphertext_button_element(self):
        button_cip = self.get_by_local.get_element('ciphertext_button','login_elements')
        return button_cip[2]

    # 获取登录方式按钮元素信息
    def get_login_style_button_element(self):
        return self.get_by_local.get_element('login_style_button','login_elements')

    # 获取忘记密码按钮元素信息
    def get_forget_password_button(self):
        return self.get_by_local.get_element('forget_password','login_elements')

    # 获取tost元素信息;message = "'string'"
    def get_tost_element(self,message):
        tost = ("xpath","//*[contains(@text,"+message+")]")
        return WebDriverWait(self.get_by_local, 2, 0.1).until(EC.presence_of_element_located(tost))