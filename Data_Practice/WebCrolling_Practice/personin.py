import os, re
import urllib.request as ur 
# urllib : 웹에서 얻은 데이터를 다루는 파이썬 패키지. 4개의 모듈이 존재한다.
# requests : urllib 4개의 모듈 중 하나인 웹 문서를 열어 데이터를 읽어오는 모듈
# from CSV import rwcsv
# 다른 파일에 존재할 때 import하는 방법
# usecsv : csv 파일을 읽고, 쓰고 할 수 있는 클래스다.
from bs4 import BeautifulSoup as bs
#  HTML/XML 파일에서 데이터를 추출하고 파싱된 데이터를 탐색하고, 
#  HTML/XML 구조를 조작하기 위한 편리한 방법을 제공

url = 'https://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=106000&cat_kewd=1757%2C1751%2C1760&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y'
soup = bs(ur.urlopen(url).read(), 'html.parser')
#print(soup) # url 정보 확인

# for i in soup.find_all('div', {"class" : "list_body"}):
#     print(i.text)

# soup.find_all('a') # 하이퍼링크 출력

for i in soup.find_all('a', {"class" : "str_tit"}):
    print(i.get('title'))
    for j in soup.find_all('span', {"class" : "job_sector"}):
         print(j.text + " ")
    print('https://www.saramin.co.kr' + i.get('href'))
    
    
    
    # https://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=106000&cat_kewd=1757%2C1751%2C1760&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y
    # 사이트에서 구직정보 긁어오기 마무리 하기. 
    # 23~24 라인을 해결해야한다.