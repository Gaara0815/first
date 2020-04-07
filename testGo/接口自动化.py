import requests
import xlrd
import json
import pprint
import xlutils

#1读取用例
excelDir = r'D:\接口测试用例.xlsx'
#打开excel
workbook = xlrd.open_workbook(excelDir)
#查看所有子表名
# print(workbook.sheet_names())
workSheet = workbook.sheet_by_name('工作表1')
#读取一行
rows = workSheet.row_values(1)
# c = workSheet.cell_value(1)
#读取指定单元
cellData = workSheet.cell(1,6).value#行，列
# pprint.pprint(cellData)
# print(workSheet.cell(1,6))#单元数据类型 0 1：字符串 2 3 4 5




#2构建接口对应请求

gurl = 'http://115.236.35.106:9000/api/product/coupon/receiver'
gdata = {"couponId":"184"}
gheaders = {"Content-Type":"application/x-www-form-urlencoded","ACCESS_TOKEN":"test-token"}
resp = requests.post(gurl,data=json.dumps(gdata),headers=gheaders)
res = resp.json()['code']
if res == 0:
    print('成功---------耗时：',resp.elapsed.total_seconds())
    excel_res = "成功"
else:
    print('失败')
    excel_res = resp.json()['error']

pprint.pprint(resp.text)


from xlutils.copy import copy#复制函数

#3 测试结果写入excel

#复制
# workbookWr = copy(workbook)
# wrSheet = workbookWr.get_sheet(0)
# wrSheet.write(1,9,excel_res)
# workbookWr.save(r'D:\接口测试用例2.xlsx')














