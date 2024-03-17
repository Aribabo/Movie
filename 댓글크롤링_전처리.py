# -*- coding: utf-8 -*-
news21_1 = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona21_1q.csv')
news21_2 = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona21_2q.csv')
news21_3 = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona21_3q.csv')
news21_4 = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/corona21_4q.csv')
news21_5 = pd.read_csv('C:/Users/user/Desktop/팀프로젝트/woohan21.csv')

news21_full = DataFrame()
news21_full = pd.concat([news21_full, news21_1], ignore_index=True)
news21_full = pd.concat([news21_full, news21_2], ignore_index=True)
news21_full = pd.concat([news21_full, news21_3], ignore_index=True)
news21_full = pd.concat([news21_full, news21_4], ignore_index=True)
news21_full = pd.concat([news21_full, news21_5], ignore_index=True)

news21_full = news21_full.drop_duplicates() # 19년 12월 31~ 20년 12월 31일까지 총 111만개의 기사
import re
a = ['코로나','폐렴', '확진', '사망', '감염', '전염', '우한''COVID', '마스크', '재택근무', '거리두기',
'영업제한', '자가격리','자가검진키트', 'PCR' ,'보건소' , '치료제', '백신','화이자','모더나','샐트리온',
'항체','재난','재앙','팬데믹','자영업','소상공인','오미크론','변이','비대면','역병','확산','RNA','코호트',
'일상회복','접종','유행','방호복', '생활치료센터','방역']
real_news = news21_full['title'].apply(lambda x : any(re.findall('|'.join(a),x,re.IGNORECASE)))
real_news.sum() # 268441개의 기사

real_news_21 = news21_full.loc[real_news,:]
real_news_21.to_csv('total_title_21.csv')

import pandas as pd

su22_1 = pd.read_parquet('댓글22/comment22_0_10000.parquet', engine='pyarrow') 
su22_2 = pd.read_parquet('댓글22/comment22_10000_19500.parquet', engine='pyarrow') 
su22_3 = pd.read_parquet('댓글22/comment22_19500_20000.parquet', engine='pyarrow') 
su22_4 = pd.read_parquet('댓글22/comment22_20000_63418.parquet', engine='pyarrow') 

full_success22 =  pd.concat([su22_1,su22_2], ignore_index=True)
full_success22 =  pd.concat([full_success22,su22_3], ignore_index=True)
full_success22 =  pd.concat([full_success22,su22_4], ignore_index=True)
full_success22 = full_success22.drop_duplicates()
full_success22.to_csv('full_success22.csv')



fa22_1 = pd.read_parquet('댓글22/error22_0_10000.parquet', engine='pyarrow') 
fa22_2 = pd.read_parquet('댓글22/error22_10000_19500.parquet', engine='pyarrow') 
fa22_3 = pd.read_parquet('댓글22/error22_19500_20000.parquet', engine='pyarrow') 
fa22_4 = pd.read_parquet('댓글22/error22_20000_63418.parquet', engine='pyarrow') 

full_fail22 =  pd.concat([fa22_1,fa22_2], ignore_index=True)
full_fail22 =  pd.concat([full_fail22,fa22_3], ignore_index=True)
full_fail22 =  pd.concat([full_fail22,fa22_4], ignore_index=True)
full_fail22 = full_fail22.drop_duplicates()
full_fail22.to_csv('full_fail22.csv')

import re
total22 = pd.read_csv('total_title_22.csv')
a = full_success22['url']

total22.loc[fail22,:]

su22_1.loc[su22_1['count']=='댓글',:]
su22_1 = pd.read_parquet('comment0_5512.parquet', engine='pyarrow') 
fa22_1 = pd.read_parquet('댓글21/error21_100000_150000.parquet', engine='pyarrow') 
su22_2 = pd.read_parquet('댓글21/comment22_10000_19500.parquet', engine='pyarrow') 

127000+150000

total22 = pd.read_csv('total_title_22.csv').iloc[:,2:5]
total22 = total22.drop_duplicates()
full_success22 = pd.read_csv('full_success22.csv').iloc[:,1:3]
full_success22 = full_success22.drop_duplicates()
total_comment_22 = pd.merge(total22,full_success22, how='outer',on='url')
total_comment_22 = total_comment_22.drop_duplicates()
total_comment_22.to_csv('total_comment_22.csv')
total_comment_22= pd.read_csv('total_comment_22.csv')
total_comment_22['count'] = total_comment_22['count'].fillna('에러')
erre22 = total_comment_22.loc[total_comment_22['count']=='에러',:]
erre22.to_csv('full_error22.csv')
success22 = total_comment_22.loc[total_comment_22['count']!='에러',:]
success22.to_csv('full_success22.csv')


# 파일 합치기
su21_1 = pd.read_parquet('댓글21/comment21_0_64500.parquet', engine='pyarrow') 
su21_2 = pd.read_parquet('댓글21/comment21_64500_100000.parquet', engine='pyarrow') 
su21_3 = pd.read_parquet('댓글21/comment21_100000_127001.parquet', engine='pyarrow') 
su21_4 = pd.read_parquet('댓글21/comment21_127000_150000.parquet', engine='pyarrow') 
su21_5 = pd.read_parquet('댓글21/comment21_150000_207500.parquet', engine='pyarrow') 
su21_6 = pd.read_parquet('댓글21/comment21_207500_268441.parquet', engine='pyarrow') 


full_success21 =  pd.concat([su21_1,su21_2], ignore_inde
full_success21 =  pd.concat([full_success21,su21_3], ignore_index=True)
full_success21 =  pd.concat([full_success21,su21_4], ignore_index=True)
full_success21 =  pd.concat([full_success21,su21_5], ignore_index=True)
full_success21 =  pd.concat([full_success21,su21_6], ignore_index=True)

full_success21 = full_success21.drop_duplicates()


total21 = pd.read_csv('total_title_21.csv')
total21 = total21.drop_duplicates()

total_comment_21 = pd.merge(total21.iloc[:,1:4],full_success21, how='outer',on='url')
total_comment_21['count'] = total_comment_21['count'].fillna('에러')
error21 = total_comment_21.loc[total_comment_21['count']=='에러',:]
error21.to_csv('full_error21.csv')
success22 = total_comment_21.loc[total_comment_21['count']!='에러',:]
success22.to_csv('full_success21.csv')





