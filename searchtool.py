class TestUntitled:
  def __init__(self,vars):
    self.year = vars['year']
    self.rule = vars['rule']
    self.no  = vars['no']
    self.no_end = vars['no_end']
  def test_untitled(self):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_argument('--headless')
    self.chrome_options.add_argument('--no-sandbox')
    self.chrome_options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome('chromedriver',chrome_options=self.chrome_options)


    self.driver.get("https://law.judicial.gov.tw/FJUD/Default_AD.aspx")
  # jud_sys
    self.driver.find_element(By.CSS_SELECTOR, "#vtype_M > input").click()

    self.driver.find_element(By.ID, "jud_year").send_keys(self.year)

    self.driver.find_element(By.ID, "jud_case").send_keys(self.rule)

    self.driver.find_element(By.ID, "jud_no").send_keys(self.no)

    self.driver.find_element(By.ID, "jud_no_end").send_keys(self.no_end)
    self.dropdown = self.driver.find_element(By.ID, "jud_court")
    self.dropdown.find_element(By.XPATH, "//option[. = '臺灣臺北地方法院']").click()
    self.driver.find_element(By.ID, "btnQry").click()
    self.soup = BeautifulSoup(driver.page_source, 'html.parser')
    self.detail = soup.find(attrs={"id": "form1"})
    self.iframe =detail.find_all('iframe')
    for i in self.iframe:
      print(i['src'])
    self.head = 'https://law.judicial.gov.tw/FJUD/'
    self.url = head+i['src']
    self.req = requests.get(url)
    self.soup_ss = BeautifulSoup(self.req.text, 'html.parser')
    return   self.soup_ss  
  def append_option(self):
    self.option = self.soup_ss.find_all('option')
    
    self.url = len(self.option)
    self.url = self.url/2
    url_ls =[]
    if ()>=25:
      for i range (25):
        url_ls.append(self.url[i])
        print('exceed len')
  
    else: 
      
      for i in range (self.url):
        url_ls.append(self.url[i])
    return self.url_ls  


 
