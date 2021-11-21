import pandas  as pd 
import os
from aiohttp.client import request
import pandas as pd
import requests
import re
import os
# 108{location}page0{108}10.xlsx
# path = './tesdata/'
path2 = "./detail_datas/"
# df_com = pd.read_csv("./109all.csv")
df = pd.DataFrame()
for  i in  os.listdir(path2):
    value = pd.read_csv(path2+i)
    df = df.join(value)
print(df.describe())    
# a= df.url  
# b= df_com

# # print(set(a)&set(b))
# df = pd.read_csv("./detail/105_final.csv")
# # df_row = df.rename(columns={"0": 'url'})
# links = df.url
# df.to_csv('./crawData_outside106/106.csv')
# print(links)