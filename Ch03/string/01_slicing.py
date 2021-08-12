# String(문자열)의 slicing

#문자열
# -> 문자의 나열 - 여러 문자로 이루어져 있기 때문에 한문자당 하나의 메모리 공간을 차지한다.
# "abc" -> a한칸, b한칸, c한칸의 공간을 차지하고 공간이 연속되어 있

# 인덱싱과 슬라이싱이 가능

# 문자열 생성 - '',"",""" """
crawling = "Data crawling is fun"
parsing = 'Data parsing is also fun'

# 전체 문자열 출력(반환)
print(crawling)
print(crawling[:])

# 특정 인덱스의 문자 출력 - 파이썬의 인덱싱은 0부터 시작함
print(crawling[0]) #첫번째 문자
print(crawling[-1]) #마지막 문자
print(crawling[2]) #인덱스2번째, 3번쨰 문자
print("=============================")
# 슬라이싱 예제
# 변수명[시작인덱스 : stop+1 인덱스]
print(crawling[0:4]) #0~3번 인덱스 까지
print(crawling[5:16]) # 5~ 15번 인덱스 까지
print(crawling[17:]) # stop을 생략하면 끝까지 - 17~ 끝까지
print(crawling[19]) # 인덱스 19번 문자
print(crawling[-1:]) # 시작은 마지막문자에서 끝까지 - 마지막문자
print(crawling[-1]) # line28과 같다
print(crawling[:-1]) # 처음부터 마지막 전 문자까지
print(crawling[16:16+4]) # 16:20 과 동일, 16~19까지

print("=============================")

print(parsing) #Data parsing is also fun
print(parsing[5:]) #parsing is also fun
print(parsing[:15]) # Data parsing is
print(parsing[:]) # Data parsing is also fun
# 다 맞춤! 뿌듯! :)

print("===========================")

######  주의!!!!! ######

string = 'happy day!!!'

string_a = string[:5] # 가능
print(string_a)

#string_a = string[:5]
# string[:5] ='abc' # 불가능
#print(string)
# 문자열의 부분(일부) 수정은 불가능

#but
#string = 'abc' # 문자열변수 전체 수정은 가능
