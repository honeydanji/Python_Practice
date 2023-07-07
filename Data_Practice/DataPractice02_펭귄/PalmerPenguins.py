import seaborn as sns
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from time import time

# 그래프 한글
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


### 목표 : 펭귄의 종을 분류하는 모델을 만들어라!!!

## 데이터셋 준비
penguins = sns.load_dataset('penguins') 

#print(penguins.head()) # 데이터 확인
#print(len(penguins))
print(penguins.dtypes) # 타입 확인

## 데이터 전처리
penguins = penguins.dropna()# NaN 삭제하기(결측치 정리)
#print(penguins.head()) # NaN 삭제후 데이터 확인
#print(len(penguins)) 

colums_delete = ['island'] # 필요없는 데이터 리스트에 저장
penguins = penguins.drop(columns=colums_delete) # 열을 통채로 지워버린다.
#print(penguins.head()) # 지워진 데이터 확인
#print(penguins.info()) # 데이터 요약해서 보여준다. head랑 비슷하면서 다르다.

## 레이블 인코딩
for column in penguins.columns:
    if penguins[column].dtype == type(object):
        penguins[column] = LabelEncoder().fit_transform(penguins[column])
# 레이블 인코딩은 뭔가? >> 범주형(객체) 데이터를 숫자형 데이터로 변환
# 왜? >> 대부분 기계 학습 모델은 숫자 입력이 필요하고 범주형 데이터로 
# 작업하기가 힘들다. 그래서 숫자 데이터로 변환시켜야 한다. 
# 현재 펭귄 데이터 타입을 보면 species는 object 타입인걸 알 수 있다.



## 훈련데이터와 테스트데이터로 나누기
X = penguins.drop("species", axis=1) # 'species' 열을 삭제하고 새로운 데이터프레임을 X에 저장한다.
y = penguins["species"] 
# 타겟 변수 ? 즉 예측하고자 하는 값이 y >> 여기서 목적은 어떤 펭귄이 어떤 종인지 예측하는 것이다.
# 'species'에 해당하는 값만 y에 저장한다. 예측하거나 분류하려는 열인 대상 변수

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y) 
# 테스트용 30% 훈련용 70%
# stratify = y : 훈련 및 테스트 세트에 있는 타겟 변수의 클래스 비율이 원본 데이터와 유사하게 유지된다. 뭔말???
# y = 'species' 로 지정했다. 데이터 안에 존재하는 펭귄의 종의 수만큼 클래스가 생성된다.
# 각각의 클래스에 분포되는 테스트용 데이터와 훈련용 데이트의 수는 다를지 몰라도 비율은 동일하게 설정된다.

### POINT
# 그럼 왜? 펭귄 종마다 클래스를 나누는 것일까? >> 범주형모델이기 때문이다.
# 즉 데이터의 범위를 정해 놓으면 새로운 펭귄데이터(인스턴스)가 입력이 될 때 쉽게 펭귄의 종류를 예측할 수 있기 때문이다.
# 결론 : 원본 데이터에서 타겟변수를 정하고, 남은 데이터를 이용해 타겟 변수의 범주를 정한다. <<< 이게 핵심이다.
#       여기서 타겟변수는 예측 대상이 되는 것! ex) 펭귄의 종을 예측하세요., 꽃의 종류를 예측하세요. 등등 

## 기준 설정? (무슨 기준)
## XGBoost (1. XGBoost 분류자 인스턴스 생성, 2. 하이퍼파라미터 설정)
# 'multi:softmax' 목표 함수를 사용한 XGBoost 분류기 학습
# xgb_classifier_softmax = xgb.XGBClassifier(
#    objective="binary:logistic", # 이진분류
#    objective="multi:softmax", # 펭귄의 종이 2개 이상이면 다중분류로 생각해야한다.
#    max_depth=3, # 트리의 최대 깊이 3
#    learning_rate=0.1, # 학습률 지정 (예시로는 : 경사하강법을 생각해라. 학습률이 높으면 빠르지만 오버슈팅이 된다.)
#    n_estimators=100 # 트리의수 ?? 추정기 수?? 
                     # 스무고개 게임을 생각해라. 질문이 많을수록 정답에 가까워 질 수 있지만, 필요하지 않은 질문을 하면 전혀다른 답이 나올 수 있다.
                     # 트리 즉 추정기는 적당해야한다.
#) 

#xgb_classifier_softmax.fit(X_train, y_train) # 모델 학습
#y_pred_softmax = xgb_classifier_softmax.predict(X_test) # 테스트 데이터 예측
#accuracy_softmax = accuracy_score(y_test, y_pred_softmax) # 정확도 계산

# 'multi:softprob' 목표 함수를 사용한 XGBoost 분류기 학습
# xgb_classifier_softprob = xgb.XGBClassifier(
#     objective="multi:softprob", # 각 클래스에 대한 확률을 출력하는 softprob 목표 함수
#     max_depth=3, # 결정 트리의 최대 깊이
#     learning_rate=0.1, # 그래디언트 부스팅의 학습률
#     n_estimators=100 # 앙상블에 사용될 결정 트리의 수
# )

# xgb_classifier_softprob.fit(X_train, y_train) # 모델 학습
# y_pred_softprob = xgb_classifier_softprob.predict_proba(X_test) # 테스트 데이터에 대한 클래스 확률 예측
# accuracy_softprob = accuracy_score(y_test, y_pred_softprob.argmax(axis=1)) # 정확도 계산

