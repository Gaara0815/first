from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec# 引入包
class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    # 账号密码登录方法
    def login(self, account, password,needWait):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/p[2]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys(account)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys(password + '\n')
        if(needWait):#最长等待30S
            WebDriverWait(self.driver, 30).until(ec.title_is('首页'))
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[1]/div/span').is_displayed()

    # # 手机号验证码登录方法
    # def login(self, account, password,needWait):
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys(account)
    #     self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/input').send_keys(password + '\n')
    #     if(needWait):#最长等待30S
    #         WebDriverWait(self.driver, 30).until(ec.title_is('首页'))