# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/5 15:01'
import time
from app.start.start import get_driver
import random

def reset_phone(driver):
    time.sleep(8)
    driver.find_element_by_android_uiautomator('new UiSelector().text("personal center-outline 个人中心")').click()
    time.sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("忘记密码？")').click()
    time.sleep(2)
    input_text = driver.find_elements_by_class_name('android.widget.EditText')
    input_text[0].send_keys('2287329355@qq.com')
    driver.find_element_by_android_uiautomator('new UiSelector().text("获取验证码")').click()
    rand_1 = 100000
    rand_2 = 111111
    verification_code = random.randint(rand_1,rand_2)
    input_text[1].send_keys(verification_code)
    button = driver.find_elements_by_class_name('android.widget.Button')
    button[2].click()
    input_text_n = driver.find_elements_by_class_name('android.widget.EditText')
    input_text_n[2].send_keys('123456')
    driver.find_element_by_android_uiautomator('new UiSelector().text("确认")').click()
