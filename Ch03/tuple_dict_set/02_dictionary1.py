# 딕셔너리
# 키(key)와 값(value)의 한 쌍을 요소로 갖는 자료형
# 딕셔너리 = {키1:값1, 키2:값2, … }
# d = {1:’a’, 2:’b’, 3:’c’}

# 딕셔너리의 특징
# 순서가 없다. 따라서, 인덱스로 접근할 수 없다
# 중괄호 {} 사용
# key를 통해서만 접근
# key는 숫자, 문자 다 가능
# key:value 한 쌍을 item이라고 한다
# 쉼표(,)로 item 구분

# dictionary 만들기
# key : value 로 이루어짐

# set -> 원소만

d = {1:'a'}
print(d)
print(type(d))

# 두번째 요소(item) 추가 (key - 2, value - 'b') 두번째는 순서랑 상관없이 그냥 요소추가
d[2] = 'b' # 새로운 요소를 만드는데 키가 2인것 인덱스 아님!
print(d)

print('====================')

# 세번째 요소(item) 추가
# key 는 문자도 가능!
d['test'] = 'value Test'
print(d)

print('====================')

member = {'name':'홍길동','phone':'1234-1234','birth':'10/15'}
print(member)

# item 추가 : address: 서울
member['address']='서울'
print(member)

# 길면 여러 줄로 입력해도 됨
naver = {
    'name':'naver',
    'url':'www.naver.com',
    'userid':'nv',
    'password':'1234'
}

print(naver)

print('====================================')

# dict 필수 함수
# 딕셔너리 주요 함수
# 딕셔너리.keys() : key만 추출해서 리스트로 반환
# [1, 2, 3]
# 딕셔너리.values() : value만 추출 리스트로 반환
# [‘a’, ‘b’, ‘c’]
# 딕셔너리.items() :
# (key:value)의 튜플을 추출해서 리스트로 반환
# [(1:’a’), (2:’b’), (3:’3’)]

print(naver.keys()) # key를 리스트형태로 반환
print(naver.values()) # value 리스트 형태로 반환
print(naver.items()) # (key,value)-튜플 리스트 반환

# dict_keys(['name', 'url', 'userid', 'password'])
# dict_values(['naver', 'www.naver.com', 'nv', '1234'])
# dict_items([('name', 'naver'), ('url', 'www.naver.com'), ('userid', 'nv'), ('password', '1234')])

print(type(naver.keys())) # key를 리스트형태로 반환 <class 'dict_keys'>
print(type(naver.values())) # value 리스트 형태로 반환 <class 'dict_values'>
print(type(naver.items())) # (key,value)-튜플 리스트 반환 <class 'dict_items'>

print('=============================')

# 리스트로 변환: list() 함수사용
to_list = list(naver.keys())
print(to_list)
print(type(to_list))

# 튜플로 변환 : tuple() 사용
to_tuple = tuple(naver.keys())
print(to_tuple)
print(type(to_tuple))

# 딕셔너리 특정 item value 참조 : key 를 이용해서 참조
member = {'name':'홍길동','phone':'1234-1234','birth':'10/15'}
print(member['name'])

print('==================================')

# key 리스트의 각 요소 출력
for key in naver.keys():
    print(key)

print('==================================')

# value값 출력
for value in naver.values():
    print(value)

print('==================================')

# item출력
for item in naver.items():
    print(item)

print('==================================')

# key로 value 찾기 :dic변수[key] 를 이용한 접근 or dic변수.get(key) 를 이용한 접근
print(naver['userid'])
print(naver.get('password'))

# 존재하지 않는 경우 : link 키가 없는 경우
# print(naver['link']) # KeyError: 'link'
print(naver.get('link')) #None 값 반환
print(naver.get('link','없음')) # 없음

# if 문에서 get() 사용
insert_key = 'link'
if naver.get(insert_key) is None:
    print(insert_key + '에 대한 data가 없습니다.')

# 존재 여부만 확인: in/ not in 연산자 사용
print('link' in naver)
print('link' not in naver)

print('==================================')

# 리스트 함수 확인 - dir로 리스트와 관련된 값 확인 가능
my_list = []
print(dir(my_list))

# 튜플 함수 확인
my_tuple = ()
print(dir(my_tuple))

# 딕셔너리 함수 확인
my_dictionary = {}
print(dir(my_dictionary))






