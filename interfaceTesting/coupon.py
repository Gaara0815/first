from interfaceTesting.login_token import get_token
from login_token import getbizId
import requests
import json
import random

#post请求测试接口方法

def post_coupon(c_url,c_data,c_headers):
    c_resq = requests.post(c_url,data=json.dumps(c_data),headers=c_headers)
    # print(c_resq.json())
    return c_resq

def get_coupon(c_url,c_data,c_headers):
    c_resq = requests.get(c_url,params=c_data,headers=c_headers)
    # print(c_resq.json())
    # print(c_resq.elapsed.total_seconds())
    return c_resq

# token = get_token("13609587905")
# token = '4ESIFiUBmhENlUbIKsHM9FoP8WOvCUEgzxdJ'
# c_url = 'http://115.236.35.106:9000/api/faster/adv/radar/point/newlist'
# c_data = {"uid":5,"size":20,"page":1}
# c_headers = '''{"Content-Type":"application/x-www-form-urlencoded","ACCESS_TOKEN":"test-token"}'''
# cc_headers = json.loads(c_headers)
# cc_headers['ACCESS_TOKEN'] = token
# get_coupon(c_url,c_data,cc_headers)

# for one in range(0,50):
#     token = '4ESIFiUBmhENlUbIKsHM9FoP8WOvCUEgzxdJ'
#     c_url = 'http://115.236.35.106:9000/api/faster/adv/radar/point/save'
#     c_data = '''{"address":"浙江省杭州市拱墅区上塘街道科园路天瑞国际","industryId":56,"adcode":"330100","level":"city","latitude":30.325501844618049,"longitude":120.15988688151043,"pointName":"好像记得叫"}'''
#     c_headers = '''{"Content-Type":"application/json","ACCESS_TOKEN":"test-token"}'''
#     cc_headers = json.loads(c_headers)
#     cc_headers['ACCESS_TOKEN'] = token
#     cc_data = json.loads(c_data)
#     cc_data['pointName'] = str(one)
#     post_coupon(c_url, cc_data, cc_headers)
# token = "kz3MtVQVvDwfSeyed8y0ukbWG8GkUG9tufnh"
# token = get_token("13333333332")
# def getMAC(length):
#     a = ''
#     str = "1234567890abcdef";
#     for one in range(0, length):
#         number = str[random.randint(0, len(str) - 1)]
#         a = a + number
#     return a
#设备采集
# for one in range(0,4000):
#     c_url = 'http://115.236.35.106:9000/api/n/faster/radar/report'
#     c_headers = '''{"Content-Type":"application/json","ACCESS_TOKEN":"test-token"}'''
#     cc_headers = json.loads(c_headers)
#     cc_headers['ACCESS_TOKEN'] = token
#     c_data = '''{"bssid":"000000000000","channel":"1","dbm":"-35","deviceType":"unknown","encryptionType":"","mac":"54ee7594c3e5","radarPointId":383,"ssid":""}'''
#     cc_data = json.loads(c_data)
#     cc_data['mac'] = getMAC(12)
#     post_coupon(c_url, cc_data, cc_headers)
#     print(str(one))
