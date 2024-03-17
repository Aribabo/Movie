# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
from pandas import DataFrame
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import psutil

data = pd.read_csv('total_title_20.csv')

# CPU과부하 해결방법
# 현재 cpu사용량을 체크후 해당 퍼센트 이전에 코드를 멈추고 시간을 둬
# CPU를 휴식시킨 후에 크롤링 다시 시작
# 이 코드를 오늘 작성해서 자기전에 돌린후 효과가 있는지 확인
def comment_crawl(data,start:int,end:int):
    options = webdriver.ChromeOptions()
    # 백그라운드 실행 옵션 추가
    options.add_argument("headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options= options)
    driver.implicitly_wait(20) 
    error_url=[];n_url=[];ct_1=[]
    comment_file = 'comment20_'+str(start)+'_'+str(end)+'.parquet'
    error_file = 'error20_'+str(start)+'_'+str(end)+'.parquet'
    for i in range(start,end):
        url1 = data.loc[i]['url']
        driver.get(url1)
        time.sleep(0.25)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        try :
            ct_1.append(soup.select('span.u_cbox_info_txt')[0].text)
            n_url.append(url1)
        except :
            error_url.append(url1)
        if i%500== 0 :
            DataFrame({'url':n_url,'count':ct_1},index=range(0,len(n_url))).to_parquet(comment_file, engine='pyarrow')
            DataFrame({'error_url':error_url},index=range(0,len(error_url))).to_parquet(error_file, engine='pyarrow')
        if psutil.cpu_percent() >= 65 :
            driver.quit()
            time.sleep(10)
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options= options)
            driver.implicitly_wait(20)
            print('rebooting')
    DataFrame({'url':n_url,'count':ct_1},index=range(0,len(n_url))).to_parquet(comment_file, engine='pyarrow')
    DataFrame({'error_url':error_url},index=range(0,len(error_url))).to_parquet(error_file, engine='pyarrow')
    driver.quit() # 반드시 꺼줘야 함
    

comment_crawl(data,58000,659899)
    

