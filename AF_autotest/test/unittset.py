# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/4 15:59'
from app.start.start import get_driver
from app.login.email_login import login_by_email
from app.login.phone_login import login_by_phone
from app.login.Logout import logout_app
from app.size.get_size import get_screen
import unittest
import random

class AutoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        rand = random.randint(0,1)
        if rand == 0:
            login_by_email(cls.driver)
        else:
            login_by_phone(cls.driver)
        print("---->测试开始")

    @classmethod
    def tearDownClass(cls):
        d = get_driver()
        logout_app(d, get_screen(d))
        print("---->测试结束")

    # app登录_邮箱登录
    # @unittest.skip
    def test_01(cls):
        print('第一条测试')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(AutoTest('test_01'))
    suite.addTest(AutoTest('test_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)