import xlrd
from xlutils.copy import copy#复制函数
from coupon import get_coupon
from login_token import get_token
import json
import os

#使用接口测试用例进行接口测试
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
# 获取工程所在的路径，如果加入目录名字切换到该目录下
config_path = os.path.join(os.path.dirname(cur_path), 'interfaceTesting')
print(config_path)
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
    isTest = workSheet.cell(one, 11).value
    if isTest == 2:
        continue
    cellUrl = workSheet.cell(one,3).value
    cellData = workSheet.cell(one,6).value
    cellHeaders = workSheet.cell(one,5).value
    expectRes = json.loads(workSheet.cell(one,8).value)
    # cellHeaders = '{'+cellHeaders+'}'

    expectCode = expectRes['code']#预计结果

    c_data = {cellData}
    res = get_coupon(cellUrl, cellData, cellHeaders, token)
    print(res)
    code = res['code']#实际结果
    if  code == expectCode:
        excel_res = '通过'
    else:
        excel_res = '不通过'
    workSheetNew.write(one, 9, str(res))  # 写单元格
    workSheetNew.write(one,10,excel_res)#写单元格

workbookNew.save(PATH(config_path + r'\接口测试用例2.xlsx'))