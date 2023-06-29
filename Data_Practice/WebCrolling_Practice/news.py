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

news = 'https://www.weeklytrade.co.kr/main/index.html'
soup = bs(ur.urlopen(news).read(), 'html.parser')
#print(soup) # url 정보 확인

#print(soup.find_all('div', {"id" : "main_middle_news"}))
for i in soup.find_all('div', {"id" : "main_middle_news"}):
    print(i.text)
        

    