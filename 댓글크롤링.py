# -*- coding: utf-8 -*-
# 드디어 다가온............................뉴스댓글크롤링
# 목적 : 뉴스기사 url에 접속하여 현재댓글수 크롤링
# 형식 : 데이터 프레임
#        날짜 url 댓글수 

#어라? 댓글이 없는 기사는 형식이 좀 다를듯
# 찾아봐야만.

run my_profile
news20_wh = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/woohan20.csv')
news2001_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2001.csv')
news2002_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2002.csv')
news2003_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2003.csv')
news2004_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2004.csv')
news2005_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2005.csv')
news2006_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2006.csv')
news2007_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2007.csv')
news2007_1_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2007_2.csv')
news2007_2_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2007_싱.csv')
news2008_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2008.csv')
news2009_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2009.csv')
news2010_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2010.csv')
news2011_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2011.csv')
news2012_co = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona2012.csv')

news20_full = DataFrame()
news20_full = pd.concat([news20_full, news20_wh], ignore_index=True)
news20_full = pd.concat([news20_full, news2001_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2002_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2003_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2004_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2005_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2006_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2007_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2007_1_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2007_2_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2008_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2009_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2010_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2011_co], ignore_index=True)
news20_full = pd.concat([news20_full, news2012_co], ignore_index=True)

news20_full = news20_full.drop_duplicates() # 19년 12월 31~ 20년 12월 31일까지 총 111만개의 기사
'코로나' in news20_full['title'][0]

# 코로나 /폐렴/ 확진/ 사망/ 감염/ 전염/ 우한 / COVID/ 마스크/ 재택근무/ 거리두기/ 
# 영업제한/ 자가격리/자가검진키트/ PCR / 보건소 / 치료제/ 백신/화이자/ 모더나/ 샐트리온
# 항체/재난/재앙/팬데믹/자영업/소상공인/오미크론/변이/비대면/역병/확산/RNA/코호트/유행/방호복
# 생활치료센터
import re
a = ['코로나','폐렴', '확진', '사망', '감염', '전염', '우한''COVID', '마스크', '재택근무', '거리두기',
'영업제한', '자가격리','자가검진키트', 'PCR' ,'보건소' , '치료제', '백신','화이자','모더나','샐트리온',
'항체','재난','재앙','팬데믹','자영업','소상공인','오미크론','변이','비대면','역병','확산','RNA','코호트',
'일상회복','접종','유행','방호복', '생활치료센터','방역']
real_news = news20_full['title'].apply(lambda x : any(re.findall('|'.join(a),x,re.IGNORECASE)))
real_news.sum() # 659899개의 기사
real_news_20 = news20_full.loc[real_news,:]
real_news_20['title'] # 총 659899개의 기사
real_news_20.to_csv('total_title_20.csv')


# news20_full2 = pd.concat([news20_full[a1],news20_full[a2]], ignore_index=True)
news20_full2 = pd.concat([news20_full2,news20_full[a1]], ignore_index=True)
news20_full2 = pd.concat([news20_full2,news20_full[a2]], ignore_index=True)

from bs4 import BeautifulSoup
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

# 2. Chrome 실행
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)   # 웹페이지 파싱까지 최대 30초 기다림

# 3. Chrome을 통해 url 정보 가져오기
url = 'https://n.news.naver.com/mnews/article/056/0010781095?sid=103'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
soup.select('span.u_cbox_info_txt')[0].text
url = 'https://n.news.naver.com/mnews/article/056/0010781095?sid=104'
driver.get(url)
import time
time.sleep(0.0001)
soup = BeautifulSoup(driver.page_source, 'html.parser')
soup.select('span.u_cbox_info_txt')[0].text


# 함수만들기~~
# Chrome 실행
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30) 
error_url=[];n_url=[];ct_1=[]
for i in range(3001,7001):
    url1 = real_news_20.loc[i]['url']
    driver.get(url1)
    time.sleep(0.7)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try :
        ct_1.append(soup.select('span.u_cbox_info_txt')[0].text)
        n_url.append(url1)
    except :
        error_url.append(url1)
    if i%100 == 0 :
        DataFrame({'url':n_url,'count':ct_1},index=range(0,len(n_url))).to_csv('comment1.csv')
        DataFrame({'error_url':error_url},index=range(0,len(error_url))).to_csv('error1.csv')



# 백그라운드 실행
# 크롤링 옵션 생성
options = webdriver.ChromeOptions()
# 백그라운드 실행 옵션 추가
options.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options= options)
driver.implicitly_wait(30) 
error_url=[];n_url=[];ct_1=[]
for i in range(3001,7001):
    url1 = real_news_20.loc[i]['url']
    driver.get(url1)
    time.sleep(0.7)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try :
        ct_1.append(soup.select('span.u_cbox_info_txt')[0].text)
        n_url.append(url1)
    except :
        error_url.append(url1)
    if i%100 == 0 :
        DataFrame({'url':n_url,'count':ct_1},index=range(0,len(n_url))).to_csv('comment1.csv')
        DataFrame({'error_url':error_url},index=range(0,len(error_url))).to_csv('error1.csv')        
driver.quit() # 반드시 꺼줘야 함


# 그 다음이요 








