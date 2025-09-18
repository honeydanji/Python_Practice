import seaborn as sns # 데이터셋
import pandas as pd # ??
import xgboost as xgb # 다중분류모델
import matplotlib as plt # 그래프(시각화)
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
# 그리드서치사용, 데이터를 훈련용과 테스트용 분류 가능, 교차검증 가능
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
# 혼동 행렬, 분류보고서 라이브러리
from sklearn.preprocessing import LabelEncoder
# 라벨인코딩 사용 가능(객체 > 숫자 변형)

# 그래프 한글 표현
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

### 목표 : 펭귄의 종을 분류해라!

## 데이터 준비
penguins = sns.load_dataset('penguins')
print(penguins['species'].value_counts())

## 데이터 구성 확인
print(penguins.head()) ### 앞에서 5개
print(len(penguins)) ### 데이터 수 
print(penguins.dtypes) ### 데이터 타입 > 라벨인코딩 사용여부 판단.

## 데이터 처리
penguins = penguins.dropna(subset=['sex']) ### 결측치 제거 >> 상황에 따라서.
print(penguins.head()) ### 결측치 제거후 데이터 확인

colums_delete = ['island'] ### 삭제데이터 변수 초기화
penguins = penguins.drop(columns=colums_delete) ### 해당 열 삭제후 저장

for colums in penguins.columns: ### 펭귄 특성 하나씩 가져와서
    if penguins[colums].dtypes == type(object): ### 해당 열의 타입 검사
        penguins[colums] = LabelEncoder().fit_transform(penguins[colums]) ### 조건이 일치하면 전부 숫자타입으로 변환

## 데이터 분리하기
X = penguins.drop("species", axis=1) ### 타겟변수 제거
y = penguins["species"] ### 타겟변수 저장 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y) ### 테스트 데이터 30% , 대상변수 y 지정


## 모델 선정 및 설정
param_grid = { ### 딕셔너리 형태로 저장
    'learning_rate' : [0.1, 0.2, 0.3, 0.4, 0.5], ### 학습률 지정
    'max_depth' : [3, 4, 5, 6, 7, 8], ### 트리 깊이
    'n_estimators' : [50, 100, 200, 300] ### 트리 수
}

xgb_model = xgb.XGBClassifier(use_label_encoder = False, eval_metric = 'mlogloss') ### 모델 객체 생성, 라벨인코딩x, 알고리즘선정
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=3) ### 그리드서치 객체 생성, 모델선정, 하이퍼파라미터선정, 데이터분할선정

scores = cross_val_score(grid_search, X_train, y_train, cv=5) ### 교차검증 객체 생성, 데이터선정, 검증을 몇개로 나눠서 할건지 선정
print("교차 검증 점수: ", scores) ### 점수 출력
print("평균 교차 검증 점수: ", scores.mean()) ### 교차 검증 평균 점수

grid_search(X_train, y_train) ### 그리드 서치 학습 >> 최상의 하이퍼파리미터 조합을 차기위해서.

grid_search.best_estimator_.get_params()['learning_rate'] ### 최적 학습률 
grid_search.best_estimator_.get_params()['max_depth'] ### 최적 최대 깊이 
grid_search.best_estimator_.get_params()['n_estimators'] ### 최적 부스팅 스테이지 

best_xgb_model = grid_search.best_estimator_ ### 최상의 하이퍼파라미터조합을 가진 모델 설정

y_pred = best_xgb_model.predict(X_test) ### 만들어 놓은 모델을 이용해서 값을 예측한다.
print("혼동 행렬: \n", confusion_matrix(y_test, y_pred)) ### 테스트용 데이터와 예측용 데이터를 비교해서 행렬로 나타낸다.
print("분류 보고서: \n", classification_report(y_test, y_pred)) ### 정밀도, 정확도 등 여러가지 메트릭의 수치를 나타낸다.

accuracy = accuracy_score(y_test, y_pred) ### 비교값을 수치로 출력한다.
print(f"Accuracy: {accuracy}") ### 정확도 출력

## 데이터 시각화
importance = best_xgb_model.feature_importances_ ### 특징들의 중요도를 모델을 돌리겠다?

for i, v in enumerate(importance): ### enumerate() : 해당 값을 튜플로 만들어 준다. >> 인덱스와 원소를 반복문을 통해 출력한다.
    print('Feature: %0d, Score: %.5f' % (i, v)) ### 출력

plt.figure(figsize=(10, 5)) ### 그래프 크기 설정
plt.barh([x for x in range(len(importance))], importance, tick_label=X_train.columns) ### 특징들을 x, y 위치 바꿔서 bar 형태로 그려준다.
plt.title('펭귄 신체데이터') ### 제목
plt.xlabel('중요도') ### 알지?
plt.show() ### 알지?

