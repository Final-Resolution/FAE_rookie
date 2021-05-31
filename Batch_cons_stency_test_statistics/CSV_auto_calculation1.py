# -*- coding:utf-8 -*-
import csv
import numpy as np
import os 

path = ".\\sensor-data\\"
#获取该目录下的所有文件，并存入列表中
csv_list = os.listdir(path)
csv_num = 0
for csv_num in range(len(csv_list)):
    with open(path + '\\' + csv_list[csv_num]) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')  # 分隔符方式
        #获取表头
        header_list = list(next(reader))
        
        leftDataProp = []  # 创建一个数组来存储数据
        
        n = 0
        for n in range(7):
            # 读取除首行以后每一行的第1列数据，并将其加入到数组leftDataProp之中
            for r in reader:
                leftDataProp.append(float(r[n]))  # 将字符串数据转化为浮点型加入到数组之中
            print('当前列为：', header_list[n])
            print('方差:', np.var(leftDataProp))   # 输出方差
            print('均方差:', np.std(leftDataProp))   # 输出均方差
            print('均值:', np.mean(leftDataProp))  # 输出均值
            print('最大值:', np.max(leftDataProp))  # 输出最大值
            print('最小值:', np.min(leftDataProp))  # 输出最小值
            n+=0
    print("CSV:", csv_list[csv_num], "is OK!")
    csv_num+=1

