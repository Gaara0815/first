import xlrd
from xlutils.copy import copy#复制函数
from coupon import get_coupon
from login_token import get_token
import json

#1读取用例
excelDir = r'D:\接口测试用例.xlsx'
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
token = get_token("13600587905")
for one in range(1,workSheet.nrows):
    cellUrl = workSheet.cell(one,3).value
    cellData = workSheet.cell(one,6).value
    cellHeaders = workSheet.cell(one,5).value
    # cellHeaders = '{'+cellHeaders+'}'
    c_data = {cellData}
    res = get_coupon(cellUrl, cellData, cellHeaders, token)
    # print(res)
    code = res['code']
    if  code == 0:
        excel_res = '通过'
    else:
        excel_res = '不通过'
    workSheetNew.write(one, 9, str(res))  # 写单元格
    workSheetNew.write(one,10,excel_res)#写单元格

workbookNew.save(r'D:\接口测试用例2.xlsx')