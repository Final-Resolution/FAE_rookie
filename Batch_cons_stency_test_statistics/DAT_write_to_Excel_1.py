# -*- coding: utf-8 -*-
"""
@author: FinalRun
"""
import pandas as pd
import os
import re 



if __name__ == "__main__":
    path0 = ".\\data0\\"
    #获取该目录下的所有文件，并存入列表中
    file_list = os.listdir(path0)
    file_num = 0

    for file_num in range(len(file_list)):
        num = re.split("[_.]", file_list[file_num])[-1]
        n = 0
        path = path0 + file_list[file_num]
        #获取测试目录下的所有DAT文件，并存入列表中
        dat_list = os.listdir(path)
        with pd.ExcelWriter(r'.\\QMA6100_'+ str(num) + '_'+ str(n) + '.xlsx') as writer:
            dat_num = 0
            for dat_num in range(len(dat_list)):
                dire = re.split("[_.]", dat_list[dat_num])[-2]
                #读取DAT数据文件
                df = pd.read_csv(path + '\\' + dat_list[dat_num], sep = "\s+", header=None, 
                names=["ACC","X","Y","Z","Step"])
                #删除第0行
                df.drop(0, inplace=True)
                #删除最后一行
                df.drop(df.tail(1).index, inplace=True)
                df.to_excel(writer, index = False, sheet_name=dire)
                dat_num+=1
            n+=1
        print("QMA6100:", num, "is OK!")
        file_num+=1

