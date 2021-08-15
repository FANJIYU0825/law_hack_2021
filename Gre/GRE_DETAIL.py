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
from pandas.io import sql
from pandas.core import indexing
from pandas.core.frame import DataFrame
import aiohttp 
import requests
import re
#import mysql.connector
import sqlite3 as lite
import sys
# import asqlite3
from fake_useragent import UserAgent
import sqlite3 as lite
ua = UserAgent()
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
# a= df.url

df_com = pd.read_csv("./outside/107_outside.csv")
b= df_com.URL
head = 'https://law.judicial.gov.tw/FJUD/'
urls = [head+i for i in b]
sys.setrecursionlimit(len(b))


#定義協程(coroutine)
async def main(n):
    
    # links = set(b)-set(a)
    # links= list(links)
    # links= list(b)
    
    user_agent = ua.random
    headers = {'user-agent': user_agent}
    aiohttp.CookieJar(unsafe=True)
    #request for data
    async with ClientSession(headers =headers) as session:
        
        df_new = pd.DataFrame()    
        #這邊我們會特別去補料106 年
        #                                        
        # tasks = [asyncio.create_task(fetch(link, session)) for link in urls[2489:2489+n ]] # 建立任務清單
        
        # gropu1 = await asyncio.gather(*tasks)
        # time.sleep(100)
        # df_new = df_new.append(gropu1 ,ignore_index='false')
        
        # tasks = [asyncio.create_task(fetch(link, session)) for link in urls[2489+n:2489+n+1 ]] # 建立任務清單
        
        # gropu1 = await asyncio.gather(*tasks)
        # time.sleep(100)
        # df_new = df_new.append(gropu1 ,ignore_index='false')
        # n+=1
        #here you schedule to run my code
        tasks6 = [asyncio.create_task(fetch(link, session)) for link in urls[+n:100+n]]  # 建立任務清單
        gropu6 = await asyncio.gather(*tasks6)
        time.sleep(100)
        df_new = df_new.append(gropu6 ,ignore_index='false')
        time.sleep(100)
        tasks7 = [asyncio.create_task(fetch(link, session)) for link in urls[100+n:200+n]]  # 建立任務清單
        gropu7 = await asyncio.gather(*tasks7)
        time.sleep(100)
        df_new = df_new.append(gropu7 ,ignore_index='false')
        
        tasks8 = [asyncio.create_task(fetch(link, session)) for link in urls[200+n:300+n]]  # 建立任務清單
        gropu8  = await asyncio.gather(*tasks8)
        time.sleep(100)
        df_new = df_new.append(gropu8 ,ignore_index='false')
        time.sleep(100)
        tasks9 = [asyncio.create_task(fetch(link, session)) for link in urls[300+n:400+n]]  # 建立任務清單
        gropu9 =  await asyncio.gather(*tasks9)
        time.sleep(100)
        df_new = df_new.append(gropu9 ,ignore_index='false')

        df_new = df_new.append(gropu9 ,ignore_index='false')
        tasks2 = [asyncio.create_task(fetch(link, session)) for link in urls[500+n:600+n]]  # 建立任務清單
        gropu2=await asyncio.gather(*tasks2)
        time.sleep(100)
        df_new = df_new.append(gropu2 ,ignore_index='false')
        
        tasks3 = [asyncio.create_task(fetch(link, session)) for link in urls[600+n:700+n]]  # 建立任務清單
        gropu3 = await asyncio.gather(*tasks3)
        time.sleep(100)
        df_new = df_new.append(gropu3 ,ignore_index='false')
        tasks3a = [asyncio.create_task(fetch(link, session)) for link in urls[700+n:800+n]]  # 建立任務清單
        gropu3a = await asyncio.gather(*tasks3a)
        df_new = df_new.append(gropu3a ,ignore_index='false')
        
        tasks4 = [asyncio.create_task(fetch(link, session)) for link in urls[800+n:900+n]]  # 建立任務清單
        gropu4 = await asyncio.gather(*tasks4)
        
        df_new = df_new.append(gropu4 ,ignore_index='false')
        tasks5 = [asyncio.create_task(fetch(link, session)) for link in urls[900+n:1000+n]]  # 建立任務清單
        gropu5 = await asyncio.gather(*tasks5)
        time.sleep(100)
        df_new = df_new.append(gropu5 ,ignore_index='false')
        

 
        
        
        
        
        
        
       
       
        
        
        return  df_new
        
#定義協程(coroutine)

