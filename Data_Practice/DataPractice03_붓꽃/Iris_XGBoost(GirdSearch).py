import pandas as pd
import seaborn as sns ### 데이터셋
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.model_selection import train_test_split ### 데이터 분리
from sklearn.linear_model import LogisticRegression ### 로지스틱 회귀 알고리즘
from sklearn.neighbors import KNeighborsClassifier ### 최근접이웃알고리즘

# 목표 : 붓꽃 종을 분류하라

## 데이터 불러오기
iris = sns.load_dataset('iris')
print(iris['species'].value_counts) ### 종마다 몇개가 있는 지 확인 >> stratify 사용 여부 판단

## 데이터 분석
print(iris.info()) ### 데이터 세부사항 확인 >> 타입, 열, 수 , 결측치 판단
                   ### 결측치가 없는 데이터는 처리 Pass

## 데이터 시각화
g = sns.pairplot(iris, hue='species', markers='+') ### 종을 기준으로 데이터 확인
plt.show() ### 데이터 눈으로 확인

## 데이터 처리
### 결측치 없고
### 붗꽃 분류 방해 요소 없고
### 결론 >> 따로 처리할 데이터 x

## 데이터 분류 및 모델 학습
X = iris.drop('species', axis=1) ### 타겟변수 제외
y = iris['species'] ### 타겟변수 저장


## Version1 -생략- (KNN-이웃수 고정)
## Version2 -생략- (KNN-데이터 분류 x)
## Version3 (KNN-데이터 학습용, 테스트용 분류)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5) ### 학습용 테스트용 분류

k_range = list(range(1, 26)) ### 이웃수 리스트로 저장 >> 최상의 하이퍼파라미터를 찾기위함.
scores = [] 
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k) ### KNN 객체 생성(이웃수 지정)
    knn.fit(X_train, y_train) ### KNN 모델 학습 시키기 (훈련용 데이터)
    y_pred = knn.predict(X_test) ### 학습시킨 모델을 통한 예측값 
    scores.append(metrics.accuracy_score(y_test, y_pred)) ### 예측값과 실제값 비교 >> 과소 or 과대 판단하기

plt.plot(k_range, scores) ### 그래프 : x = 이웃수, y = 정확도
plt.xlabel("k")
plt.ylabel("score")
plt.title("Version3")
plt.show()

## Version4 -생략- (Logistic Regression)
