from login_token import get_token
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
# c_url = 'http://192.168.0.211:9000/api/faster/radar/point/data/search'
# c_data = {"size":50,"pointName":"北京","page":1}
# print(type(c_data))
# c_headers = '''{"Content-Type":"application/x-www-form-urlencoded","ACCESS_TOKEN":"test-token"}'''
# post_coupon(c_url,c_data,c_headers,token)