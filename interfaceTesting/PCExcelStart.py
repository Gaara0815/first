import xlrd
from xlutils.copy import copy#复制函数
from interfaceTesting.coupon import post_coupon
from interfaceTesting.coupon import get_coupon
from interfaceTesting.login_token import getlogin_resp
from interfaceTesting.login_token import getbizId
import json
import os
import time
import hashlib
from interfaceTesting.WorkManager import Workmanager
#PC版72投接口测试
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cur_path = os.path.dirname(os.path.realpath(__file__))
# 获取工程所在的路径，如果加入目录名字切换到该目录下
config_path = os.path.join(os.path.dirname(cur_path), 'interfaceTesting')
# jme = locatpath = PATH(config_path + r'\接口测试用例.xlsx')

#1读取用例
excelDir = PATH(config_path + r'\PC版72投接口测试用例.xlsx')
#打开excel
# workbook = xlrd.open_workbook(excelDir,formatting_info=True) #保持excel原有格式
workbook = xlrd.open_workbook(excelDir)
#查看所有子表名
# print(workbook.sheet_names())
workSheet = workbook.sheet_by_name('工作表1')
#读取一行
rows = workSheet.row_values(1)
workbookNew = copy(workbook)
workSheetNew = workbookNew.get_sheet(0)



#读取指定单元
# cellData = workSheet.cell(1,6).value#行，列
# pprint.pprint(cellData)
# print(workSheet.cell(1,6))#单元数据类型 0 1：字符串 2 3 4 5

VERSION_RELEASE = False
root = 'https://72ad.topjoytec.com' if VERSION_RELEASE else 'http://115.236.35.106:9000'

#执行
# login_resp = getlogin_resp("13600587905")
# token = login_resp.json()['data']['token']
# KyToken = login_resp.json()['data']['kyToken']
token   = 'P1LDMfsJEtxQEAMwtm6EThxluyqfsIU9nWJ3'
KyToken =  'kU1eafimzckM4FkshaobrdqeHp1FRx6Uk9S9'
password='123456789'
# s.encode()#变成bytes类型才能加密
nowPassword = hashlib.md5(password.encode())
#定向包ID
DXBid = 0
# for one in range(1,workSheet.nrows):
work_manager = WorkManager(workSheet.nrows, 2)  # 或者work_manager =  WorkManager(10000, 20)
work_manager.wait_allcomplete()
def startTest(one):
    one = one+1
    #是否测试
    isTest = workSheet.cell(one, 11).value
    if isTest == 2:
        return
    #请求方式
    reqMethod = workSheet.cell(one,4).value
    cellUrl = root+workSheet.cell(one,3).value
    cellData = workSheet.cell(one,6).value
    cellHeaders = workSheet.cell(one,5).value
    #预期返回数据
    expectRes = json.loads(workSheet.cell(one,8).value)

    expectCode = expectRes['code']#预计结果

    # c_data = {cellData}
    c_data = json.loads(cellData)
    if (one == 5):#处理广告创建特殊字段
        c_data['bizId'] = getbizId(32)
        c_data['startTime'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))+' 开始'
        c_data['releaseStartDay'] = time.strftime('%Y%m%d', time.localtime(time.time()))
    if(one == 19):#处理定向包删除特殊字段
        c_data['id'] = DXBid
    if (one == 21):  # 处理修改密码特殊字段
        newpassword = '123456789'
        # s.encode()#变成bytes类型才能加密
        newPassword = hashlib.md5(newpassword.encode())
        c_data['password'] = nowPassword.hexdigest()
        c_data['newPassword'] = newPassword.hexdigest()
    if (one == 23):  # 处理账号密码登录特殊字段
        c_data['password'] = newPassword.hexdigest()
    cc_headers = json.loads(cellHeaders)
    cc_headers['ACCESS_TOKEN'] = token
    cc_headers['KyToken'] = KyToken
    if reqMethod == 'post':
        c_resq = post_coupon(cellUrl, c_data, cc_headers)
    else:
        c_resq = get_coupon(cellUrl, c_data, cc_headers)
    res = c_resq.json()
    reqTime = c_resq.elapsed.total_seconds()#请求消耗时间
    print(workSheet.cell(one,1).value + str(res))
    code = res['code']#实际结果
    if (one == 18 and code == 0):#处理定向包创建后返回的字段
        DXBid = res['data']['id']
    if  code == expectCode:
        excel_res = '通过'
    else:
        excel_res = '不通过'
    workSheetNew.write(one, 6,json.dumps(c_data))  # 写单元格
    workSheetNew.write(one, 9, str(res))  # 写单元格
    workSheetNew.write(one,10,excel_res)#写单元格
    workSheetNew.write(one, 12, str(reqTime))  # 写单元格

workbookNew.save(PATH(config_path + r'\PC版72投接口测试结果.xls'))