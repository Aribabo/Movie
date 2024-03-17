pip install selenium

from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import random

def scroll():
    try:        
        # 페이지 내 스크롤 높이 받아오기
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            # 임의의 페이지 로딩 시간 설정
            # PC환경에 따라 로딩시간 최적화를 통해 scraping 시간 단축 가능
            pause_time = random.uniform(1, 2)
            # 페이지 최하단까지 스크롤
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            # 페이지 로딩 대기
            time.sleep(pause_time)
            # 무한 스크롤 동작을 위해 살짝 위로 스크롤(i.e., 페이지를 위로 올렸다가 내리는 제스쳐)
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight-50)")
            time.sleep(pause_time)
            # 페이지 내 스크롤 높이 새롭게 받아오기
            new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
            # 스크롤을 완료한 경우(더이상 페이지 높이 변화가 없는 경우)
            if new_page_height == last_page_height:
                print("스크롤 완료")
                break
                
            # 스크롤 완료하지 않은 경우, 최하단까지 스크롤
            else:
                last_page_height = new_page_height
            
    except Exception as e:
        print("에러 발생: ", e)



driver = webdriver.Chrome(ChromeDriverManager().install())

movie = pd.read_csv('연도별50위영화.csv')

list = []
movie_list = []
name_list = []
url_list = []
view_list = []
    
for i in movie.loc[:,'영화명'] :
    keyword = i
    url = 'https://www.youtube.com/results?search_query={}'.format(keyword)
    driver.get(url)
    time.sleep(2)
    scroll()
        
    soup = bs(driver.page_source, 'html.parser')

    name = soup.select('a#video-title')
    video_url = soup.select('a#video-title')
    view = soup.select('a#video-title')


    for j in range(len(name)):
        movie_list.append(i)
        name_list.append(name[j].text.strip())
        view_list.append(view[j].get('aria-label').split()[-1])
       # url_list.append('https://www.youtube.com'+video_url.get('href'))
    for j in video_url:
        url_list.append('{}{}'.format('https://www.youtube.com',j.get('href')))
        
    
youtubeDic = {
      '영화제목' : movie_list,
      '영상제목': name_list,
      '주소': url_list,
      '조회수': view_list}
youtubeDf = pd.DataFrame(youtubeDic)
  
    
youtubeDf.to_csv( '50위영화별유튜브_1025.csv', encoding='', index=False)
    



movie1 = pd.read_csv('50위영화별유튜브_1025.csv')
