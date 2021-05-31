# -*- coding: utf-8 -*-

'''
    该脚本用以批量重命名CSV文件，可根据实际需求更改
'''
import os
import re
import os.path



if __name__ == '__main__':
    filepath = input("请输入需要重命名的文件夹路径：")
    chip_num = input("请输入当前芯片的编号：")
    path = './' + str(filepath) + '/'
    num= 1
    for file in os.listdir(path):
        os.rename(os.path.join(path,file),
                  os.path.join(path,str(chip_num) + "_" + str(num)+".csv"))
        num+=1
    print("重命名完毕！")