async def add_data (url,Search_row):
    
    c = conn.cursor()
    sqls  =f"INSERT INTO law_main  VALUES(?,?)",(url,Search_row)
    time.sleep(3)
    c.execute(sqls)
    time.sleep(4)
    conn.commit()
    time.sleep(5)
async def fetch(link, session):
    
    try:
        n= random.randint(1,4)
        time.sleep(5)
        queue = asyncio.Queue()
        async with session.get(link) as response:  #非同步發送請求
            time.sleep(5)
            assert response.status == 200

            

            html_body = await response.text()
            
            n= random.randint(1,5)
            
            
            print("==")
            print(link)
            print("==")
            row_html = []
            
            row_datas = []
            
            
            
            

            soup = BeautifulSoup(html_body, "lxml")  # 解析HTML原始碼
        
            # print(soup)
            # row_html.append(soup)

            # a = re.findall(r'pkid=\w+%\w+%\w+%\w+%\w+%\w+%\w+%\w+%\w+',html_body)
            
            
                
                        
                # text.append(a.group())
            value_law = soup.find_all('tr') 
            
            search_row = [unicodedata.normalize('NFKC', value_law[x].text) for x in range (len(value_law)) if value_law[x].text  != '' ]
            strmain =[ ''.join(search_row[i].split()) for i in range(len(search_row))]
            
            #去特殊文字
            
            # #特殊符號補上
            # replacestr = ["├──┼───────────┼─────────────┤│"\
            #   ,'│'\
            #   ,'┌──┬───────────┬─────────────┐'\
            #   ,'──┴───────────┴─────────────┘'\
            #   ,'└']
            # strmain = [strmain[i].replace(f"{replacestr[0]}","")\
            # .replace(f"{replacestr[1]}",'')\
            # .replace(f"{replacestr[2]}",'')\
            # .replace(f"{replacestr[3]}",'') for i in range(len(strmain)) ]
            row_datas.append(strmain)

            data =DataFrame()
            data['url'] =[link]
            data['search_rows'] = row_datas  

            SearchText=data['search_rows'] 
            # SearchText= SearchText.to_list()
            # SearchText = SearchText
            # SearchText = str(SearchText)
            print(SearchText.to_list()[0][0:10])
            
            law_link = str(link)
            add_data(law_link,SearchText)
            # c = conn.cursor()
            # connection = mysql.connector.connect(user='root',
            #                    password='s2380215',
            #                   host='127.0.0.1',
            #                   database='law_hack')
            # cursor = connection.cursor()
            
            
            # sqls  =f"INSERT INTO law_main106_2 (url,search_row) VALUES ('{law_link}','{SearchText}' )"
            

            # cursor.execute(sqls)
            time.sleep(5)
            # c.execute(sqls)
            # async with conn:
        
            #     sqls  =f"INSERT INTO law_main106_2 (url,search_row) VALUES ('{law_link}','{SearchText}' )"

            #     await conn.execute(sqls)
            #     await conn.commit()

            #寫資料庫

            
            #  寫入等待資料寫用
            # conn.commit()
            # cursor.close()
            
            # c.execute(sqls)
            
            # conn.commit()
            # conn.close()
            
            return data
    
    except Exception as e:

            print(e)
df_add = pd.DataFrame()

start_time = time.time()
print(start_time)
# conn = asqlite3.connect('106_law.db')

conn = lite.connect('107_law.db')
# cout_list = [0,1000,2000,3000,4000,5000,6000,7000,8000]
# for i in cout_list:
loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)
result = loop.run_until_complete(main(0)) #執行協程(coroutine)
df_new = df_add.append(result ,ignore_index='false')
df_new.to_csv("107LAWMAIN.csv")
# sql = 'SELECT *  FROM law_main106_2 '
# # sq = c.execute(sql)
# # print(sq)
# df = pd.read_sql(sql,con=conn)
# print(df.url)
conn.close()
# print(result)

# # links = set(b)-set(a)
# loop.run_until_complete(main()) 
# connection.close()  

# try:
#     # 連接 MySQL/MariaDB 資料庫
#     connection = mysql.connector.connect(user='root',
#                     password='s2380215',
#                     host='127.0.0.1',
#                     database='law_hack')
#     cursor = connection.cursor()    
#     loop = asyncio.get_event_loop()  #建立事件迴圈(Event Loop)
#     # loop.run_until_complete(main())  #執行協程(coroutine)
#     # # links = set(b)-set(a)
#     loop.run_until_complete(main()) 
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("資料庫連線已關閉")
        
end = time.time() -start_time     
print(end+"秒")