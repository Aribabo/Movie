# -*- coding: utf-8 -*-
df1 = pd.read_csv('1113_totalrealdata_거리좌석합침.csv')
df1.columns
df2 = df1.iloc[:,5:]
df2.columns
# df2 = df2.dropna(axis = 0)
df_x = df2.drop('관객수', axis = 1)
df_x.columns
# df_x.isna().sum()
# df_y = df2['관객수']
# df_x.isna().sum()


df_y = pd.cut(df2['관객수'],[0,1500000,3000000,7000000,17000000],labels=[0,1,2,3])
df_y = df_y.astype('int')


# =============================================================================
# 오버샘플링 - ADASYN 사용
# =============================================================================
from imblearn.over_sampling import ADASYN
from imblearn.over_sampling import RandomOverSampler
m_ADASYN = ADASYN(random_state=0)
df_x1, df_y1 = m_ADASYN.fit_resample(df_x, df_y)
m_random = RandomOverSampler(random_state=0)
df_x2, df_y2 = m_random.fit_resample(df_x, df_y)


x_train, x_test, y_train, y_test = train_test_split(df_x2, df_y2, test_size = 0.4 ,random_state=0)


# =============================================================================
# CatBoost와 Optuna를 사용하여 학습
# =============================================================================
def objective(trial):
    model = catboost.CatBoostClassifier(
        iterations=trial.suggest_int("iterations", 100, 1000),
        learning_rate=trial.suggest_float("learning_rate", 1e-3, 1e-1, log=True),
        depth=trial.suggest_int("depth", 4, 10),
        l2_leaf_reg=trial.suggest_float("l2_leaf_reg", 1e-8, 100.0, log=True),
        bootstrap_type=trial.suggest_categorical("bootstrap_type", ["Bayesian"]),
        random_strength=trial.suggest_float("random_strength", 1e-8, 10.0, log=True),
        bagging_temperature=trial.suggest_float("bagging_temperature", 0.0, 10.0),
        od_type=trial.suggest_categorical("od_type", ["IncToDec", "Iter"]),
        od_wait=trial.suggest_int("od_wait", 10, 50),
        # n_estimators = trial.suggest_int("n_estimators", 1000, 10000),
        # max_depth = trial.suggest_int("max_depth", 4, 16),
        verbose=False
    )
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)

sampler = TPESampler(seed=1)
study = optuna.create_study(study_name="catboost", direction="maximize", sampler=sampler)
study.optimize(objective, n_trials=20)

trial =study.best_trial
trial.value
trial.params.items()

model = catboost.CatBoostClassifier(**trial.params, verbose=False)
model.fit(x_train, y_train)
model.score(x_train, y_train)
model.score(x_test,y_test)


x_train.to_csv('real_x_train.csv')
x_test.to_csv('x_test.csv')
y_train.to_csv('y_train.csv')
y_test.to_csv('y_test.csv')

x_train, x_test, y_train, y_test 
