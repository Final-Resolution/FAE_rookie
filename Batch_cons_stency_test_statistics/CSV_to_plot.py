import csv
import matplotlib.pyplot as plt
#from datetime import datetime




filename = 'test.csv'
'''
exampleFile = open(filename)  # 打开csv文件
exampleReader = csv.reader(exampleFile)  # 读取csv文件
exampleData = list(exampleReader)  # csv数据转换为列表
length_zu = len(exampleData)  # 得到数据行数
length_yuan = len(exampleData[0])  # 得到每行长度
'''
with open(filename) as f:
    #创建一个与该文件相关联的reader对象
    reader=csv.reader(f)
    #只调用一次next()方法，得到文件的第一行，将第一行数据中的每一个元素存储在列表中
    header_row=next(reader)
    Data_list = list(reader)  # csv数据转换为列表
    length_zu = len(Data_list)  # 得到数据行数
    length_yuan = len(Data_list[0])  # 得到每行长度


# for i in range(1,length_zu):
#     print(exampleData[i])

x = list()
y = list()

for i in range(1, length_zu):  # 从第二行开始读取
    x.append(Data_list[i][5])  # 将第一列数据从第二行读取到最后一行赋给列表x
    #y.append(Data_list[i][1])  # 将第二列数据从第二行读取到最后一行赋给列表

#设置图形的格式
    
#调整绘图大小，避免坐标重叠
plt.figure(figsize=(10, 6))
#绘制x,y的折线图
plt.plot(x)  
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#这是字体大小和标签
plt.title("Add title!",fontsize=16)
#X轴暂不设置标签
plt.xlabel('',fontsize=16)
#设置标签
plt.ylabel(header_row[5] + "(mg/s2)",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=10)

plt.savefig('.\\output.png',dpi=800) # 保存图片

plt.show()  # 显示折线图

