import pandas as pd
import seaborn as sns

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier # 최근접 이웃 알고리즘
from sklearn.metrics import accuracy_score

# 목표 : 붓꽃 종을 분류하라!

## 데이터 불러오기
iris = sns.load_dataset('iris') 

## 데이터 분석
# print(iris.head()) ### 데이터 확인하기
# print(len(iris)) ### 데이터 수 확인하기
# print(iris.keys()) ### 데이터 key-value 확인하기 >> 데이터가 딕셔너리 형태
# print(iris.dtypes) ### 데이터 타입 확인 >> 라벨 인코딩 사용 여부 판단
print(iris.info()) ### 데이터 세부사항 확인 >> 타입, 열, 수, 결측치 전부 확인이 가능하다.
                   ### 결측치가 없기 때문에 따로 처리 하지 않아도 된다.




