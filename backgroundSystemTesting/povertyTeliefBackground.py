from selenium import webdriver
import time
import os
import unittest

#权益后台测试
class interestBackground(unittest.TestCase):
    def setUp(self) -> None:#每次都会运行
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.0.214:10030/#/')
        self.driver.implicitly_wait(5)

    # 管理员登录测试
    def test_1_login(self):
        print('test_1_login')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('admin')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
        self.driver.implicitly_wait(5)
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[1]').is_enabled())


    #基地账号登录测试
    def test_2_login(self):
        print('test_2_login')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('test1')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('123')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
        self.driver.implicitly_wait(5)
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[1]').is_enabled())


    # 添加分类测试
    # def test_3_addAct(self):
    #     print('test_3_addAct')
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('admin')
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('admin')
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[2]').click()#商品分类
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/button/span').click()#添加分类
    #     self.driver.implicitly_wait(3)
    #
    #     self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/a').click()
    #     self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/input').send_keys('自动化测试')#新建优惠活动
    #     self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div').click()
    #     # menu_table = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/table')
    #     # rows = menu_table.find_elements_by_tag_name('tr')
    #     # # python 得len()函数返回对象（字符、列表、元组）得长度或者元素得个数
    #     # before_add_numbers = len(rows)
    #     # print(before_add_numbers)
    #
    #     self.driver.implicitly_wait(5)
    #     # 上传图片
    #     os.system(r'E:\\a.exe')
    #     self.driver.implicitly_wait(10)
    #     # self.assertTrue(self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div/img').is_enabled())
    #     # self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]').click()  # 确定
    #
    #     # now_table = self.driver.find_element_by_xpath(
    #     #     '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/table')
    #     # now_rows = menu_table.find_elements_by_tag_name('tr')
    #     # # python 得len()函数返回对象（字符、列表、元组）得长度或者元素得个数
    #     # now_numbers = len(now_rows)
    #     # self.assertTrue(now_numbers>before_add_numbers)

    #团购活动创建测试
    # def test_4_addGroupon(self):
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('admin')
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('admin')
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
    #
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/div/ul/a[7]').click()
    #     # 窗口最大化
    #     self.driver.maximize_window()
    #     # 获取第一个窗口的句柄
    #     first_windows = self.driver.current_window_handle
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/input').send_keys('13600587905')
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/button[1]').click()
    #     # 获取当前所有打开窗口的句柄
    #     all_handles = self.driver.window_handles
    #     # 进入创建窗口
    #     for newhandle in all_handles:
    #         if newhandle != first_windows:
    #             self.driver.switch_to.window(newhandle)
    #             self.driver.implicitly_wait(5)
    #             #顶部
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/input').send_keys("团购创建测试")
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/input').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/span[20]/em').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[4]/button[3]').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/input').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/span[31]/em').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/div/div[4]/button[3]').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/i').click()
    #             time.sleep(3)
    #             # 上传图片
    #             os.system(r'E:\\a.exe')
    #             self.driver.implicitly_wait(10)
    #
    #             #商品
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/input').send_keys('商品1')
    #             self.driver.find_element_by_xpath(
    #                 '//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[4]/div/div/div/div/div/i').click()
    #             time.sleep(3)
    #             # 上传图片
    #             os.system(r'E:\\a.exe')
    #             self.driver.implicitly_wait(10)
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[3]/div[1]/button').click()
    #             self.driver.implicitly_wait(5)
    #             self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[1]/p[2]/button').click()
    #             self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[1]/p[1]/div/input').send_keys("规格1")
    #             self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[1]/p[3]/span[1]/div/input').send_keys("规格值1")
    #             self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div[1]/p[3]/span[2]/div/input').send_keys("规格值2")
    #             self.driver.find_element_by_xpath('//*[@id="skuBox"]/div[2]/p[4]/div/div[2]/input').send_keys("100")
    #             self.driver.find_element_by_xpath('//*[@id="skuBox"]/div[2]/p[5]/div/div[2]/input').send_keys("0.01")
    #             self.driver.find_element_by_xpath('//*[@id="skuBox"]/div[3]/p[4]/div/div[2]/input').send_keys("200")
    #             self.driver.find_element_by_xpath('//*[@id="skuBox"]/div[3]/p[5]/div/div[2]/input').send_keys("0.02")
    #             self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]').click()
    #             self.driver.implicitly_wait(10)
    #
    #             #底部
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[6]/div/div/div[1]/div/span[2]').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[6]/div/div/div[2]/ul[2]/li[1]').click()
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[7]/div/div/textarea').send_keys("活动描述活动描述活动描述活动描述活动描述")
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[11]/div/button[2]').click()
    #             self.driver.implicitly_wait(10)
    #     for newhandle in all_handles:
    #         if newhandle == first_windows:
    #             self.driver.switch_to.window(newhandle)
    #             self.driver.implicitly_wait(5)
    #             self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/button[2]').click()
    #             self.driver.implicitly_wait(5)
    #             kk = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span').text;
    #             self.assertTrue(kk == '团购创建测试')

    def tearDown(self) -> None:
        print('tearDown')


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