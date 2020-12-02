import pytest
import os
import allure
from selenium import webdriver
import time
#72投PC版
class Test_caseqq():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://192.168.0.32:9006/#')
        self.driver.implicitly_wait(5)

    # 函数级结束
    def teardown(self):
        self.driver.quit()
    #账号密码登录
    def test_1_login(self):
        login(self,'13600587905','123456789')

        assert self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/span').is_displayed()

    # 账号密码登录（失败）
    def test_2_login(self):
        '''账号密码错误'''
        login(self,'13600587905','12345678')
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div/div/p[1]').is_displayed()










#登录方法
def login(self,account,password):
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/p[2]').click()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys(account)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys(password + '\n')
    # self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
    self.driver.implicitly_wait(10)

if __name__ == '__main__':
    #生成测试报告
    pytest.main(['test_72tou.py', '-s', '--alluredir=report/allure_result'])
    os.system('allure serve report/allure_result')