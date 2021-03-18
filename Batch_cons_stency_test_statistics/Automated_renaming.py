#!/usr/bin/python3
'''
陀螺仪测试数据整理，根据测试数据文件的内容来判断该数据文件的方向属性
本版本因通过识别文件名做为索引，需在数据目录下创建"QMA6100_0"文件夹
'''

import os
import re
import os.path
import numpy as np
'''
获取当前目录的中的芯片标号，并返回
'''
def get_chip_num(path):
    # 拆分路径，文件名
    file_path, file_name = os.path.split(path)
    #print(file_path)
    #print(file_name)
    #print("---------------------------------------")
 
    # 拆分文件名，后缀名
    short_name, extension = os.path.splitext(file_name)
    #print(short_name)
    #print(extension)
    #print("---------------------------------------")
 
    # 获取上层路径
    parent_path, parent_name = os.path.split(file_path)
    #print(parent_path)
    #print(parent_name)
    #print("---------------------------------------")
    s = parent_name
    l = len(s) 
    numbers = []
    i = 0
    while i < l:
        num = ''
        symbol = s[i]
        while '0' <= symbol <= '9': # symbol.isdigit()
            num += symbol
            i += 1
            if i < l:
                symbol = s[i]
            else:
                break
        i += 1
        if num != '':
            numbers.append(int(num))
    chip_num = numbers[1]
    return  chip_num

def get_lines(file_path):
    #逐个读取DAT文件首行
    with open(file_path, 'r', encoding='utf-8') as f:  # 打开文件
        lines = f.readlines()  # 读取所有行
        first_line = lines[2]  # 取第一行
        last_line = lines[-2]  # 取最后一行
        data = first_line.split()
    return data

def rename(num, dire):
    n=0
    for i in fileList:
        #设置旧文件名（就是路径+文件名）
        oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符
        #设置新文件名
        newname=path + os.sep +'QMA6100_'+str(num)+'_'+str(dire)+str(n)+'.DAT'
        os.renames(oldname,newname)   #用os模块中的rename方法对文件改名
        print(oldname,'======>',newname)
        n+=1
            


'''
#a_float_new = list(map(safe_float, a))
'''
def safe_float(number):
    try:
        return float(number)
    except:
        return None
'''
获取坐标种类
'''
def get_coor(max_index):
    if max_index == 0:
        coor = 'x'
    elif max_index == 1:
        coor = 'y'
    elif max_index == 2:
        coor = 'z'
    return coor

'''
获取坐标方向
'''
def get_dire(max_index):
    if (max_index != 0 ):
        if(max_index > 0):
            dire = '+'
        if(max_index < 0):
            dire = '-'
    else:
        print('WoW!!!')
    return dire
    



if __name__ == "__main__":
    file_num = 1
    path0 = "Basic_test_data\\"
    #获取该目录下的所有文件，并存入列表中
    fileList0 = os.listdir(path0)
    data = []
    n = 0
    
    for file_num in range(len(fileList0)):        
        path = path0 + 'QMA6100_' + str(file_num) +'\\'
        #获取该目录下的所有文件，并存入列表中
        fileList = os.listdir(path)
        for n in range(len(fileList)):
            #首先对第一个文件进行处理测试
            file_path = path + fileList[n]
            #获取当前目录的芯片编号
            chip_num = get_chip_num(path)
            #print('chip_num :',chip_num)
            #获取第一个文件首行的内容
            data = get_lines(file_path)
            #删除第一个元素
            data.pop(0)
            #删除最后一个元素
            data.pop(3)
            #将列表转换为float类型
            data_float = map(float, data)
            data_float = list(data_float)
            #将列表取绝对值
            data_float_abs = list(map(abs,data_float))
            #获取列表中的排序列表,comp_list为从小到大的索引列表
            a = np.array(data_float_abs)
            comp_list = list(np.argsort(a))
            #获取该文件的坐标值
            coor = get_coor(comp_list[2])
            #获取该文件的方向值
            dire = get_dire(data_float[comp_list[2]])
            dire = coor + dire
            #print('dire:' ,dire)
            #重命名
            #设置旧文件名（就是路径+文件名）
            oldname=path+ os.sep + fileList[n]   # os.sep添加系统分隔符
            #设置新文件名
            newname=path + os.sep +'QMA6100_'+str(chip_num)+'_'+dire+'.DAT'
            os.renames(oldname,newname)   #用os模块中的rename方法对文件改名
            #print(oldname,'======>',newname)
            n+=1            
        file_num+=1
        print("QMA6100:" , str(file_num), "is OK!")
        
            
    
    
