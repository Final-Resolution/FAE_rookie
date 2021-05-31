# -*- coding:utf-8 -*-
import csv
import numpy as np

with open('data.csv') as csv_file:
    row = csv.reader(csv_file, delimiter=',')  # 分隔符方式

    next(row)  # 读取首行
    leftDataProp = []  # 创建一个数组来存储数据

    # 读取除首行以后每一行的第1列数据，并将其加入到数组leftDataProp之中
    for r in row:
        leftDataProp.append(float(r[0]))  # 将字符串数据转化为浮点型加入到数组之中

print('方差:', np.var(leftDataProp))   # 输出方差
print('均方差:', np.std(leftDataProp))   # 输出均方差
print('均值:', np.mean(leftDataProp))  # 输出均值
print('最大值:', np.max(leftDataProp))  # 输出最大值
print('最小值:', np.min(leftDataProp))  # 输出最小值
