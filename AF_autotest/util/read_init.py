# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/10 21:25'
import configparser

class ReadIni(object):
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'E:/AF_autotest/config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path,encoding='UTF-8')
        return read_ini
    # 通过key获取对应的value
    def get_value(self,key,node=None):
        if node == None:
            node = 'login_elements'
        # 异常处理：节点错误时，返回None
        try:
            value = self.data.get(node,key)
            return value
        except:
            value = None
            return value
if __name__ == '__main__':
    r = ReadIni()
    print(r.get_value('course','course_element'))