### POINT
# "데이터를 학습시킨다" << 의미가 정확히 뭘까?
# 1. 수집된? 정리된? 정리안된? 아무튼 특정 데이터가 주어진다.
# 2. 데이터가 어떤 식으로 이루어져 있는 지 파악하자.(단, 목적이 정해져 있어야 한다.)
#    - 표 자체를 분석하기
#    - 그래프로 그려서 분석하기
#    - 해당 데이터의 도메인 지식을 찾아보기
#    - 데이터가 제공된 곳(사람, 웹 등) 살펴보기
# 3. 각각의 데이터들이 서로 어떻게 상호작용하는 지에 따라서 학습 모델을 구성한다.
# 4. 모델이 정해지면 데이터를 학습 시킨다.
#    : 크게 분류 or 예측으로 나뉜다.
# 결론: 주어진 데이터를 이해하는 것이 가장 중요하고, 
#       그 데이터의 목적을 분명하게 알아야하며, 
#       어떤 알고리즘을 적용해야 실제값과 예측값의 오차를 줄일 수 있을까? 를 고민하는 것이 핵심이다.


## 하이퍼 파라미터 그리드 설정
param_grid = {
    'learning_rate': [0.1, 0.2, 0.3, 0.4, 0.5], # 학습률 리스트 설정
    'max_depth': [3, 4, 5, 6, 7, 8],  # 트리의 최대 깊이 리스트 설정
    'n_estimators': [50, 100, 200, 300]  # 부스팅 스테이지(결정트리 개수) 리스트 설정
}

    # 왜? girdsearch의 근본적인 이유를 생각하면 된다.
    # 학습률, 트리깊이, 트리 개수를 다양하게 지정해야만
    # 이 중에서 최상의 조합을 찾을 수 있다.
    # 학습률이 0.1 만 있으면 gridserach를 사용할 필요가 없다.

## 모델 객체 생성
xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')  
# XGBoost 분류 모델 생성, 라벨 인코딩 사용 안 함, 다중 클래스 로그 손실 사용
# 여기서 한가지 의문이 생긴다. 라벨 인코딩은 이미 사용해서 범주형 데이터를 처리했는데,
# 모델을 생성하는 코드에서 "use_label_encoder=False" 이 부분은 무슨 의미일까?
# XGBoost는 분류 해야할 데이터가 들어오면 자동으로 내부 라벨 인코딩을 하도록 설정되어 있다.
# 하지만 이미 라벨 인코딩으로 데이터를 처리 했기 때문에 혼동을 주지 않기 위해 
# 해당 기능을 비활성화 시킨 것이다. 
# 즉 "내가 이미 범주형 변수의 인코딩을 처리했으므로 XGBoost가 그것에 대해 걱정할 필요가 없다." 라는 의미다.



## 그리드 서치 객체 생성
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=3, scoring='accuracy')  
# 그리드 서치 객체 생성. estimator는 사용할 모델, param_grid는 테스트할 하이퍼파라미터 그리드, cv는 cross-validation 분할 개수, scoring은 성능 평가 지표

## 그리드 서치 학습
grid_search.fit(X_train, y_train)  # 학습 데이터를 이용하여 그리드 서치 학습
# 여기가 펭귄 종을 분류하는데 있어서 가장 포인트가 되는 지점이라고 생각한다.
# 주어진 데이터로 범주를 확실하게 나누는 걸 학습시키는 부분이다.
# 여기서 학습이 이상하게 되어버리면 결과물이 말도 안되게 나올 수 있다. 
# 더 쉽게 정리하자면
# 각각의 펭귄들이 가진 신체 데이터의 평균값을 범주(클래스)로 정해준다. >>> 이 말이 "학습을 시킨다."라는 말이 될 수 있다. 

## 최적 하이퍼 파라미터 확인
print('Best learning_rate:', grid_search.best_estimator_.get_params()['learning_rate'])  # 최적 학습률 출력
print('Best max_depth:', grid_search.best_estimator_.get_params()['max_depth'])  # 최적 최대 깊이 출력
print('Best n_estimators:', grid_search.best_estimator_.get_params()['n_estimators'])  # 최적 부스팅 스테이지 출력

## 최적 모델로 예측

best_xgb_model = grid_search.best_estimator_  
### 최적 모델 추출
y_pred = best_xgb_model.predict(X_test)  
### 테스트 데이터에 대한 예측 수행

# 정확도 계산
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")




#### 펭귄을 분류하는데 있어서 각 특징들의 중요도를 나타낸다.

## 학습 데이터로 모델 학습
best_xgb_model.fit(X_train, y_train)

## 펭귄을 분류하는데 특징 중요도를 가져옵니다
importance = best_xgb_model.feature_importances_

## 펭귄 특징을 출력
for i, v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i, v))

## 특징 우선순위 그래프
plt.figure(figsize=(10, 5))
## 그래프 크기를 설정
plt.barh([x for x in range(len(importance))], importance, tick_label=X_train.columns)

## 그래프 구성 
plt.title('펭귄 신체데이터')
plt.xlabel('중요도')

plt.show()




















### 개념
# 하이퍼파라미터 : 변경이 가능한 변수로 학습률, 에코프(훈련반복횟수), 가중치 초기화 등이 있다.

