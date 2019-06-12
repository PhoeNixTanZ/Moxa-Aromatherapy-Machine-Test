# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/5 15:00'

from app.start.start import get_driver
import time
import random

def reset_email(driver):
    time.sleep(8)
    driver.find_element_by_android_uiautomator('new UiSelector().text("personal center-outline 个人中心")').click()
    time.sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("忘记密码？")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号找回")').click()
    input_text = driver.find_elements_by_class_name('android.widget.EditText')
    input_text[0].send_keys('18852923055')
    button = driver.find_elements_by_class_name('android.widget.Button')
    button[1].click()
    rand_1 = 100000
    rand_2 = 111111
    verification_code = random.randint(rand_1,rand_2)
    input_text[1].send_keys(verification_code)
    button[2].click()
    input_text_n = driver.find_elements_by_class_name('android.widget.EditText')
    input_text_n[2].send_keys('123456')
    time.sleep(1)
    button[3].click()
