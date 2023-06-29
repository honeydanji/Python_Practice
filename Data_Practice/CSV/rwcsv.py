import csv, os

## csv파일 읽을 때
def opencsv(filename): # 'filename.csv' 라고 적어야 한다. 
    f = open(filename, 'r') # 읽기 모드(r)로 'filename'을 연다. >> f 객체에 저장
    reader = csv.reader(f) # 객체 f를  csv.reader로 읽어 new라는 객체에 저장한다.
    output = [] # 리스트 객체를 만든다.
    for i in reader: # reader안에 있는 요소를 1나씩 output(리스트)에 저장한다.
        output.append(i)
    f.close()
    return output
# opencsv() 함수에서는 f를 파일 객체로 해 직접 open 하는 방식을 사용했다.


## csv파일 작성할 때
def writecsv(filename, the_list): # filename : 만들(작성할) 파일, the_list : csv형 리스트를 저장한 객체 즉 데이터
    with open(filename, 'w', newline = '') as f: # 새 csv 파일을 쓰기 모드(w)로 엽니다.
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)
# writecsv() 함수에서는 with 문을 사용해 코드 길이가 조금 더 짧습니다.