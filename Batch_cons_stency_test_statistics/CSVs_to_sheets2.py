#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import pandas as pd
import os
import re
import chardet
import time


# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']


if __name__ == '__main__':
    start = time.time()
    file_name = input("请输入需要合并的文件名：")
    csv_path = '.\\' + str(file_name) + '\\'
    list = os.listdir(csv_path)  # 列出文件夹下所有的目录与文件
    encoding = get_encoding(csv_path + list[0])
    #使用lambda表达式进行key排序
    list.sort(key=lambda x:int(x.split(str(file_name + '_'))[1].split('.csv')[0]))
    #encoding = get_encoding(csv_path + list[0])
    writer = pd.ExcelWriter('data_' + file_name + '_out''.xlsx')
 
    for i in range(0,len(list)):
        
        data = pd.read_csv(csv_path + list[i], encoding=encoding, skiprows=1,
                           header=None, error_bad_lines = False,warn_bad_lines=True)
        data.to_excel(writer, sheet_name=list[i], index = False, header=None)
        print("正在合并文件: " + str(list[i]))
    print("正在保存文件!" )
    writer.save()
    end = time.time()
    print("程序运行完毕！总共用时：" + str(end-start) + "s")
