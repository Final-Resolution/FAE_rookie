import pandas as pd
from pandas import DataFrame
import os
import re
import time

def find_row(num_value,file_name):
    """
    Returns the row number based on the value of the specified cell
    """
    demo_df = pd.read_excel(file_name, sheet_name = "QST_final_bill", usecols=[1])
    #demo_df = pd.read_excel(file_name, sheet_name = "Sheet1")
    print("正在搜索！")
    for indexs in demo_df.index:
        for i in range(len(demo_df.loc[indexs].values)):
            if (str(demo_df.loc[indexs].values[i]) == num_value):
                row = str(indexs+2).rstrip('L')
                return row


def delete_row(file_name, row_num):
    df = pd.read_excel(str(file_name), sheet_name = "QST_final_bill")
    df1 = df.drop([int(row_num)-2], axis=0, inplace = False) #删除第n行，inplace=True则原数据发生改变
    print("已删除文件：" + file_name + " 中的第 " + str(row_num) + " 行" )
    # 保存数据
    print("正在保存文件，请稍后！")
    df1.to_excel('example.xlsx', sheet_name='QST_final_bill', index=False, header=True)


if __name__ == "__main__":
    start = time.time()
    file_name = 'test0.xlsx'
    content = input("请输入需要检索的内容：")
    row_num = find_row(str(content),file_name)
    print('内容: \"' + str(content) + '\"所在行数为：' + row_num)
    delete_row(file_name, row_num)
    end = time.time()
    print("程序已运行完毕，总共用时：",end-start,"s")
