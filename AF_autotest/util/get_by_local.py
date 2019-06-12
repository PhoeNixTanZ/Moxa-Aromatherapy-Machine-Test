# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/10 23:06'
from util.read_init import ReadIni
from app.start.start import get_driver
class GetBylocal(object):
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key,node=None):
        #uiautomator>new UiSelector().text("personal center-outline 个人中心")
        read_ini = ReadIni()
        node = node
        local = read_ini.get_value(key,node)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            if by == 'uiautomator':
                return self.driver.find_element_by_android_uiautomator(local_by)
            elif by == 'element_by_className':
                return self.driver.find_element_by_class_name(local_by)
            elif by == 'elements_by_className':
                return self.driver.find_elements_by_class_name(local_by)
            elif by == 'element_by_xpath':
                return self.driver.find_element_by_xpath(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None