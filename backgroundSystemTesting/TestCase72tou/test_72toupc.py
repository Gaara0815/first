import pytest
import os
import allure
from selenium import webdriver
import time
from Page72tou.page72tou import LoginPage,IndexPage,MediaPage,LargePage,AuthenticationPage,PersonalPage,OrientationPage,PeoplePage,LandingPage,AdvPage
from Page72tou.page72tou import login
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec  # 引入包


ADVname = '测试广告'
DXBname = '测试定向包'
RQBname = '测试人群包'
IMEIname = 'IMEI300'
Landingname = '测试落地页'
account = '13600587905'
password = '123456789'
CSUrl = 'http://192.168.0.32:9006/#'
ZSUrl = 'https://72ad.topjoytec.com/#'#使用正式地址需修改登录方法及方法中参数
server = 1  #1测试，2正式
#72投PC版
class Test_72touPC():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(CSUrl)
        self.driver.implicitly_wait(20)

    # 函数级结束
    def teardown(self):
        self.driver.quit()

    #账号密码登录
    def test_1_login(self):
        '''使用正确账号密码登录'''
        loginPage = LoginPage(self.driver)
        loginPage.login(account,password,True)
        print('使用正确账号密码是否登陆成功')
        assert loginPage.get_title() != 'AI全景式信息投放管理平台'

    # 账号密码登录（失败）
    def test_2_login(self):
        '''使用错误账号密码错误'''
        loginPage = LoginPage(self.driver)
        loginPage.login(account,'12345678',False)
        print('使用错误账号密码是否正常登陆失败')
        assert loginPage.get_title() == 'AI全景式信息投放管理平台'

    #点击首页审核中广告数
    def test_3_initMedia(self):
        '''点击首页广告数'''
        indexPage = IndexPage(self.driver)
        advtype = indexPage.initMedia()
        print('点击首页广告数是否成功进入媒体广告列表')
        assert advtype == '审核中'

    #关闭广告弹窗
    def test_4_closeBuildAdv(self):
        '''关闭弹窗'''
        advPage = AdvPage(self.driver)
        advPage.closeBuildAdv()
        print('是否成功关闭创建广告的弹窗')
        assert advPage.get_title() == '首页'

    #创建媒体广告
    def test_5_buildMediaAdv(self):
        '''创建媒体广告'''
        advPage = AdvPage(self.driver)
        first_title = advPage.buildMediaAdv(ADVname,server)
        print('是否成功创建广告:'+ADVname)
        assert first_title == ADVname

    #删除广告
    def test_6_deleteMediaAdv(self):
        '''删除广告'''
        mediaPage = MediaPage(self.driver)
        first_title = mediaPage.deleteMediaAdv(ADVname)
        print('是否成功删除广告:'+ADVname)
        assert first_title != ADVname

    #创建定向包
    def test_7_buildDXB(self):
        orientationPage = OrientationPage(self.driver)
        firstName = orientationPage.buildDXB(DXBname)
        print('是否正常创建定向包:'+DXBname)
        assert firstName == DXBname

    # 删除定向包
    def test_8_deleteDXB(self):
        orientationPage = OrientationPage(self.driver)
        firstName = orientationPage.deleteDXB(DXBname)
        print('是否成功删除定向包:'+DXBname)
        assert firstName != DXBname

    #创建人群包
    def test_9_buildRQB(self):
        peoplePage = PeoplePage(self.driver)
        firstName = peoplePage.buildRQB(RQBname)
        print('是否正常创建人群包:'+RQBname)
        assert firstName == RQBname

    # 删除人群包
    def test_10_deleteRQB(self):
        peoplePage = PeoplePage(self.driver)
        firstName = peoplePage.deleteRQB(RQBname)
        print('是否成功删除人群包:'+RQBname)
        assert firstName != RQBname

    #创建上传人群包
    def test_11_buildIMEIRQB(self):
        peoplePage = PeoplePage(self.driver)
        firstName = peoplePage.buildImeiRQB(IMEIname)
        print('是否正常创建上传人群包:'+IMEIname)
        assert firstName == IMEIname

    #删除上传人群包
    def test_12_deleteRQB(self):
        peoplePage = PeoplePage(self.driver)
        firstName = peoplePage.deleteIMEIRQB(IMEIname)
        print('是否成功删除上传人群包:'+IMEIname)
        assert firstName != IMEIname

    #创建落地页
    def test_13_buildIMEIRQB(self):
        landingPage = LandingPage(self.driver)
        firstName = landingPage.buildLanding(Landingname)
        print('是否正常创建落地页:'+Landingname)
        assert firstName == Landingname

    #删除落地页
    def test_14_deleteRQB(self):
        landingPage = LandingPage(self.driver)
        firstName = landingPage.deleteLanding(Landingname)
        print('是否成功删除落地页:'+Landingname)
        assert firstName != Landingname

    #退出登录
    def test_15_exitLogin(self):
        indexPage = IndexPage(self.driver)
        title = indexPage.exitLogin()
        print('是否正常退出')
        assert title == 'AI全景式信息投放管理平台'



if __name__ == '__main__':
    #生成测试报告
    pytest.main(['test_72toupc.py', '-s', '--alluredir=report/allure_result'])
    os.system('allure serve report/allure_result')

    #pyinstaller --console --onefile test_72toupc.py   #打包


    # # 生成报告数据
    # pytest  .py --alluredir=report/allure_result
    #
    # # 本地环境生成报告
    # allure serve report/allure_result