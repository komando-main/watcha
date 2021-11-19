# Selenium 임포트
from selenium import webdriver
# 키보드 down키(↓)를 누르게 하기 위해 Keys 임포트
from selenium.webdriver.common.keys import Keys
# Beautiful Soup 임포트
from bs4 import BeautifulSoup

# csv 파일 생성을 위해 임포트
import csv
csv_fileName = 'watcha.csv'

csv_open = open(csv_fileName, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)

csv_writer.writerow(('image'))

PATH = "/MYStudy/Python_Study/csv"
driver = webdriver.Chrome(PATH)

driver.get("https://watcha.com/staffmades/410")

body = driver.find_element_by_css_selector("body")

for i in range(100):
    keys = body.send_keys(Keys.PAGE_DOWN)
    
htmlsrc = driver.page_source
bs = BeautifulSoup(htmlsrc, 'html.parser')

wrapper = bs.find_all('span', {"class" : "css-1te5psz-StyledBackground e1q5rx9q1"})

images_wrap = []
    
for images in wrapper:
    image = images.find('span', class_="css-1te5psz-StyledBackground e1q5rx9q1")['style']
    url_text = image.split('background-image: url("')[1][23:-3]
    images_wrap.append(url_text)

csv_open.close()

driver.quit()