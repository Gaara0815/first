from selenium import webdriver
import time
import os

def start():
    driver = webdriver.Chrome()
    driver.get('http://apirabbitmq.caloinfo.cn:15672/#/queues/%2F/queue.zgapi.transient')
    driver.find_element_by_xpath('//*[@id="login"]/form/table/tbody/tr[1]/td/input').send_keys(
        'zgapi')
    driver.find_element_by_xpath('//*[@id="login"]/form/table/tbody/tr[2]/td/input').send_keys(
        'zgapi@topjoycloud')
    driver.find_element_by_xpath('//*[@id="login"]/form/table/tbody/tr[3]/td/input').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tabs"]/li[1]').click()
    time.sleep(2)
    while True:
        a = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/table[3]/tbody/tr[1]/td').text
        times = a[0:len(a) - 2]
        if(len(times)<2):
            print('异常异常异常异常异常异常异常')
        else:
            print('正常正常正常正常正常正常正常')
        print('time='+times)
        savePhoto(driver)
        time.sleep(1800)

def start2():
    driver = webdriver.Chrome()
    driver.get('http://advert.topjoycloud.com:9538/zgapi/jsp/login.do')
    driver.find_element_by_xpath('/html/body/div/section[2]/div/form/div[1]/div[3]').click()
    driver.find_element_by_xpath('/html/body/div/section[2]/div/form/div[2]/div[1]/input[1]').send_keys(
        'admin')
    driver.find_element_by_xpath('/html/body/div/section[2]/div/form/div[2]/div[1]/input[2]').send_keys(
        'ky2020@72jrdl')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="Login"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="westreg"]/div/div[2]/div[1]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="westreg"]/div/div[2]/div[2]/ul/li[1]/a').click()
    time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/span[1]/span').click()
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[1]/span[1]/input[1]').send_keys(
    #     '山西米奥电子商务有限公司')
    driver.find_element_by_link_text("查询").click()
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a').click()
    time.sleep(2)
    # while True:
    #     savePhoto(driver)
    #     time.sleep(60*30)



def savePhoto(driver):
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
        url = driver.save_screenshot('.\\' + directory_time + '\\' + picture_time + '.png')
        # print("%s ：截图成功！！！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)
    time.sleep(2)

start()
# start2()