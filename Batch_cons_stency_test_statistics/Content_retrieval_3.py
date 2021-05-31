#!/usr/bin/python
#coding = UFT-8

import pandas as pd
from pandas import DataFrame
import numpy as np
import sys
import os
import re
import time

def find_row(file_name):
    """
    Returns the row number based on the value of the specified cell
    """
    row_list = []
    courier_list = []
    courier_file = "courier1.txt"
    print("正在导入快递单号列表！")
    courier_pd = pd.read_table(courier_file,header = None, encoding = "utf-8")
    content = courier_pd
    demo_df = pd.read_excel(file_name, sheet_name = "QST_final_bill", usecols=[1])
    #demo_df = pd.read_excel(file_name, sheet_name = "Sheet1")
    print("正在搜索！")
    a = 0
    for a in  range(len(courier_pd)):
        num_value = content[0][a]
        for indexs in demo_df.index:
            for i in range(len(demo_df.loc[indexs].values)):
                if (str(demo_df.loc[indexs].values[i]) == num_value):
                    row = str(indexs+2).rstrip('L')
                    row_list.append(row)
                    #print(row_list)
                    print("内容：" + num_value + " 编号：" + str(a) + " 已检索成功！")
    return row_list

def delete_row(file_name, row_list):
    #对列表进行去重，防止程序崩溃
    row_list = list(set(row_list))
    #对列表进行降序排列，首先删除尾部行
    row_list.sort(reverse=True)
    df = pd.read_excel(str(file_name), sheet_name = "QST_final_bill")
    #df1 = df.drop([int(row_num)-2], axis=0, inplace = False) #删除第n行，inplace=True则原数据发生改变
    for i in range(len(row_list)):
        df.drop([int(row_list[i])-2], axis=0, inplace = True)
        print("已删除文件：" + file_name + " 中的第 " + str(int(row_list[i])-2) + " 行" )
    # 保存数据
    print("正在保存文件，请稍后！")
    df.to_excel('example.xlsx', sheet_name='QST_final_bill', index=False, header=True)




if __name__ == "__main__":
    start = time.time()

    # 首先将pandas读取的数据转化为array
    #courier_array = np.array(courier_pd)
    # 然后转化为list形式
    #courier_list =courier_array.tolist()

    # 待检索母表路径
    file_name = 'Out0.xlsx'
    #content = input("请输入需要检索的内容：")
    #content = courier_pd[0][2901]
    #content = courier_pd
    #print("正在搜索内容：" + content)
    row_list = find_row(file_name)
    #print('内容: \"' + str(content) + '\"所在行数为：' + row_num)
    delete_row(file_name, row_list)
    end = time.time()
    print("程序已运行完毕，总共用时：",end-start,"s")
