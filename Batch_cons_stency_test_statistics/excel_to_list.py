# -*- coding:utf-8-*-
import numpy as np
import pandas as pd

df = pd.DataFrame(pd.read_excel('test2.xlsx')) #pd.dataframe

df_data = np.array(df) #np.ndarray()
df_list=df_data.tolist() #list
print(df_list)
print(type(df_list))
