def crawing(page):
  head = 'https://law.judicial.gov.tw/'
  #here FJUD need to search qryresultls I want auto
  url_tool = f"/FJUD/qryresultlst.aspx?q=98e3f356f47628974d04d68d8800c1a0&amp;sort=DS&amp;&amp;Page={page}"
  url_tool = head+url_tool
  req = requests.get(url_tool)
  # timeto think the sample of it
  # url = input("query the result of ")
  # req = requests.get(url)
  soup = BeautifulSoup(req.text, 'html.parser')
  query_list = soup.find('div')
  content =query_list.find_all('td')

  id_list=[content[x].text for x in range(len(content)) if x%5 == 0]
  v_court_list=[content[x].text for x in range(len(content)) if x%5 == 1]
  date_list=[content[x].text for x in range(len(content)) if x%5 == 2]
  jugetile_list=[content[x].text for x in range(len(content)) if x%5 == 3]
  jugeintro_list=[content[x].text for x in range(len(content)) if x%5 == 4]
  jugeurl_list = [content[x].find('a')['href'] for x in range(len(content)) if x%5 == 1]
  # MAIN DATA
  df = pd.DataFrame()
  df['court'] = v_court_list
  df['Date'] = date_list
  df['tile'] = jugetile_list
  df['jugeintro'] = jugeintro_list
  df['URL'] = jugeurl_list
  url = df.URL
  row_datas =[]
  text_datas = []
  history_flag = []
  for x in url: 
      
      head = 'https://law.judicial.gov.tw/FJUD/'
      url = head+x
      
      inside = requests.get(url)
      detail = BeautifulSoup(inside.text, 'lxml')
      temp = detail.find('tr')

      value_law = temp.find_all('div') 
      

      search_row = [value_law[x] for x in range (len(value_law)) if value_law[x].text  != '' and value_law[x].text  != value_law[x+1].text]
      # text_row =  [unicodedata.normalize('NFKC', str(value_law[x]) for x in range (len(value_law))  if value_law[x].text  != ''   ]
                  
      row_datas.append(search_row)
      text_datas.append(text_row)
      # 歷史資訊 這邊我會希望可以增加資訊
      badge=detail.find(attrs={"id": "hyPrintHistory"})
      hisv_court= badge.get('href')

      histreq = requests.get(head+hisv_court)
      detail_history = BeautifulSoup(histreq.text, 'lxml')
      count_histroy=len(detail_history.find_all('td'))
      if count_histroy >0 :
        his_flag ='Y'
      else :
        his_flag ='N'
      history_flag.append(his_flag)
  df['search_rows'] = row_datas
  df['history_flag'] = history_flag
  return df
#這邊是屬於我加入TAG 資料欄位
#這邊些需要人工備註之後會做出相關的塞選
def flage_add (df):
# page_1.to_excel()
  df  = page_1 
  pain_flag = []
  surrender_flag = []
  cause_flag=[]
  attitude_flag =[]
  # 爬下來所有的主文
  for i in range (len(page_1.search_rows)):
    text_main=BeautifulSoup(str(page_1.search_rows[i]))
    value_law = text_main.find_all('div')
    # flag 標記可以一直加入如果討論有關鍵字可以搜尋的時候
    for x in range (len(value_law)):
      main = value_law[x].text
      if main.find('犯後態度良好') or main.find('態度良好') >0:
        attitude= 1
      elif main.find('坦承犯行')or main.find('坦認犯行') >0:
        attitude= 1
      else: 
        attitude = 0
      if main.find('過失傷害')>0:
        print('過失傷害')
        pain = 1
      elif main.find('過失重傷')>0:

        pain = 2
      else:
        pain = 0
      if main.find('自首')>0:
        surrender =1
      else: 
        surrender =0
      if main.find('車禍')>0:
        cause_type = 0
      else:  
        cause_type = 1 
    pain_flag.append(pain)
    surrender_flag.append(surrender)
    cause_flag.append(cause_type)
    attitude_flag.append(attitude)
  page_1['pain_flag'] = pain_flag
  page_1['surrender_flag'] = surrender_flag
  page_1['cause_flag'] = cause_flag
  page_1['attitude_flag'] = attitude_flag
  tag_excel = pd.DataFrame()
  tag_excel['Date'] = page_1['Date'] 
  tag_excel['tile'] =page_1['tile']
  tag_excel["pain_flag"] = page_1.pain_flag
  tag_excel['surrender_flag']=page_1['surrender_flag']
  tag_excel['cause_flag']=page_1['cause_flag']
  tag_excel['history_flag']=page_1['history_flag']
  tag_excel['attitude_flag']=page_1['attitude_flag']
  tag_excel['main']='主文撰寫中先不放資料會太大'
  tag_excel['attachment']='附件撰寫中'
  tag_excel['text']='內容撰寫中'
  # 這邊是需要人工標記的部分
  tag_excel['mediation']='備註'
  tag_excel['ecominic']='備註'
  tag_excel['result']='需備註'
  tag_excel['defendant_opinion']='備註'
  tag_excel['court_opinion'] ="備註"
  tag_excel['url']=head+page_1.URL
  tag_excel['title']=page_1.title

  return tag_excel
 
