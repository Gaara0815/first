import requests
import json
import random

#获取token测试

# a = ''
def getbizId(length):
         a = ''
         str = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
         for one in range(0, length):
             number = random.randint(0,61)
             a = a+(str[number])
         print(a)
         return a


def getStrs(length):
    a = ''
    str = "沙发我我攻击完全的深刻的渴望我我无我欧尼恩发你基督教可是可能发生骄傲进度计划的黑白分明开始看覅看不完就事论事可麻烦龙门飞剑把打火机的骄傲了考试看看谁看看";
    for one in range(0, length):
        number = random.randint(0, 61)
        a = a + (str[number])
    print(a)
    return a

#测试环境72投，今日点亮
def get_token(mobile):
    sms_url = 'http://115.236.35.106:9000/api/n/sms/faster/login'
    sms_data = {"mobile": mobile}
    sms_headers = {"Content-Type": "application/json"}
    sms_resp = requests.post(sms_url, data=json.dumps(sms_data), headers=sms_headers)
    # print(sms_resp.text)
    err = sms_resp.json()['error']
    yzm = err[len(err)-4:len(err)]
    print(err)

    login_url = 'http://115.236.35.106:9000/api/n/user/login/faster/sms'
    login_data = {"mobile": mobile,"smsCode":yzm}
    login_headers = {"Content-Type": "application/json"}
    login_resp = requests.post(login_url, data=json.dumps(login_data), headers=login_headers)
    print(login_resp.text)
    token = login_resp.json()['data']['token']
    # print(token)
    return token


#测试环境 活动田
def get_HDTtoken(mobile):
    sms_url = 'http://testlingjuanminipro.caloinfo.com:4550/api/n/message/code/send'
    parm = {
        'mobile': mobile,
        'type': 'verfiy',
    }
    sms_headers = {"Content-Type": "application/json"}
    sms_resp = requests.get(sms_url, params=parm, headers=sms_headers)
    print(sms_resp.text)
    err = sms_resp.json()['message']
    yzm = err[len(err)-4:len(err)]
    print(err)

    login_url = 'http://testlingjuanminipro.caloinfo.com:4550/api/n/user/third/weixin/mini/mobile/login'
    login_data = {"mobile": mobile,"code":yzm,'smsType': 'verfiy'}
    login_headers = {"Content-Type": "application/json"}
    login_resp = requests.post(login_url, data=json.dumps(login_data), headers=login_headers)
    print(login_resp.text)
    token = login_resp.json()['data']['token']
    print(token)
    return token

# get_token('14444444444')
# get_HDTtoken('13600587906')
# for o in range(0,50):
#     getbizId(12)
# getStrs(12)