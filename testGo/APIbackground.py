from selenium import webdriver
import time
import os
import win32gui
import win32con
import win32clipboard as w
from threading import Thread  # 导入线程函数
from testGo.sendQQ import sendByUser,setImage
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
        savePhoto(driver,'1')
        time.sleep(1800)

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
        savePhoto(driver,'2')
        time.sleep(1800)


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
        Fail_name = '.\\' + directory_time + '\\' + name + '.png'
        url = driver.save_screenshot(Fail_name)
        time.sleep(5)
        sendByUser('3417781932')
        setImage(File_Path + name + '.png')
        # print("%s ：截图成功！！！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)
    time.sleep(2)


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


def main():  # 定义main函数
    t1 = Thread(target=start)  # 定义线程t1
    t2 = Thread(target=start2)  # 定义线程t2
    t1.start()  # 开始运行t1线程
    t2.start()  # 开始运行t2线程

# start()
# start2()
# sendQQ()
if __name__ == '__main__':
    main()