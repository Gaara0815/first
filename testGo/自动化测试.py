from appium import  webdriver
import time,traceback

# appPackage = 'com.tencent.mobileqq'
# appActivity = '.activity.SplashActivity'
appPackage = 'com.faster.advertiser'
appActivity = '.ui2.act.SplashActivity'

start = {}
start['platformName'] = 'Android'
start['platformVersion'] = '8.1.0'
start['deviceName'] = 'MI PLAY'
start['appPackage'] = appPackage
start['appActivity'] = appActivity
start['unicodeKeyboard'] = True
start['resetKeyboard'] = True
start['noReset'] = True
start['newCommandTimeout'] = 6000

#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub',start)

time.sleep(3)
et_phone = driver.find_element_by_id('com.faster.advertiser:id/et_phone')
et_phone.send_keys('13600587905')

tv_send_yzm = driver.find_element_by_id('com.faster.advertiser:id/tv_send_yzm')
tv_send_yzm.click()

et_yzm = driver.find_element_by_id('com.faster.advertiser:id/et_yzm')

# driver.find_element_by_id('com.tencent.mobileqq:id/relativeItem').click()
# driver.find_element_by_id('com.topjoytec.jrdl:id/today_light').click()

