import xlrd
from xlutils.copy import copy#复制函数
from coupon import post_coupon
from coupon import get_coupon
from login_token import get_token
from login_token import getbizId
import json
import os
import time

#使用接口测试用例进行接口测试
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cur_path = os.path.dirname(os.path.realpath(__file__))
# 获取工程所在的路径，如果加入目录名字切换到该目录下
config_path = os.path.join(os.path.dirname(cur_path), 'interfaceTesting')
# jme = locatpath = PATH(config_path + r'\接口测试用例.xlsx')

#1读取用例
excelDir = PATH(config_path + r'\接口测试用例.xlsx')
#打开excel
# workbook = xlrd.open_workbook(excelDir,formatting_info=True) #保持excel原有格式
workbook = xlrd.open_workbook(excelDir)
#查看所有子表名
# print(workbook.sheet_names())
workSheet = workbook.sheet_by_name('工作表1')
#读取一行
rows = workSheet.row_values(1)
# c = workSheet.cell_value(1)
workbookNew = copy(workbook)
workSheetNew = workbookNew.get_sheet(0)



#读取指定单元
# cellData = workSheet.cell(1,6).value#行，列
# pprint.pprint(cellData)
# print(workSheet.cell(1,6))#单元数据类型 0 1：字符串 2 3 4 5

#执行
# token = get_token("13600587905")
token = '4ESIFiUBmhENlUbIKsHM9FoP8WOvCUEgzxdJ'
for one in range(1,workSheet.nrows):
    #是否测试
    isTest = workSheet.cell(one, 11).value
    if isTest == 2:
        continue
    #请求方式
    reqMethod = workSheet.cell(one,4).value
    cellUrl = workSheet.cell(one,3).value
    cellData = workSheet.cell(one,6).value
    cellHeaders = workSheet.cell(one,5).value
    #预期返回数据
    expectRes = json.loads(workSheet.cell(one,8).value)

    expectCode = expectRes['code']#预计结果

    # c_data = {cellData}
    c_data = json.loads(cellData)
    if(one==11):
        c_data['bizId'] = getbizId(32)
        c_data['releaseDay'] = time.strftime('%Y-%m-%d',time.localtime(time.time())) + " 开始"
        c_data['releaseStartDay'] = time.strftime('%Y%m%d',time.localtime(time.time()))
    cc_headers = json.loads(cellHeaders)
    cc_headers['ACCESS_TOKEN'] = token
    if reqMethod == 'post':
        c_resq = post_coupon(cellUrl, c_data, cc_headers)
    else:
        c_resq = get_coupon(cellUrl, c_data, cc_headers)
    res = c_resq.json()
    reqTime = c_resq.elapsed.total_seconds()#请求消耗时间
    print(res)
    code = res['code']#实际结果
    if  code == expectCode:
        excel_res = '通过'
    else:
        excel_res = '不通过'
    workSheetNew.write(one, 9, str(res))  # 写单元格
    workSheetNew.write(one,10,excel_res)#写单元格
    workSheetNew.write(one, 12, str(reqTime))  # 写单元格

workbookNew.save(PATH(config_path + r'\接口测试结果.xlsx'))