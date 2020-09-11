from Page72tou.pageBase import Page
from selenium import webdriver
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
#登录页
class LoginPage(Page):
    def __init__(self, driver):
        self.driver = driver

#首页
class IndexPage(Page):
    def __init__(self, driver):
        self.driver = driver

    def initMedia(self):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div').click()
        advtype = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/span').text
        return advtype

    def exitLogin(self):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[2]/div/div').click()
        title = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/p[1]').text
        return  title


#媒体广告
class MediaPage(Page):
    def __init__(self, driver):
        self.driver = driver

    def deleteMediaAdv(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[1]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[1]/ul/a[1]').click()
        first_title = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/div').text
        if  first_title == name:
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[3]/div/div/div/div/span').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[25]/div/div[2]/div/div/div/span[4]').click()
            time.sleep(3)
            self.driver.find_element_by_xpath('/html/body/div[45]/div[2]/div/div/div/div/div[3]/button[2]').click()
            time.sleep(5)
            first_title = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/div').text
        return first_title




#大屏广告
class LargePage(Page):
    def __init__(self, driver):
        self.driver = driver



#认证页
class AuthenticationPage(Page):
    def __init__(self, driver):
        self.driver = driver



#个人中心页
class PersonalPage(Page):
    def __init__(self, driver):
        self.driver = driver



#定向包页
class OrientationPage(Page):
    def __init__(self, driver):
        self.driver = driver

    def buildDXB(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/button').click()

        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[2]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/textarea').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/button').click()
        dxbName = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        return dxbName

    def deleteDXB(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[1]').click()
        first_title = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        if first_title == name:
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[5]/div/div/span[2]').click()
            self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
            time.sleep(5)
            first_title = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        return first_title


#人群包页
class PeoplePage(Page):
    def __init__(self, driver):
        self.driver = driver

    def buildRQB(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/input').send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[3]/div/button[2]').click()
        first_name = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        return first_name


    def deleteRQB(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[2]').click()
        first_name = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        if first_name == name:
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/span').click()
            self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div[3]/button[2]').click()
            time.sleep(5)
            first_name = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        return first_name

    def buildImeiRQB(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/form/div[3]/div/div[2]/div/button').click()
        time.sleep(3)
        # 上传图片
        os.system(r'E:\\IMEI300.exe')
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div[2]/button[1]').click()
        time.sleep(8)
        first_name = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        return first_name

    def deleteIMEIRQB(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[2]').click()
        first_name = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        if first_name == name:
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/span[2]').click()
            self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div[3]/button[2]').click()
            time.sleep(5)
            first_name = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div').text
        return first_name


#落地页 页
class LandingPage(Page):
    def __init__(self, driver):
        self.driver = driver

    def buildLanding(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[3]').click()

        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/img').click()
        self.driver.find_element_by_xpath('//*[@id="saveLoadPage"]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/input').send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]').click()
        first_name = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/ul/li[1]/div[1]/p[1]').text
        return first_name

    def deleteLanding(self,name):
        login(self)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/ul/a[3]').click()
        first_name = self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/ul/li[1]/div[1]/p[1]').text
        if  first_name == name:
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/ul/li[1]/div[1]/p[2]/button[4]').click()
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]').click()
            time.sleep(5)
            first_name = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/ul/li[1]/div[1]/p[1]').text
        return first_name


#广告创建页
class AdvPage(Page):
    def __init__(self, driver):
        self.driver = driver

    def closeBuildAdv(self):
        login(self)
        print('登录成功')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/a/i').click()
        print('点击成功')
        time.sleep(2)

    def buildMediaAdv(self,name):
        login(self)
        print('登录成功')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[1]').click()
        time.sleep(3)
        #
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if '创建/编辑 媒体广告' == self.driver.title:
                print('切换到目标窗口')
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div').click()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/button').click()
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[5]/div/div/input').send_keys('2')
                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/button').click()
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/input').send_keys(
                    name)
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div/input').send_keys(
                    name)

                self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[3]/div/div/div').click()

                time.sleep(3)
                # 上传图片
                os.system(r'E:\\a.exe')
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/div/div/div[2]/button[2]').click()
                #落地页
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/div[6]/span[2]').click()
                time.sleep(5)
                self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[1]').click()
                self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div[2]/div/div[3]/button').click()
                title = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/div')
                first_title = title.text
                return first_title





def login(self):
    pageBase = Page(self.driver)
    pageBase.login('13600587905', '123456789', True)