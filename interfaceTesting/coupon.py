from login_token import get_token
from login_token import getbizId
import requests
import json

#post请求测试接口方法

def post_coupon(c_url,c_data,c_headers):
    c_resq = requests.post(c_url,data=json.dumps(c_data),headers=c_headers)
    # print(res)
    return c_resq

def get_coupon(c_url,c_data,c_headers):
    c_resq = requests.get(c_url,params=c_data,headers=c_headers)
    # print(res)
    return c_resq

# token = get_token("13609587905")
# token = '4ESIFiUBmhENlUbIKsHM9FoP8WOvCUEgzxdJ'
# c_url = 'http://115.236.35.106:9000/api/adv/faster/save'
# c_data = {"needSmartRelease":1,"landingTitle":"","releaseTime":"00:00～24:00","releasePrice":2000.0,"releaseDay":"2020-04-10 开始",
# "fasterAdvReleaseLocation":{"needVideo":1,"settleModes":[{"updatedTime":2019,"settleMode":"CPC","minPrice":1030,"cptPublication":"",
# "createdTime":2019,"id":1290,"releaseLocationId":1,"suggestPrice":2030},{"updatedTime":2019,"settleMode":"CPM","minPrice":1000,
# "cptPublication":"","createdTime":2019,"id":1291,"releaseLocationId":1,"suggestPrice":10000}]},"fixedPrice":3010.0,"acquisitionMode":0,
# "releaseStartDay":"20200410","promoteType":1,"landingType":"0","needOptimizeMaterial":1,"dayMaxAmount":1000000.0,"settleMode":"CPC",
# "bizId":'MV7eFmdLvWhC0IacMqyk3bnB37EOXQPb',"createModel":"0","advName":"广告创建测试","releaseStartTime":"0","previewImg":"","releaseEndDay":"",
# "directionalJson":{"locationId":1,"coverNum":"456334","timeset":["4276"],"behavior":{"behaviorSceneTitle":"App,电商,资讯",
# "behaviorStrengthTitle":"不限","behaviorScene":["3880","3881","3882"],"behaviorStrength":["3891"],"behaviorValidityTitle":"7天",
# "behaviorValidity":["3884"]},"exposureNum":"14562389"},"fixedPriceDayAmount":1000010.0,"fixedPriceSupport":1,"landingId":"","editUrl":"",
# "entrustOperation":0,"needScreenshot":0,"materialImgs":[{"originalImg":"http://cdn.topjoytec.com/gBWQdYeXLqy3Sk4glLxVeg.jpg",
# "cutImg":"http://cdn.topjoytec.com/XEyoQ5Y5ksC90LiefiAIpQ.jpg","materialSize":"640*720"}],"releaseEndTime":"24","isOuterUrl":1,
# "landingUrls":["ikf.kskdk"],"slogan":"还记得看到了","releaseLocationId":1}
# print(type(c_data))
# c_headers = '''{"Content-Type":"application/x-www-form-urlencoded","ACCESS_TOKEN":"test-token"}'''
# cc_headers = json.loads(c_headers)
# cc_headers['ACCESS_TOKEN'] = token
# post_coupon(c_url,c_data,cc_headers)