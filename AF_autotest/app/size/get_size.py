# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/4 14:16'

from app.start.start import get_driver

# 获取屏幕宽高
def get_screen(driver):
    size = driver.get_window_size()
    return size
