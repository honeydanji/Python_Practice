import urllib.request as ur
import time
# urllib : 웹에서 얻은 데이터를 다루는 파이썬 패키지. 4개의 모듈이 존재한다.
# requests : urllib 4개의 모듈 중 하나인 웹 문서를 열어 데이터를 읽어오는 모듈
# from CSV import rwcsv
# 다른 파일에 존재할 때 import하는 방법
# usecsv : csv 파일을 읽고, 쓰고 할 수 있는 클래스다.
from bs4 import BeautifulSoup as bs

#  HTML/XML 파일에서 데이터를 추출하고 파싱된 데이터를 탐색하고,
#  HTML/XML 구조를 조작하기 위한 편리한 방법을 제공

while True:
    for page_num in range(1, 6):
        url = f"https://www.saramin.co.kr/zf_user/jobs/list/domestic?page={page_num}&loc_mcd=106000&cat_kewd=1757%2C1751%2C1760&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y"
        soup = bs(ur.urlopen(url).read(), "html.parser")
        # print(soup) # url 정보 확인

        # for i in soup.find_all('div', {"class" : "list_body"}):
        #     print(i.text)

        # soup.find_all('a') # 하이퍼링크 출력

        title = soup.find_all("a", {"class": "str_tit"})
        sectors = soup.find_all("span", {"class": "job_sector"})
        location = soup.find_all("div", {"class": "col company_info"})

        for i, j, k in zip(title, sectors, location):
            print(i.get("title"), end=" ")
            print(j.text)
            #print(k.text.strip())

            p_tags = k.find_all('p') #k에 저장된 것들 중에서 <p>만 들고온다.  
            for p in p_tags[:2]:
                print(p.text.strip())
            
            print("https://www.saramin.co.kr" + i.get("href"), end="\n")  # 기본 표현 줄 바꾸음 없애고 싶다면 end=" "라고 표현
            print()

    time.sleep(3600)

# https://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=106000&cat_kewd=1757%2C1751%2C1760&panel_type=&search_optional_item=n&search_done=y&panel_count=y&preview=y
# 사이트에서 구직정보 긁어오기 마무리 하기.
# 23~24 라인을 해결해야한다.

        
