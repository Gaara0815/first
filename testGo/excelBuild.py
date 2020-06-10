import xlrd
from xlutils.copy import copy#复制函数
import os
import random

#excel数据处理
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
cur_path = os.path.dirname(os.path.realpath(__file__))
# 获取工程所在的路径，如果加入目录名字切换到该目录下
config_path = os.path.join(os.path.dirname(cur_path), 'testGo')

#1读取用例
excelDir = PATH(config_path + r'\数据.xlsx')
#打开excel
workbook = xlrd.open_workbook(excelDir)
#查看所有子表名
workSheet = workbook.sheet_by_name('Sheet1')
#读取一行
workbookNew = copy(workbook)
workSheetNew = workbookNew.get_sheet(0)

for one in range(1,25):
    workSheetNew.write(one, 0, one)  # 写单元格
    workSheetNew.write(one, 1, random.randint(1000, 10000))  # 写单元格
    workSheetNew.write(one, 2, random.randint(1, 50))  # 写单元格
    workSheetNew.write(one, 3, random.randint(1, 30))  # 写单元格

workbookNew.save(PATH(config_path + r'\假数据.xls'))