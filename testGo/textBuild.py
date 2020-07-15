import os
import random

def getIMEI(length):
    a = ''
    str = "1234567890";
    for one in range(0, length):
        number = random.randint(0, len(str)-1)
        a = a + (str[number])
    return a

def getIDFA(length):
    a = ''
    str = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for one in range(0, length):
        if(one==8 or one==13 or one==18 or one==23):
            number = '-'
        else:
            number = str[random.randint(0, len(str)-1)]
        a = a + number
    return a

def getMAC(length):
    a = ''
    str = "1234567890ABCDEFabcdef";
    for one in range(0, length):
        if (one == 2 or one == 5 or one == 8 or one == 11 or one == 14):
            number = ':'
        else:
            number = str[random.randint(0, len(str) - 1)]
        a = a + number
    return a

#txt数据处理
# txtName = "IMEI300.txt"
txtName = "IDFA30000000.txt"
# txtName = "MAC29999999.txt"
f=open(txtName, "a+")
start = time.time()
for i in range(0,29999999):
    # new_context = getIMEI(15) + '\n'
    new_context = getIDFA(36) + '\n'
    # new_context = getMAC(17) + '\n'
    f.write(new_context)
f.close()
end = time.time()
print(end-start)


