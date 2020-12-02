from selenium import webdriver
import time
from selenium.webdriver import ActionChains
def start():
    # 此步骤很重要
    chrome_options = webdriver.ChromeOptions();
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    # 打开浏览器
    driver = webdriver.Chrome(options=chrome_options);
    # driver = webdriver.Chrome()
    driver.get('http://192.168.0.34:9000/h/n/firstCode/regLogin')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div/input').send_keys(
        '13600587913')
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div[2]/div/input').send_keys(
        '1234')
    # # 选择拖动滑块的节点
    # sli_ele = driver.find_element_by_xpath('//*[@id="nc_1-stage-1"]/div/div[3]')
    # # ------------鼠标滑动操作------------
    # action = ActionChains(driver)
    # # 第一步：在滑块处按住鼠标左键
    # action.click_and_hold(sli_ele)
    # # 第二步：相对鼠标当前位置进行移动
    # time.sleep(3)
    # action.move_by_offset(1500, 0)
    # time.sleep(3)
    # # 第三步：释放鼠标
    # action.release()
    # # 执行动作
    # action.perform()
    # driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/button').click()
    # time.sleep(10)

# start()



import requests
from selenium import webdriver
import urllib.request
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import random
##选用开发者模式，创建一个浏览器对象，可避免被检测到是selenium模拟浏览器
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=option)
def get_track(distance ):
    track = []
    current = 0
    mid = distance * (4/5)
    t = 2
    v = 0
    v1  = 0
    a1 = 2
    a = 4
    while current < distance:
        if current < mid:
            move = v * t + 1/2 * a *t * t
            current += move
            track.append(round(move))
            v = v + a*t
        else:
            move1 = v1 * t + 1/2 * a1 *t *t
            current += move1
            track.append(round(move1))
            v1 = v1 + a1*t

    return track
def main():
    browser.get('http://192.168.0.34:9000/h/n/firstCode/regLogin')
    # browser.find_element_by_id('J_Quick2Static').click()#点击密码登录按钮，选择用密码方式登录,如打开浏览器的界面是登录，此行可省略


    slider = browser.find_element_by_xpath('//*[@id="nc_1-stage-1"]/div/div[3]')#找到滑动按钮
    ActionChains(browser).click_and_hold(slider).perform()
    track = get_track(700)#模拟运动轨迹，速度先快后慢
    for x in track:
        ActionChains(browser).drag_and_drop_by_offset(slider,xoffset=x,yoffset=random.randint(1,3)).perform()
    ActionChains(browser).release().perform()
    # denglu =browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]')
    # denglu.click()#点击登录按钮
    # browser.find_element_by_id('bought').click()#进入自己的账户界面，点击全部订单
    # time.sleep(2)

if __name__ == '__main__':
    main()
