import grequests
import requests
import json
from login_token import get_token
import time
import random

#广告请求上报测试


def advRep(token):
    materials = []
    url = 'http://115.236.35.106:9000/api/n/lightup/adv/request?location=STAKE_COMMENT'
    data = {"appVersion":"2.3.9","deviceWidth":"720","language":"zh-CN","imsi":"869507034526271","advWidth":"720","ua":"Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36","platform":"0","mac":"02:00:00:00:00:00","operator":"46003","deviceHeight":"1356","osVersion":"8.1.0","vendor":"PD1731","pkgName":"com.topjoytec.jrdl","advHeight":"1356","model":"vivo Y71","networkType":"2","isBoot":"0","androidId":"869507034526271","deviceType":"0","orientation":"0","density":"2","appName":"今日点亮","ip":"","isBreak":"0","imei":"869507034526271"}
    headers = {"Content-Type": "application/json", "ACCESS_TOKEN": token,"PLATFORM": "Android",
               "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36"}
    ret = requests.post(url=url,data=json.dumps(data), headers=headers)
    code = ret.json()['code']
    print('advReptime=' +str(ret.elapsed.total_seconds()))
    if(code==0):
        materials = ret.json()['data']['materials']
        # print(len(materials))#列表长度
        # tradeNo = ret.json()['data']['tradeNo']
    else:
        print(ret.json())
    return materials



def showReport(token,url):
    # url = 'http://115.236.35.106:9000/api/n/adv/media/exposure'
    # parm = {
    #     'tradeNo':tradeNo,
    #     'advId': 736,
    #     'appId': 'rNHXmLj7eRPQ1WaRm9eeo2qQSm6eiOVotz3P',
    #     'locationId': 'QI6Jeo745z67aw12k8A0wg4Th5dAbpQ7xyQ1'
    # }
    headers = {"Content-Type": "application/json","ACCESS_TOKEN" : token,"User-Agent" : "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36"}
    ret = requests.get(url=url, headers=headers)
    code = ret.json()['code']
    print('showReport---->' + str(code))
    print('showReporttime=' + str(ret.elapsed.total_seconds()))
    return code




def clickReport(token,url):
    # url = 'http://115.236.35.106:9000/api/n/adv/media/click'
    # parm = {
    #     'tradeNo': tradeNo,
    #     'advId': 736,
    #     'appId': 'rNHXmLj7eRPQ1WaRm9eeo2qQSm6eiOVotz3P',
    #     'locationId': 'QI6Jeo745z67aw12k8A0wg4Th5dAbpQ7xyQ1'
    # }
    headers = {"Content-Type": "application/json", "ACCESS_TOKEN": token,
               "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y71 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36"}
    ret = requests.get(url=url, headers=headers)
    code = ret.json()['code']
    print('clickReport---->'+str(code))
    print('clickReporttime=' + str(ret.elapsed.total_seconds()))
    return code



# token = get_token('13600587905')
token = "eh2eFy8NFrpbSXKYbw7hoqsrKtSUAMnq"
# advRep(token)
#循环请求广告
start = time.time()
for one in range(0,100):
    materials = advRep(token)
    if(len(materials)!=0):
        exposureUrls = materials[0]['exposureUrls'][0]
        print(exposureUrls)
        clickUrls = materials[0]['clickUrls'][0]
        showReport(token, exposureUrls)
        # print(clickUrls)
        if(random.randint(0,9) == 5):
            clickReport(token,clickUrls)

end = time.time()
print(end-start)

# def allAdv():
#     print(time.time())
#     materials = advRep(token)
#     if (len(materials) != 0):
#         exposureUrls = materials[0]['exposureUrls'][0]
#         print(exposureUrls)
#         clickUrls = materials[0]['clickUrls'][0]
#         showReport(token, exposureUrls)
#         if (random.randint(0, 9) == 5):
#             clickReport(token, clickUrls)
#
# req_list = [allAdv() for i in range(10)]
# grequests.map(req_list)