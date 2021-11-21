from bs4 import BeautifulSoup
import grequests
import time
import pandas as pd 
import re
import random
df= pd.read_csv("./final/106_final.csv")
 

df = df.rename(columns={"0": 'url'})
links = df.url
df_new = pd.DataFrame()
start_time = time.time()
reqs = (grequests.get(link,stream=False) for link in links[:1])  # 建立請求集合

 

# response = grequests.imap(reqs, grequests.Pool(4))  # 發送請求
response = grequests.imap(reqs) 
for r in response:
    soup = BeautifulSoup(r.content, "lxml")
    print(len(soup))
      # 解析HTML原始碼
    r.close()
    
    #找出標題
    contents =soup.find_all('td')
    #我這邊是使用生程式 去撰寫  但是這方法不一定好用
    #I 
    id_list =[contents[x].text for x in range(len(contents)) if x%5 == 0]
    v_court_list=[contents[x].text for x in range(len(contents)) if x%5 == 1]
    date_list=[contents[x].text for x in range(len(contents)) if x%5 == 2]
    jugetile_list=[contents[x].text for x in range(len(contents)) if x%5 == 3]
    jugeintro_list=[contents[x].text for x in range(len(contents)) if x%5 == 4]
    jugeurl_list = [contents[x].find('a').get('href') for x in range(len(contents)) if x%5 == 1]
    df = pd.DataFrame()

    df['court'] = v_court_list
        # print(contents)
    # v_court = []
    # compile=re.compile(r"臺\w+\s?\w*院")
        
    # a = re.findall(compile,v_court_list)
    
    # v_court.append(a[0])

    
    # df['court'] = v_court
    df['Date'] = date_list
    d = df['Date']
    for i in range(len(d)):
        d.iloc[i]=d.iloc[i].replace(d.iloc[i][0:3], str(int(d.iloc[i][0:3]) + 1911))
    d=pd.to_datetime(d,format='%Y/%m/%d')
    df['Date']=d
    df['Year'] = df['Date'].dt.year 
    df['title'] = jugetile_list
    df['jugeintro'] = jugeintro_list
    # I will want to add more data inside
    df['URL'] = jugeurl_list
    head = 'https://law.judicial.gov.tw/FJUD/'
    url = head+df.URL
    df['URL'] = url
    df_new = df_new.append(df,ignore_index=True)
    #用random 去跑  模擬
    n= random.randint(1,5)
    time.sleep(n)
    
    court = df_new['court'][0] 
    print ("done"+court) 
print ("Done"+court)
court = df_new['court'][0] 
court = str(court)
print(df_new.head())
df_new.to_csvv(f"./crawData_outside106/106.csv")   
    
  


print("花費：" + str(time.time() - start_time) + "秒")