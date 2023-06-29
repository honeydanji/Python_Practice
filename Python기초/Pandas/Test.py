# 리스트 사용
mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

# 리스트 반복문 출력
for stock in mystock:
    print(stock)


# 튜플 사용
# : 요소를 수정할 수는 없지만 속도가 굉장히 빠르다.
mystock2 = ('카카오', '네이버')
print(mystock2[1])

# 딕셔너리
# : 요소들이 key : value 로 구성되어 있다. key값을 이용하면 요소를 굉장히 빠르게 찾을 수 있다.
mystock_dic = {'key1': '다음', 'key2': '야후'}
print(mystock_dic['key1'])
print(mystock_dic['key2'])

# 딕셔너리 예제
kakao_daily_ending_prices = {'2016-02-19': 92600,
                             '2016-02-18': 92400,
                             '2016-02-17': 92100,
                             '2016-02-16': 94300,
                             '2016-02-15': 92300}
print(kakao_daily_ending_prices['2016-02-19'])

