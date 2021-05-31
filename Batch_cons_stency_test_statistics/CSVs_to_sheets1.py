#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import pandas as pd
import os
import re
import chardet

# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']


if __name__ == '__main__':
    file_name = input("请输入需要合并的文件名：")
    csv_path = '.\\' + str(file_name) + '\\'
    list = os.listdir(csv_path)  # 列出文件夹下所有的目录与文件
    encoding = get_encoding(csv_path + list[0])
    writer = pd.ExcelWriter(file_name + '_out''.xlsx')
 
    for i in range(0,len(list)):
        
        data = pd.read_csv(csv_path + list[i], encoding=encoding, skiprows=1,
                           header=None, error_bad_lines = False,warn_bad_lines=True)
        data.to_excel(writer, sheet_name=list[i], index = False, header=None)
        print("正在合并文件: " + str(list[i]))
    print("正在保存文件!" )
    writer.save()
