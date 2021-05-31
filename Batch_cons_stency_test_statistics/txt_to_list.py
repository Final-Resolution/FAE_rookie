#!/usr/bin/python
#coding = UFT-8
import sys
import codecs
import numpy as np
import pandas as pd
from pandas import DataFrame


courier_list = []
file_list = open("courier0.txt", "r", encoding = "utf-8")
 
#for line in file_list.readlines():
#    courier_list.append(list(map(str, line.split(" "))))
#print(courier_list)

courier_pd = pd.read_table('courier.txt',header = None)
#courier_list = courier_pd.values.tolist()
# 首先将pandas读取的数据转化为array
courier_array = np.array(courier_pd)
# 然后转化为list形式
courier_list =courier_array.tolist()




#with codecs.open('courier.txt','r',encoding='utf-8') as fin:
#    print(fin.read().replace('','').encode('utf-8','ignore').decode('utf-8'))



