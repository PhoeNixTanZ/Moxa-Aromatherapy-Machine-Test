# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/4 14:26'
import time
from app.start.start import get_driver
def login_by_phone(driver):
    # driver = get_driver()
    time.sleep(10)
    driver.find_element_by_android_uiautomator('new UiSelector().text("personal center-outline 个人中心")').click()
    time.sleep(2)
    driver.find_element_by_xpath('//android.view.View[contains(@index,4)]').click()
    phone_input = driver.find_elements_by_class_name('android.widget.EditText')
    phone_input[0].send_keys('18852923055')
    phone_input[1].send_keys('123456')
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button").text("登录")').click()
