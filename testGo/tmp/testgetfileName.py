# import os
# def file_name(file_dir):
#   for root, dirs, files in os.walk(file_dir):
#     print(root) #当前目录路径
#     print(dirs) #当前路径下所有子目录
#     print(files) #当前路径下所有非目录子文件
#     # for i in range(0,len(files)):
#     #     print(files[i])
#
# file_name(r'C:\Users\Administrator\Desktop\图标1_slices')


from flask import  Flask

app = Flask(__name__)

@app.route('/post',methods = ['POST'])
def test_post():
    return 'post'


if __name__ == '__main__':
    app.run('127.0.0.1','9090')