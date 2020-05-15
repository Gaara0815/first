from login_token import get_token
import requests
import json

#post请求测试接口方法

def get_coupon(c_url,c_data,c_headers,c_token):
    cc_headers = json.loads(c_headers)
    cc_headers['ACCESS_TOKEN'] = c_token
    c_resq = requests.post(c_url,data=json.dumps(c_data),headers=cc_headers)
    res = c_resq.json()
    # print(res)
    return res

# token = get_token("13609587905")
# c_url = 'http://115.236.35.106:9000/api/product/coupon/receiver'
# c_data = {"couponId":"184"}
# c_headers = '''{"Content-Type":"application/x-www-form-urlencoded","ACCESS_TOKEN":"test-token"}'''
# get_coupon(c_url,c_data,c_headers,token)