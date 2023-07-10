import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier # 최근접 이웃 알고리즘

# 목표 : 붓꽃 종을 분류하라!

## 데이터 불러오기
iris = sns.load_dataset('iris') 

## 데이터 분석
# print(iris.head()) ### 데이터 확인하기
# print(len(iris)) ### 데이터 수 확인하기
# print(iris.keys()) ### 데이터 key-value 확인하기 >> 데이터가 딕셔너리 형태
# print(iris.dtypes) ### 데이터 타입 확인 >> 라벨 인코딩 사용 여부 판단
# print(iris.info()) ### 데이터 세부사항 확인 >> 타입, 열, 수, 결측치 전부 확인이 가능하다.
                   ### 결측치가 없기 때문에 따로 처리 하지 않아도 된다.
                   
# print(iris.isnull()) ### 결측치 확인

## 데이터 처리
### 결측치 없고,
### 붓꽃을 분류하는데 방해 특성 없음. 
### 처리할 데이터는 존재하지 않음.

## 데이터 시각화
g = sns.pairplot(iris, hue='species', markers='+')
plt.show() ### 붓꽃 꽃잎 -길이 , 폭 꽃받침 - 길이, 폭의 연관성을 나타내는 그래프

## 데이터 분류 및 모델 학습
X = iris.drop('species', axis=1) ### 타겟변수를 구성하는 특성 X 초기화
y = iris['species'] ### 타겟변수 지정(대상변수)

## version 2(Train과 Test로 나누지 않고, KNN 분류기) + 모델 성능 검사 및 향상
k_range = list(range(1, 26)) ### 이웃수 범위 지정 왜?? 
scores = [] ### k(이웃수)의 따른 예측값 정확도 저장 변수
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k) ### 최근접이웃 객체 생성(이웃수 지정)
    knn.fit(X,y) ### 데이터 학습 시키기
    y_pred = knn.predict(X) ### 예측값 변수 초기화
    scores.append(metrics.accuracy_score(y, y_pred)) ### 예측값 리스트에 추가(그래프 확인용)

plt.plot(k_range, scores) ### 이웃수에 따른 결과값
plt.xlabel("Value of k fro KNN")
plt.ylabel("Accuracy Score")
plt.title('Version2')
plt.show() ### 이웃수에 따른 결과값 그래프

## version 3(Train과 Test로 나누고, KNN분류기)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5) 
### random_state(임의 상태 매개변수) :  재현성을 보장 >> 실행할 때 마다 결과값이 다르게 나오는 걸 방지하기 위함이다.
### 훈련용 데이터와 테스트용 데이터는 어떤 기준으로 데이터가 분류 되는 것일까?
### 기본적으로는 모델에 내장 되어 있는 난수 생성기 시스템의 규칙을 따른다.
### 해당 규칙으로는 시스템 시간, 기타 소스 등이 있다. 이 말은 즉 코드 실행할 때 마다
### 분류된 데이터가 리셋 된다는 말이다. 이걸 방지하고자 데이터를 분류 하는데 기준이 되는
### 난수의 값을 임의로 셋팅 해주는 것이다. 
### 수가 5든 100이든 상관없다. 임의로 아무 수나 지정해주면 된다. 

k_range = list(range(1, 26)) ### 이웃수 범위 지정 왜?? 
scores = [] ### k(이웃수)의 따른 예측값 정확도 저장 변수
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k) ### 최근접이웃 객체 생성(이웃수 지정)
    knn.fit(X_train,y_train) ### knn 모델 데이터 학습 시키기
    y_pred = knn.predict(X_test) ### 학습이 완료된 knn 예측값 
    scores.append(metrics.accuracy_score(y_test, y_pred)) ### 예측값 리스트에 추가(그래프 확인용)

plt.plot(k_range, scores) ### 이웃수에 따른 결과값
plt.xlabel("Value of k fro KNN")
plt.ylabel("Accuracy Score")
plt.title('Version3')
plt.show() ### 이웃수에 따른 결과값 그래프

## version 4(로지스틱 회귀)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

### k(이웃수)의 따라서 새로운 데이터의 형태가 달라진다.
### k는 데이터의 민감도와 관련이 있다. 왜??
### 최근접 이웃 알고리즘(KNN)의 원리를 알아야한다.
### 새로운 데이터가 들어온다. 그래프 어딘가에 찍힌다.
### 새로운 데이터의 주변에는 기존 데이터들이 분포해 있다.
### 기존 데이터가 어떤 형태를 가지는 가에 따라 새로운 데이터의
### 형태가 정해진다. 그럼? 기존 데이터 몇개를 기준으로 판단을 하는 걸까?
### 여기서 몇개가 k(이웃수)이다. 이웃수에 따라서 새로운 데이터의 형태가 정해질텐데
### 그럼 이웃수가 많으면 좋을까? 적으면 좋을까? 당연 상황에 따라 다르다.
### 이웃수가 적을 때 : 기존 데이터가 정말 명확해야한다. 즉 1 아니면 2 이런 식으로 답할 수 있어야한다.
### 이웃수가 많은 때 : 땅따먹기라고 생각하면 될듯하다. 즉 데이터를 판단할 때 사용되는 특성들이 많을 때? << 생각이 필요한 부분.
 
## version1(이웃수 고정)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print(knn.predict([[6, 3, 4, 2]]))
### 이웃수를 시작부터 고정할 수 있지만, 모델의 성능을 높이기 위해서 
### k값을 범위로 주고 하나씩 전부 돌려본 다음 최상의 값이 나온 값을 사용하기 위함이다.





