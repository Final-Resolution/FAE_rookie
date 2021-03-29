# python批量更换后缀名
import os
import sys
os.chdir(r'./test')

# 列出当前目录下所有的文件
files = os.listdir('./')
print('files',files)

for fileName in files:
	portion = os.path.splitext(fileName)
	# 如果后缀是.dat 
	if portion[1] == ".DAT":
		#把原文件后缀名改为 txt
		newName = portion[0] + ".txt" 
		os.rename(fileName, newName)
