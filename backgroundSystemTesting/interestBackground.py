from selenium import webdriver
import time
import os
import unittest

#权益后台测试
class interestBackground(unittest.TestCase):
    def setUp(self) -> None:#每次都会运行
        self.driver = webdriver.Chrome()
        self.driver.get('http://115.236.35.106:3502/#/')
        self.driver.implicitly_wait(5)

    #登录测试
    def test_login(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('light_admin')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
        self.driver.implicitly_wait(5)
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[1]').is_enabled())
        # if driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[1]').is_enabled():  # 元素是否激活
        #     print('登录测试--------》登录成功')
        #     return True
        # else:
        #     print('登录测试--------》登录失败')
        #     return False

    #添加活动测试
    def test_addAct(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('light_admin')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[3]/div').click()#营销工具
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[3]/ul/a[1]').click()#优惠活动
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/button[3]').click()#新建优惠活动
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[4]/div[2]/div/input').send_keys('自动化测试2')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[5]/div[2]/div/input').send_keys('100')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[7]/div[2]/div/input').send_keys('2')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[8]/div[2]/p[1]/div/input').send_keys('1')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[9]/div[2]/div/div[1]/div/input').click()#活动时间
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[9]/div[2]/div/div[2]/div/div/div[1]/div[2]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[9]/div[2]/div/div[2]/div/div/div[2]/div[4]/button[3]').click()#确认
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/div/input').send_keys('30')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[11]/div[2]/div/div[2]').click()
        self.driver.implicitly_wait(5)
        #上传图片
        os.system(r'E:\textFile\aaa.exe')

        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[14]/div[2]/div/input').send_keys('1')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[15]/div[2]/div/textarea').send_keys('会佛尔啥计算机')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[17]/button[2]').click()
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/button[3]').is_enabled())



if __name__ == '__main__':
    unittest.main()















# #登录测试
# def login():
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('admin')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('light_admin')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
#     driver.implicitly_wait(5)
#     if driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[1]').is_enabled():#元素是否激活
#         print('登录测试--------》登录成功')
#         return True
#     else:
#         print('登录测试--------》登录失败')
#         return False
#
# #创建活动测试
# def addAct():
#     # driver.implicitly_wait(5)
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[3]/div').click()#营销工具
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/li[3]/ul/a[1]').click()#优惠活动
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/button[3]').click()#新建优惠活动
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[4]/div[2]/div/input').send_keys('自动化测试2')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[5]/div[2]/div/input').send_keys('100')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[7]/div[2]/div/input').send_keys('2')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[8]/div[2]/p[1]/div/input').send_keys('1')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[9]/div[2]/div/div[1]/div/input').click()#活动时间
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[9]/div[2]/div/div[2]/div/div/div[1]/div[2]').click()
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[9]/div[2]/div/div[2]/div/div/div[2]/div[4]/button[3]').click()#确认
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[10]/div[2]/div[2]/div/input').send_keys('30')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[11]/div[2]/div/div[2]').click()
#     time.sleep(5)
#     #上传图片
#     os.system(r'E:\textFile\aaa.exe')
#
#     driver.implicitly_wait(30)
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[14]/div[2]/div/input').send_keys('1')
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[15]/div[2]/div/textarea').send_keys('会佛尔啥计算机')
#     time.sleep(3)
#     driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[17]/button[2]').click()
#     if driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/button[3]').is_enabled():
#         print('创建活动测试--------》创建成功')
#         return True
#     else:
#         print('创建活动测试--------》创建失败')
#         return False
#
# if(login()):
#     addAct()