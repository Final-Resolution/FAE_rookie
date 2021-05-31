#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import pandas as pd
import os
import re

if __name__ == '__main__':
    Folder_Path = '.\\data\\'

    writer = pd.ExcelWriter('./out.xlsx')

    os.chdir(Folder_Path)
    file_list = os.listdir()

    for item in file_list:
        sheetname = item.split('_')[0]
        data = pd.read_table(Folder_Path+item, sep=',', encoding='GBK')
        data.to_excel(writer, sheetname, index=False)

    writer.save()
