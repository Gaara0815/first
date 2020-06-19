import time
#普通测试
def hello():
    print('hello')
    print('hello1')
    print('哈'*500)
    print(a[5])
    print(a[5:len(a)-1])
# a = 'aaa's
a = 'h&t&t&p&s:&//&m&3347&.&g&i&t&h&u&b&.&i&o'
# b = a.replace('&', '')
import random
b = a[random.randint(0,len(a)-1)]
x = random.randint(0,9)
print(b)
print(x)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print('哈'*500)
# hello()