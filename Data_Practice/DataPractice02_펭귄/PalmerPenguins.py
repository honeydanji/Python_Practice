import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split

### 목표 : 펭귄의 종을 예측하는 모델을 만들어라!!!

## 데이터셋 준비
penguins = sns.load_dataset('penguins') 

#print(penguins.head()) # 데이터 확인
#print(len(penguins))
#print(penguins.dtypes) # 타입 확인

## 데이터 전처리
penguins = penguins.dropna()# NaN 삭제하기
#print(penguins.head()) # NaN 삭제후 데이터 확인
#print(len(penguins)) 

colums_delete = ['island'] # 필요없는 데이터 리스트에 저장
penguins = penguins.drop(columns=colums_delete) # 열을 통채로 지워버린다.
#print(penguins.head()) # 지워진 데이터 확인
#print(penguins.info()) # 데이터 요약해서 보여준다. head랑 비슷하면서 다르다.

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

## POINT
# 그럼 왜? 펭귄 종마다 클래스를 나누는 것일까? >> 범주형모델이기 때문이다.
# 즉 데이터의 범위를 정해 놓으면 새로운 펭귄데이터(인스턴스)가 입력이 될 때 쉽게 펭귄의 종류를 예측할 수 있기 때문이다.
# 결론 : 원본 데이터에서 타겟변수를 정하고, 남은 데이터를 이용해 타겟 변수의 범주를 정한다. <<< 이게 핵심이다.
#       여기서 타겟변수는 예측 대상이 되는 것! ex) 펭귄의 종을 예측하세요., 꽃의 종류를 예측하세요. 등등 
