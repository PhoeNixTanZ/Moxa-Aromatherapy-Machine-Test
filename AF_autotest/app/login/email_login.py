# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/4 14:26'
# import sys
# sys.path.append('E:/AF_autotest')
from app.start.start import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from util.read_init import ReadIni
from util.get_by_local import GetBylocal


def login_by_email(driver):
    # driver = get_driver()
    time.sleep(10)
    get_by_local = GetBylocal(driver)
    get_by_local.get_element('user_center','app_buttom').click()
    time.sleep(1)
    email_input = driver.find_elements_by_class_name('android.widget.EditText')
    email_input[0].send_keys('2287329355@qq.com')
    email_input[1].send_keys('123456')
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("登录")').click()
    tost = ("xpath","//*[contains(@text,'登录成功')]")
    WebDriverWait(driver,2,0.1).until(EC.presence_of_element_located(tost))
if __name__ == '__main__':
    d = get_driver()
    login_by_email(d)