import random
import os
import re
import os.path

filepath = input("请输入需要重命名的文件夹路径：")
path = './' + str(filepath) + '/' #目标文件夹
listname = os.listdir(path) #遍历目录
for n in listname:
    print(n)
    temp1 = random.randint(1000000, 9999999) #此处没有容错，可能会出现循环过程中随机数一样而造成文件被覆盖的现象，两个随机数的组合能降低这种风险，并且训练GAN时，丢失几个数据也是无关紧要的
    temp2 = random.randint(10000000, 99999999)
    oldname = os.path.join(path, n)
    newname = os.path.join(path, str(temp1) + str(temp2) + '.csv') #我的数据后缀是'.png'
    os.rename(oldname, newname)
