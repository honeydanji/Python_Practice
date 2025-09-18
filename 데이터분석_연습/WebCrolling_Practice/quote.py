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


url = 'https://quotes.toscrape.com/'
html = ur.urlopen(url)
# ur.urlopen(url)을 이용해 url 주소에 해당하는 웹 사이트를 불러오고 HTML 객체에 저장한다.
# html.read()[:100]
# read()를 이용해 html에 뭐가 들어 있는 지 알 수 있다. 
soup = bs(html.read(), 'html.parser')
# print(soup) # 지정한 url에 html 형식으로 모든 데이터가 출력된다.
# print(soup.find_all('span')) # 지정한 url에서 <span>태그와 관련된 모든 것을 출력한다.
quote = soup.find_all('span') # <span>태그만 뽑아서 quote 객체에 저장한다.
quote[0].text # .text : quote안에 있는 리스트 요소중에서 속성값이 text인 것만 추출한다. 이렇게 하면 태그는 날아간다.

#for i in quote: #quote 리스트에서 모든 요소의 텍스트만 추출한다.
#    print(i.text)

for i in soup.find_all('div', {"class" : "quote"}): 
    print(i.text) 
# 위 코드를 설명하면 아래와 같다
# <div> 태그안에 둘러 쌓여있고 class(속성값)가 quote인 값들 중에서 속성값이 text인 값만 출력하겠다.










