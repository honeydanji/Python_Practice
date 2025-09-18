## Series 
# 1. 1차원 배열과 비슷하다.
# 2. Pandas의 클래스다.
# 3. 출력할 때 인덱스를 지정해주지 않으면 0번부터 셋팅된다.
# 4. 인덱스 값을 따로 정해줄 수 있다.

from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao)

# 인덱스 값만 출력
for date in kakao.index:
    print(date)

# 요소 값만 출력
for ending_price in kakao.values:
    print(ending_price)

#구조는 리스트와 비슷한데 출력은 인덱스와 값이 동시에 나온다.


## Series 연산
# 1. 연산을 하게 되면 서로 같은 인덱스를 자동으로 찾아서 더해준다.
# 2. 인덱싱 순서가 달라도 상관없다. 인덱싱이 같냐 틀리냐만 구분지으면 알아서 연산을 해준다.

mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
print(merge)
