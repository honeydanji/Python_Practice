import os, re, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CSV.rwcsv import opencsv, writecsv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/user/Desktop/Python/Data_Practice/DataPractice01_아파트실거래가/apt_prac2.csv', encoding = 'cp949')
# print(df.head()) # 앞에서 5개행 출력
# print(df.tail()) # 뒤에서 5개행 출력

# print(df.가격)
# print(df.loc[:10, ['가격', '층']])


# 데이터 추가하기
df['단가'] = df.가격.str.replace(',', '').astype(int) / df.면적.astype(float)
# 선택열을 기준으로 오름차순으로 정렬하기
df.sort_values(by = '단가')

