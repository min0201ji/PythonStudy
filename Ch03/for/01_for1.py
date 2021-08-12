# for문 : 정해진 횟수만큼 반복할 때 주로 사용
# 문법
# for 반복요소를 저장할 변수, in 반복을 위한 리스트 또는 범위:
# 반복문장1
# 반복문장2...

# 리스트['박민지','박민정','박준형','이소희','문소진']의 요소를 모두 출력하시오.
s_name=['박민지','박민정','박준형','이소희','문소진'] #리스트 생성
# print(s_name[0])
# print(s_name[1])
# print(s_name[2])
# print(s_name[3])
# print(s_name[4])

for name in s_name : # name이라는 변수 만들기
    print(name) #위의 print(s_name[0])...4 까지와 같은 입력임

num = [1,2,3,4,5,6,7,8,9]
# 위 리스트의 요쇼들을 각각 출력하시오
for x in num:
    print(x)
# 만약 주어진 변수의 이름이 같아도, 사실상 쓰임은 in뒤와 for문에서의 쓰임이 다르기떄문에 가능함.
# for num in num:
#   print(num) -> 가능
# 위 리스트의 요쇼들을 한 라인에 출력하시오.
print('=================================')
for x in num:
    print(x, end='')

# ==============================================
# 반복 범위 설정: range() 함수
# 특정 범위의 정수 생성
# range(10) # start, step 생략 -> 10개의 정수 0~9까지의 정수(시작은0)
# range(1,10) # step 생략 -> 1에서 9까지의 정수(start에서 stop 1 까지의 정수)
# range(1,10,2) # start에서 stop 1까지 step 간격으로 정수 생성(1에서 9까지 2씩 건너뛰면서

print()
print('=================================')

# range(10) # start, step 생략 -> 10개의 정수 0~9까지의 정수(시작은0)
for i in range(10): # 0~9
    print(i)

print('=================')

# range(1,10) # step 생략 -> 1에서 9까지의 정수(start에서 stop 1 까지의 정수)
for i in range(1,10):
    print(i)

print('=================')
# range(1,10,2) # start에서 stop 1까지 step 간격으로 정수 생성(1에서 9까지 2씩 건너뛰면서
for i in range(1,10,2):
    print(i)

# for i in range(11,21) #11~20

# for i in range(10,1):
    print(i) # 에러 없지만 실행은 됨

print('=================')
for i in range(10,1,-1):
    print(i)