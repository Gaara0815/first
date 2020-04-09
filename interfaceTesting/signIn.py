import requests
import json
import xlrd
import json
import random
#1读取用例
excelDir = r'D:\mobile.xlsx'
#打开excel
# workbook = xlrd.open_workbook(excelDir,formatting_info=True) #保持excel原有格式
workbook = xlrd.open_workbook(excelDir)
#查看所有子表名
# print(workbook.sheet_names())
workSheet = workbook.sheet_by_name('Sheet1')

# a = ''
def getbizId(length):
         a = ''
         str = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
         for one in range(0, length):
             number = random.randint(0,61)
             a = a+(str[number])
         print(a)
         return a

#测试环境
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
    # print(login_resp.text)
    token = login_resp.json()['data']['token']
    return token

    # 输入邀请码接口
    # sign_url = 'http://115.236.35.106:9000/api/n/adv/faster/invite'
    # sign_data = {"inviteBy": "695969", "token": token}
    # sign_headers = {"Content-Type": "application/json","ACCESS_TOKEN" : token}
    # sign_resp = requests.post(sign_url, data=json.dumps(sign_data), headers=sign_headers)
    # print(sign_resp.text)


# get_token('15967139174')

#创建广告
def buildAdv(mobile):
    buildAdv_url = 'http://115.236.35.106:9000/api/adv/faster/save'
    buildAdv_data = {"needSmartRelease":1,"landingTitle":"","releaseTime":"00:00～24:00","releasePrice":2000.0,"releaseDay":"2020-04-10 开始","fasterAdvReleaseLocation":{"needVideo":1,"settleModes":[{"updatedTime":2019,"settleMode":"CPC","minPrice":1030,"cptPublication":"","createdTime":2019,"id":1290,"releaseLocationId":1,"suggestPrice":2030},{"updatedTime":2019,"settleMode":"CPM","minPrice":1000,"cptPublication":"","createdTime":2019,"id":1291,"releaseLocationId":1,"suggestPrice":10000}]},"fixedPrice":3010.0,"acquisitionMode":0,"releaseStartDay":"20200410","promoteType":1,"landingType":"0","needOptimizeMaterial":1,"dayMaxAmount":1000000.0,"settleMode":"CPC","bizId":getbizId(32),"createModel":"0","advName":"TM咖啡","releaseStartTime":"0","previewImg":"","releaseEndDay":"","directionalJson":{"locationId":1,"coverNum":"456334","timeset":["4276"],"behavior":{"behaviorSceneTitle":"App,电商,资讯","behaviorStrengthTitle":"不限","behaviorScene":["3880","3881","3882"],"behaviorStrength":["3891"],"behaviorValidityTitle":"7天","behaviorValidity":["3884"]},"exposureNum":"14562389"},"fixedPriceDayAmount":1000010.0,"fixedPriceSupport":1,"landingId":"","editUrl":"","entrustOperation":0,"needScreenshot":0,"materialImgs":[{"originalImg":"http://cdn.topjoytec.com/gBWQdYeXLqy3Sk4glLxVeg.jpg","cutImg":"http://cdn.topjoytec.com/XEyoQ5Y5ksC90LiefiAIpQ.jpg","materialSize":"640*720"}],"releaseEndTime":"24","isOuterUrl":1,"landingUrls":["ikf.kskdk"],"slogan":"还记得看到了","releaseLocationId":1}
    buildAdv_headers = {"Content-Type": "application/json","ACCESS_TOKEN" : get_token(mobile)}
    buildAdv_resp = requests.post(buildAdv_url, data=json.dumps(buildAdv_data), headers=buildAdv_headers)
    print(buildAdv_resp.text)

#循环创建广告
for one in range(0,workSheet.nrows):
    m = workSheet.cell(one,1).value
    mobile = str(m)[0:-2]
    print(mobile)
    buildAdv(mobile)
# buildAdv("13600587905")