from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import datetime

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://watcha.com/staffmades/410' 
driver.get(url)

# 자료들 담을 리스트 준비
info_list = []
rate1_list = []
rate2_list = []
rate3_list = []
rate4_list = []
rate5_list = []
rate6_list = []
rate7_list = []
rate8_list = []
rate9_list = []
rate10_list = []

#1위
rate_num1 = "#rank-1"

rate1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[1]/section/ul/li[1]/div[1]/ul/li[1]/div/div[1]/div[1]/div[1]/span")
rate1 = driver.find_element(By.XPATH, "//html/body/div[1]/div[1]/main/div[1]/section/ul/li[1]/div[1]/ul/li[1]/div/div[2]/div/div")
title_rate1 = rate1.get_attribute("style")
rate1_src = rate1.get_attribute("data-src")

rate1_list.append(rate_num1)
rate1_list.append(title_rate1)
rate1_list.append(rate1_src)

#2위
rate_num2 = "#rank-2"

rate2 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[2]/a/div[1]/img")
title_rate2 = rate2.get_attribute("alt")
rate2_src = rate2.get_attribute("data-src")

rate2_list.append(rate_num2)
rate2_list.append(title_rate2)
rate2_list.append(rate2_src)

#3위
rate_num3 = "#rank-3"

rate3 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[3]/a/div[1]/img")
title_rate3 = rate3.get_attribute("alt")
rate3_src = rate3.get_attribute("data-src")

rate3_list.append(rate_num3)
rate3_list.append(title_rate3)
rate3_list.append(rate3_src)

#4위
rate_num4 = "#rank-4"

rate4 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[4]/a/div[1]/img")
title_rate4 = rate4.get_attribute("alt")
rate4_src = rate4.get_attribute("data-src")

rate4_list.append(rate_num4)
rate4_list.append(title_rate4)
rate4_list.append(rate4_src)

#5위
rate_num5 = "#rank-5"

rate5 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[5]/a/div[1]/img")
title_rate5 = rate5.get_attribute("alt")
rate5_src = rate5.get_attribute("data-src")

rate5_list.append(rate_num5)
rate5_list.append(title_rate5)
rate5_list.append(rate5_src)

#6위
rate_num6 = "#rank-6"

rate6 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[6]/a/div[1]/img")
title_rate6 = rate6.get_attribute("alt")
rate6_src = rate6.get_attribute("data-src")

rate6_list.append(rate_num6)
rate6_list.append(title_rate6)
rate6_list.append(rate6_src)

#7위
rate_num7 = "#rank-7"

rate7 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[7]/a/div[1]/img")
title_rate7 = rate7.get_attribute("alt")
rate7_src = rate7.get_attribute("data-src")

rate7_list.append(rate_num7)
rate7_list.append(title_rate7)
rate7_list.append(rate7_src)

#8위
rate_num8 = "#rank-8"

rate8 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[8]/a/div[1]/img")
title_rate8 = rate8.get_attribute("alt")
rate8_src = rate8.get_attribute("data-src")

rate8_list.append(rate_num8)
rate8_list.append(title_rate8)
rate8_list.append(rate8_src)

#9위
rate_num9 = "#rank-9"

rate9 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[9]/a/div[1]/img")
title_rate9 = rate9.get_attribute("alt")
rate9_src = rate9.get_attribute("data-src")

rate9_list.append(rate_num9)
rate9_list.append(title_rate9)
rate9_list.append(rate9_src)

#10위
rate_num10 = "#rank-10"

rate10 = driver.find_element(By.XPATH, "//*[@id='g-contents']/div[2]/div[10]/a/div[1]/img")
title_rate10 = rate10.get_attribute("alt")
rate10_src = rate10.get_attribute("data-src")

rate10_list.append(rate_num10)
rate10_list.append(title_rate10)
rate10_list.append(rate10_src)

#리스트들 취합
info_list.append(rate1_list)
info_list.append(rate2_list)
info_list.append(rate3_list)
info_list.append(rate4_list)
info_list.append(rate5_list)
info_list.append(rate6_list)
info_list.append(rate7_list)
info_list.append(rate8_list)
info_list.append(rate9_list)
info_list.append(rate10_list)

#오늘 날짜 가져오기
now = datetime.datetime.now().date()
today_split = str(now).split("-")
today = today_split[1]+today_split[2]

#데이터 csv 파일로 저장
data = pd.DataFrame(info_list)
data.columns = ["rate", "title", "img_link"]

data.to_csv(today+"_wavve.csv", encoding="cp949", index=None)
time.sleep(5)

driver.close()


