import requests
from bs4 import BeautifulSoup


watcha_resul = requests.get("https://pedia.watcha.com/ko-KR")

watcha_soup = BeautifulSoup(watcha_resul.text, 'html.parser')

ebeya3l5 = watcha_soup.find('div', {"class":'css-6kwoq4-StyledHorizontalScrollInnerContainer ebeya3l5'})
ul = ebeya3l5.find('ul')

divs = ul.find_all('div',{'class':'css-5yuqaa'})
for div in divs:
  print(div.text)

imgs = ul.find_all('img')
for img in imgs:
  print(img.get('src'))