# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/11 1:20'
from handle.login_handle import LoginHandle
from app.start.start import get_driver
import time

class LoginBusiness(object):
    def __init__(self,driver):
        self.login_handle = LoginHandle(driver)

    def login_pass(self):
        time.sleep(30)
        self.login_handle.send_username('2287329355@qq.com')
        self.login_handle.send_password('123456')
        self.login_handle.click_login()

    def login_user_error(self):
        self.login_handle.send_username('')
        self.login_handle.send_password('123456')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_tost("请输入邮箱")
        if user_flag:
            return True
        else:
            return False

if __name__ == '__main__':
    d = get_driver()
    dw = LoginBusiness(d)
    dw.login_pass()