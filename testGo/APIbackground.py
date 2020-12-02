from selenium import webdriver
import time
import os
import win32gui
import win32con
import win32clipboard as w
from threading import Thread  # 导入线程函数
from testGo.sendQQ import sendByUser,setImage,setImage2
# pywin32

def start():
    driver = webdriver.Chrome()
    driver.get('http://47.96.164.71:15672/#/queues/%2F/ha.adv.queue')
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="login"]/form/table/tbody/tr[1]/td/input').send_keys(
        'lightup')
    driver.find_element_by_xpath('//*[@id="login"]/form/table/tbody/tr[2]/td/input').send_keys(
        'lightup')
    driver.find_element_by_xpath('//*[@id="login"]/form/table/tbody/tr[3]/td/input').click()
    time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="tabs"]/li[1]').click()
    # time.sleep(2)
    while True:
        # a = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/table[3]/tbody/tr[1]/td').text
        # times = a[0:len(a) - 2]
        # if(len(times)<2):
        #     print('异常异常异常异常异常异常异常')
        # else:
        #     print('正常正常正常正常正常正常正常')
        # print('time='+times)
        # sendQQ(times)
        savePhoto(driver,'a')
        time.sleep(1800)

#
def start2():
    driver = webdriver.Chrome()
    driver.get('http://advert.topjoycloud.com:9538/zgapi/jsp/login.do')
    driver.maximize_window()
    driver.find_element_by_xpath('/html/body/div/section[2]/div/form/div[1]/div[3]').click()
    driver.find_element_by_xpath('/html/body/div/section[2]/div/form/div[2]/div[1]/input[1]').send_keys(
        'admin')
    driver.find_element_by_xpath('/html/body/div/section[2]/div/form/div[2]/div[1]/input[2]').send_keys(
        'ky2020@72jrdl')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="Login"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="westreg"]/div/div[2]/div[1]/div[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="westreg"]/div/div[2]/div[2]/ul/li[4]').click()
    time.sleep(3)
    frame = driver.find_element_by_xpath('//*[@id="tt"]/div[2]/div[2]/div/iframe')
    driver.switch_to.frame(frame);
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/span[2]/input[1]').send_keys(
        '山西米奥电子商务有限公司')
    while True:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]/span/span[1]').click()
        time.sleep(10)
        savePhoto(driver,'b')
        time.sleep(1800)

def start11():
    driver = webdriver.Chrome()
    driver.get('http://192.168.0.32:9006/#')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/p[2]').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/input').send_keys('13600587905')
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/input').send_keys('123' + '\n')
    # self.driver.find_element_by_xpath('//*[@id="app"]/div/div/button').click()
    driver.implicitly_wait(10)
    texts = driver.switch_to.alert.text
    print(texts)
    assert texts == '密码不正确，请重新输入'

#雷达设备设置WIFI密码
def start3():
    driver = webdriver.Chrome()
    driver.get('http://192.168.1.1/')
    driver.maximize_window()
    # driver.find_element_by_xpath('//*[@id="maincontent"]/div/form/div[1]/fieldset/fieldset/div[1]/div/input').send_keys(
    #     'admin')
    driver.find_element_by_xpath('//*[@id="maincontent"]/div/form/div[1]/fieldset/fieldset/div[2]/div/input').send_keys(
        'admin')
    driver.find_element_by_xpath('//*[@id="maincontent"]/div/form/div[2]/input[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[2]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[2]/ul/li[2]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/fieldset[1]/table/tbody/tr[3]/td[4]/input[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tab.wireless.ap.encryption"]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cbid.wireless.ap.encryption"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cbid.wireless.ap.encryption-psk2"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cbid.wireless.ap._wpa_key"]').send_keys(
        'kaiyuxinxi2020dl72')
    driver.find_element_by_xpath('//*[@id="maincontent"]/div/form/div[3]/input[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tab.wireless.ap.encryption"]/a').click()
    driver.find_element_by_xpath('//*[@id="cbi-wireless-ap-_wpa_key"]/div/img').click()
    password = driver.find_element_by_xpath('//*[@id="cbid.wireless.ap._wpa_key"]').get_attribute('value')
    if(password == 'kaiyuxinxi2020dl72'):
        print('修改成功')
    else:
        print('修改失败')
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(picture_time)
    driver.quit()



    # time.sleep(2)


def start4():
    driver = webdriver.Chrome()
    driver.get('http://47.99.48.199:8081/clusters/kafka_cluster/consumers/api.consume/topic/api-advert/type/KF')
    driver.maximize_window()
    while True:
        driver.refresh()
        photo = savePhoto(driver,'start4')
        print('start4='+photo)
        # sendByUser('3417781932')
        # setImage(photo)
        time.sleep(30)


def start5():
    driver = webdriver.Chrome()
    driver.get('http://47.99.48.199:8081/clusters/kafka_cluster/topics')
    driver.maximize_window()
    while True:
        driver.refresh()
        photo = savePhoto(driver, 'start5')
        print('start5=' + photo)
        # sendByUser('1358099456')
        # setImage2(photo)
        time.sleep(30)

def savePhoto(driver,name):
    # 生成年月日时分秒时间
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # print(picture_time)
    # print(directory_time)
    # 打印文件目录
    # print(os.getcwd())
    # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        File_Path = os.getcwd() + '\\' + directory_time + '\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            # print("目录新建成功：%s" % File_Path)
        # else:
            # print("目录已存在！！！")
    except BaseException as msg:
        print("新建目录失败：%s" % msg)
    try:
        Fail_name = '.\\' + directory_time + '\\' + picture_time+name + '.png'
        url = driver.save_screenshot(Fail_name)
        photo = File_Path + picture_time +name + '.png'
        return photo
        # sendByUser('3417781932')
        # setImage(File_Path + picture_time + '.png')
        # print("%s ：截图成功！！！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)


def sendQQ(msg):
    # 窗口名字
    name = "3417781932"
    # 将测试消息复制到剪切板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, name)
    # while 1==1:
    if 1 == 1:
        # 填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        # 回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


# def main():  # 定义main函数
#     t1 = Thread(target=start4)  # 定义线程t1
#     t2 = Thread(target=start5)  # 定义线程t2
#     t1.start()  # 开始运行t1线程
#     t2.start()  # 开始运行t2线程

# start()
# start2()
# start3()
# sendQQ()
# start4()
start11()
# if __name__ == '__main__':
#     main()