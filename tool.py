def crawing(page):
  head = 'https://law.judicial.gov.tw/'
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
