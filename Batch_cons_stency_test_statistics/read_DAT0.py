# -*- coding: utf-8 -*-
"""
@author: FinalRun
"""
import pandas as pd
#from openpyxl import load_workbook,Workbook
#import xlwt,os,xlrd


path = "./"

#读取DAT数据文件
df = pd.read_csv(path+"QMA6100_1.DAT", sep = "\s+", header=None, 
names=["ACC","X","Y","Z","Step"])

'''
DataFrame.drop(labels=None,axis=0, index=None, columns=None, inplace=False)
删除含有指定元素的行或列，或删除指定行，列
参数说明：
labels 就是要删除的行列的名字，用列表给定
axis 默认为0，指删除行，因此删除columns时要指定axis=1；
index 直接指定要删除的行
columns 直接指定要删除的列
inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
inplace=True，则会直接在原数据上进行删除操作，删除后无法返回。
df.drop(df.tail(n).index) 从尾部去掉 n 行
df.drop(df.head(n).index) 从头去掉 n 行
'''
#删除第0行
df.drop(0, inplace=True)
#删除最后一行
df.drop(df.tail(1).index, inplace=True)
dire_name = "x+"
#df.to_excel("./DATA.xlsx",index = False, sheet_name=dire_name)


with pd.ExcelWriter(r'.\\DATA0.xlsx') as writer:
    df.to_excel(writer, index = False, sheet_name='x+')
    df.to_excel(writer, index = False, sheet_name='x-')

    df.drop(df.tail(10).index, inplace=True)
    df.to_excel(writer, index = False, sheet_name='y+')
    df.to_excel(writer, index = False, sheet_name='y-')

