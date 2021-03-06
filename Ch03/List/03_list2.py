#리스트 연산
# 리스트 합치기(결합): +연산자 사용
a =[1,2,3]
b = [4,5,6]
c = a+b # a+리스트와 b리스트를 결합해서 하나의 리스트 생성
print(c)

# 리스트 곱하기(반복): * 연산자 사용
a = [1,2,3]
b = [4,5,6]
d = a * 3 #a리스트의 원소들을 3번 반복해서 원소를 생성 -> 하나의 리스트 반환
print(d)

# 리스트 내용 변경
# 인덱싱 접근, 슬라이싱 접근 모두 가능
a =[1,2,3]
a[2] = 30 # 리스트 원소 값 변경
print(a)

a[0:2] = [10,20]
print(a)

# 인덱싱을 통해 원소 값 변경
b = [4,5,6]
b[0] = [1,2,3,4] #리스트를 한 원소값으로 주면 하위 리스트로 생성
print(b)

# 빈 리스트 값 저장
c = [1,2,3,4,5,6]
c[1:3] = [] #빈리스트는 생략(삭제)해 버림
print(c)

## 문자열과 다르게 리스트는 부분 원소값 변경이 가능하다 ##