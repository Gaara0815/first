import requests
from pprint import pprint
import MySQLdb

# res = requests.post(
#     'http://115.236.35.106:9000/api/n/guest/login',
#     data={
#
#     }
#
# )
#
# pprint(res.json())

conn = MySQLdb.connect(#创建连接
    host= '192.168.0.136',
    user = '用户名',
    password = '密码',
    da = '库名',
    charset = 'utf8'
)

c = conn.cursor()

# c.execute('select * from 表名')#读取表数据
# row = c.fetchone()#返回一条数据
# print(row)

# for i in range(c.rowcount):#循环
#     row = c.fetchone()  # 返回一条数据
#     print(row)

row = c.fetchall()  # 返回所有数据
row = c.fetchmany(100)#读取多少条
print(row)

conn.commit()#修改数据后

conn.close()#关闭数据库




















