# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/4 11:46'
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_driver():
    # 设置配置文件
    capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "emulator-5554",
            "app": "C:\\Users\\14329\\Desktop\\app-debug.apk",
            "noReset": "true"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
    return driver

