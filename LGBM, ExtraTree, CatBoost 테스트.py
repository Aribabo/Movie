pip install lightgbm
sklearn.metrics.mean_absolute_error



movie_dataset = pd.read_csv('변수종합최종_11111.csv', encoding = 'cp949')

movie_dataset.info()
movie_dataset.columns
movie_dataset.isnull().sum()

y_column = movie_dataset['관객수']
x_columns = movie_dataset[['개봉시기', '개봉전상영횟수', '국내영화여부', '대형배급사여부', '등급', '관람객평점',
       '관람객평점자수', '기자&평론가평점', '기자&평론가수', '네티즌평점', '네티즌평점자수', '천만감독유무',
       '천만배우유무', '천만배우수', '주연배우팔로워수평균', '원작 유무(1, 0)', '시리즈 유무(1, 0)', 
       '4D 유무(1, 0)', '특별상영관여부', '수상여부', '수상횟수', '개봉일수',
       '인스타태그수', '블로그태그수', '상영점유율_평균', '스크린수_평균', '상영횟수_평균', '좌석수_평균',
       '좌석점유율_평균', '좌석판매율_평균', '티켓값평균', '스크린수_총합', '상영횟수_총합', '코로나확진자수합',
       '코로나평균확진자수', '거리두기수준', '좌석띄어앉기', '음식물제한', '음료제한', '시간제한', '미접종자제한',
       '일평균기사건수', '일평균보도건수', '일평균코로나평균기사수', '12세관람가', '15세관람가', '청소년관람불가',
       '인기장르', '비인기장르']]


x_train, x_test, y_train, y_test = train_test_split(x_columns, y_column, test_size =0.25 , random_state=0)


from sklearn.metrics import mean_absolute_error as MAE

# lightgbm -> 얜 아니야 
import lightgbm as lgb
LR = lgb.LGBMRegressor(n_estimators = 5,learning_rate = 0.3,min_child_samples = 5,num_leaves=19, random_state=42).fit(x_train, y_train)
pred = LR.predict(X_test)
MAE(y_test,pred)
# 1301939.150800355
# LR = lgb.LGBMRegressor(n_estimators = 5, learning_rate = 0.3,random_state=42).fit(X_train, y_train)
# 1225304.015934097
# LR = lgb.LGBMRegressor(n_estimators = 5, learning_rate = 0.3,min_child_samples = 5,random_state=42).fit(X_train, y_train)
# 1177238.5764555288
# LR = lgb.LGBMRegressor(n_estimators = 5, learning_rate = 0.3,min_child_samples = 5,num_leaves=19,random_state=42).fit(X_train, y_train)
# 1139946.4963413565

# ExtraTree
from sklearn.ensemble import ExtraTreesRegressor
ETR = ExtraTreesRegressor(n_estimators=5, min_samples_split=14, min_samples_leaf= 14,random_state=10).fit(x_train, y_train)
pred = ETR.predict(x_test)
MAE(y_test, pred)
# 1264377.069475757
#ETR = ExtraTreesRegressor(n_estimators=5, min_samples_split=15, min_samples_leaf= 15,random_state=10).fit(X_train, y_train)
#1155773.995306411
#ETR = ExtraTreesRegressor(n_estimators=5, min_samples_split=14, min_samples_leaf= 14,random_state=10).fit(X_train, y_train)
#1150334.0721537014

pip install catboost
# catboost
from catboost import CatBoostRegressor
cat = CatBoostRegressor(random_state=10).fit(x_train, y_train)
pred = cat.predict(x_test)
MAE(y_test,pred)
# 1105154.545575626

