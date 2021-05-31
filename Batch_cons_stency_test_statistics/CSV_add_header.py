# -*- coding: utf-8 -*-

import pandas as pd
import re
import os

path = '.\\sensor-data\\'
#获取该目录下的所有文件，并存入列表中
csv_list = os.listdir(path)
csv_num = 0
for csv_num in range(len(csv_list)):  
    df = pd.read_csv(path + '\\' + csv_list[csv_num],header=None,
                     names=['Acc-X','Acc-Y','Acc-Z','Gyro-X','Gyro-Y','Gyro-Z','Temp'])
    '''
    #删除第0行
    df.drop(0, inplace=True)
    #删除最后一行
    df.drop(df.tail(1).index, inplace=True)
    '''
    df.to_csv(path + '\\' + csv_list[csv_num],index=False)
    print("CSV:", csv_list[csv_num], "is OK!")
    csv_num+=1

