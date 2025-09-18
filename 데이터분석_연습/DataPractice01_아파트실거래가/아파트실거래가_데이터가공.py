import os, re, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from CSV.rwcsv import opencsv, writecsv

apt = opencsv('C:/Users/user/Desktop/Python/Data_Practice/DataPractice01_아파트실거래가/apt_202306.csv')
# print(len(apt)) # 가공해야할 자료의 수
# print(apt[0]) # 데이터 구조 파악 # 리스트안에 리스트 있는 구조. 자바 : List<int []> 라고 볼 수 있다.
# ['0시군구', '1번지', '2본번', '3부번', '4단지명', '5전용면적(㎡)', '6계약년월', '7계약일', '8거래금액(만원)', '9층', '10건축년도', '11도로명', '12해제사유발생일', '13거래유형', '14중개사소재지']


new_list = [] # csv형 리스트 만들기
new_list2 = []
new_list3 = []

# 부산에 120m^2 이상 5억 원 이하 아파트 검색
for i in apt:
    if float(i[5].replace(',', '')) >= 120 and int(i[8].replace(',', '')) <= 300000 and re.match('부산', i[0]):
        # replace를 사용해서 문자열을 정리해줘야한다. 그래야 int()를 사용할 수 있다.
        # new_list.append([i[0], i[5], i[8]]) # list에 추출한 값 저장하기.
        new_list3.append([i[0], i[5], i[8], i[9], i[13]])
    
writecsv('apt_prac.csv', new_list3) # 리스트를 csv 파일로 저장하기.