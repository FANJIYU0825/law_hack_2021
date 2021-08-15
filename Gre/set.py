# 這邊url_tool 你需要使用 
### colab 才需要~~~~~
!apt update
!apt install chromium-chromedriver
!pip install selenium
###
!pip install fake_useragent
from fake_useragent import UserAgent
import pytest
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unicodedata

from fake_useragent import UserAgent

ua = UserAgent()
import requests 
import xml
from bs4 import BeautifulSoup
import time
import re
import math
from fake_useragent import UserAgent
import time
import random
df = pd.DataFrame() 
mutil_json = []
row_datas =[]
link = []
df_a =pd.DataFrame()
for i in range(len(url)): 
    print(i)
    data= pd.DataFrame()
    # time.sleep(1)
    Url = url[i]
    ua = UserAgent()
    
    time.sleep(1)
    user_agent = ua.random
    headers = {'user-agent': user_agent}
    link.append(url[i])
    num1 = random.randint(3,8)
    time.sleep(num1)
    # time.sleep(1)
    inside = requests.get(Url,headers=headers)
    a = re.findall(r'pkid=\w+%\w+%\w+%\w+%\w+%\w+%\w+%\w+%\w+',inside.text)
    
    js_path="https://law.judicial.gov.tw/controls/GetJudRelatedLaw.ashx?"+a[0]
    data["json"] = [js_path]
    detail = BeautifulSoup(inside.text, 'lxml')
    mutil_json.append(js_path)
    # row_html.append(detail)
    # print(detail)
    
    
    
    

    
    # text.append(a.group())
    value_law = detail.find_all('tr') 
    
    

     
          
    search_row = [unicodedata.normalize('NFKC', value_law[x].text) for x in range (len(value_law)) if value_law[x].text  != '' ]
    strmain =[ ''.join(search_row[i].split()) for i in range(len(search_row))]
    
    #  [unicodedata.normalize('NFKC', str(value_law[x].text) 
    #  for x in range (len(value_law))  if value_law[x].text  != ''  and value_law[x].text  != value_law[x+1].text]  ]
    print(strmain[0:10])
    data["strmain"] =strmain
    row_datas.append(strmain)
    # text_datas.append(text_row)
    # histroy flag  may be can use more colunm
    data['url'] = url[i]
  # will try to get history flag but it will return null 
  # need chance to get it 
    data.to_csv(f"/content/drive/MyDrive/爬蟲/LAWHACK/107id:{a[0]}.csv")
    
    
df_a["Url"] =link
df_a['GetJudRelat'] = mutil_json
df_a['search_rows'] = row_datas      

  
  
# df["row_html"] = row_html 

path = f'/content/drive/MyDrive/爬蟲/LAWHACK/108detailv2.csv'


df.to_csv(path)

print("done")
