from aiohttp import ClientSession
from bs4 import BeautifulSoup
import asyncio
import time
import pandas as pd
import re
import random
import unicodedata
import time
import pandas  as pd 
import os
from aiohttp.client import request
import pandas as pd
import requests
import re


import sys


# path2 = "./108detail/"
# df = pd.DataFrame()
# file_paths = os.listdir(path2)
# for i in range(0,len(file_paths)):
#     try:
#         value = pd.read_csv(path2+file_paths[i])
#         df = df.append(value ,ignore_index='false')

#     ### Do Some Stuff
#     except:
#             continue
#        # or pass
df = pd.read_csv("106law.csv")


c = df.url
head = 'https://law.judicial.gov.tw/FJUD/'
df_com = pd.read_csv("./outside/106_outside.csv")
like  = [head+i for i in df_com.URL]


#定義協程(coroutine)
async def main():
    
    # links = set(like)-set(c)
    links= list(like)
    
    # links= list(b)
    df_new = pd.DataFrame()
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch(link, session)) for link in links]  # 建立任務清單
        await asyncio.sleep(2)
        group = await asyncio.gather(*tasks)  # 打包任務清單及執行
        print(len(asyncio.all_tasks()))
        # print(group)

        df_new = df_new.append(group,ignore_index=True)
        return df_new
#定義協程(coroutine)

async def fetch(link, session):
    
    try:
        async with session.get(link) as response:  #非同步發送請求
        

           
            html_body = await response.text()
            df = pd.DataFrame()
            df['url'] =[link]
            n= random.randint(1,5)
            
            await asyncio.sleep(n)
            print("==")
            print(link)
            print("==")
            row_html = []
            
            row_datas = []
            
            
            
            

            soup = BeautifulSoup(html_body, "lxml")  # 解析HTML原始碼
        
            
            row_html.append(soup)

            a = re.findall(r'pkid=\w+%\w+%\w+%\w+%\w+%\w+%\w+%\w+%\w+',html_body)
            
            
                
                        
                # text.append(a.group())
            value_law = soup.find_all('tr') 
            
            search_row = [unicodedata.normalize('NFKC', value_law[x].text) for x in range (len(value_law)) if value_law[x].text  != '' ]
            row_datas.append(search_row)

            
            df['search_rows'] = row_datas      
           
            
            df["row_html"] = row_html
            
            a= random.randint(1,3)
            time.sleep(a)
            
            # df.to_csv(f"./108detail/108{id}_detail.csv", index = False)
            
            return df
    
    except Exception as e:

            print(e)
df_add = pd.DataFrame()
start_time = time.time()
loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)

# loop.run_until_complete(main())  #執行協程(coroutine)
# # links = set(b)-set(a)
result = loop.run_until_complete(main()) 
df_add = df_add.append(result,ignore_index=True)
conn = lite.connect('law.db')
c = conn.cursor()

import sqlite3 as lite
df_add.to_sql('law_main106', conn, if_exists='append', index = False)
# import sqlite3
# conn = sqlite3.connect('billionaire.db')  #建立資料庫
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE detail(url, search_rows, row_html,year)')  #建立資料表
# df_add.to_sql(df_add,"106detail",conn =conn ,if_exists='append',index_label=[0])

 
#如果資料表存在，就寫入資料，否則建立資料表
# df.to_sql('108_law', conn, if_exists='append', index=False) 
# async def main():
   
#     links = df_row.url
    
#     async with ClientSession() as session:
#         tasks = [asyncio.create_task(fetch(link, session)) for link in links]  # 建立任務清單
        
#         await asyncio.gather(*tasks)  # 打包任務清單及執行 
#         #Return Task  
# async def fetch(link, session):
#         async with session.get(link) as response:  #非同步發送請求
#             html_body = await response.text()
#             # 想要 Return  html_body


        
        