from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime



options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://watcha.com/staffmades/410'
driver.get(url)

html = driver.page_source.encode(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')


#spans = soup.select('span[class $="e1q5rx9q1"]')
#spansTig = str(soup.select('span[class $="e1q5rx9q1"]')[0]['style'])[23:-3]
#print(spansTig)
divs = soup.select('div[class $="eb5y16b1"]')

#print(spans)
ranks=[]
titles=[]
imgUrls=[]
datas=[]

#셀레늄이 포문보다 느려서 15개 이상 찾으면 에러나면서 못찿는다
i=0
for title in divs:
    i+=1
    ranks.append('#rank-'+str(i)) 
    titles.append(str(title.text))
    imgUrls.append(str(soup.select('span[class $="e1q5rx9q1"]')[i]['style'])[23:-3])
    if i == 15:
        break

#print(ranks)
#print(titles)
#print(imgUrls)
#print(type(len(divs)))

b=0
while b < len(ranks):
    datas.append([ranks[b], titles[b], imgUrls[b]])
    b+=1
    if b == 10:
        break
    
#print(datas)

#오늘 날짜 가져오기
now = datetime.datetime.now().date()
today_split = str(now).split("-")
today = today_split[1]+today_split[2]

data = pd.DataFrame(datas)
data.columns = ["rate", "title", "img_link"]
data.to_csv(today+"_watcha.csv", encoding="cp949", index=None)

driver.close()
print(data)