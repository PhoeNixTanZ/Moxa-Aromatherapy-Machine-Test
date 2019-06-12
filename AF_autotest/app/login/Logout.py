# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/4 17:25'
from app.start.start import get_driver
from app.size.get_size import get_screen
import time

def logout_app(driver,size):
    time.sleep(10)
    driver.find_element_by_android_uiautomator('new UiSelector().text("personal center-outline 个人中心")').click()
    time.sleep(5)
    x1 = 1002
    y1 = 93.9
    x2 = 1078.9
    y2 = 2158.8
    a = x1/x2
    b = y1/y2
    x = size['width']
    y = size['height']
    time.sleep(5)
    driver.tap([(a*x,b*y)])
    time.sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("确认 ")').click()
