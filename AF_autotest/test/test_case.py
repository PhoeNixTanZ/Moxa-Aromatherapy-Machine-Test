# _*_ coding:utf-8 _*_
__author__ = 'Tanz'
__date__ = '2019/6/11 18:36'
import unittest
import HTMLTestRunner
import requests
class AfTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setUpClass')

    # @unittest.skip('test_01')
    def test_01(self):
        url = 'http://chiyang.cheergoal.com/sys/sysUser/login'
        data = {
            'appKey': 'sasasasasasadad',
            'data': {
                'username': 'cyadmin',
                'password': '123456'
            },
            'version': '1.0'
        }
        r = requests.post(url=url, json=data)
        r = r.json()
        r = r['message']
        self.assertIn('success', r, '接口测试失败')
    def test_02(self):
        a = 1
        self.assertEqual(a,2)
    @classmethod
    def tearDownClass(cls):
        print('12')

if __name__ == '__main__':
    # unittest.main()
    html_file = 'E:/AF_autotest/report/report.html'
    fp = open(html_file,'wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告')
    suite = unittest.TestSuite()
    suite.addTest(AfTest('test_01'))
    suite.addTest(AfTest('test_02'))
    # unittest.TextTestRunner().run(suite)
    report.run(suite)