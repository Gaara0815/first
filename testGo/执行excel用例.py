import  xlrd #第三方库 读取excel
import  xlutils#
from xlutils.copy import copy#复制函数

excelDif = r'C:\Users\Administrator\Desktop\测试用例.xlsx'
wordbook = xlrd.open_workbook(excelDif)

print(wordbook.sheet_names())#查看所有字表名 返回的是list


#打开excel
workbookWr = xlrd.open_workbook(excelDif)
#复制
workbk2 = copy(workbookWr)
wrSheet = workbk2.get_sheet(1)
wrSheet.write(1,2,'hhh')#写单元格
workbk2.save(r'C:\Users\Administrator\Desktop\测试用例1.xlsx')