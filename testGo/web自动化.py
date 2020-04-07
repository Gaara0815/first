from selenium import webdriver
import unittest

# class StringReplaceTestCase1(unittest.TestCase):
#     def runTest(self):
#         source = 'selenium'
#         expect = 'se*le*nium'
#         result = source.replace("*","")
#         self.assertEqual(expect,result)

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)#智能等待
kwdselectid = driver.find_element_by_id('kw')
kwdselectid.send_keys('python')

driver.find_element_by_id('su').click()

