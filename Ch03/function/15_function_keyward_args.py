# 7월2일(금) 1교시 -

# 키워드 인수 예제

# 학생 정보를 입력받아 학생 dict를 구성하여 반환하는 함수
def studnet_info(name,age,gender):
    student = {
        'name':name,
        'age':age,
        'gender':gender
    }
    return student

# 함수 테스트(호출)
# 함수 호출시 인수를 넘겨 dict가 제대로 구성되어 반환되는지 출력
print(studnet_info(name='Park',gender='여',age=23)) # 키워드 인수
print(studnet_info('lee',20,'남')) # 위치인수
print(studnet_info('moon',gender='여',age=25)) # 위치 인수와 키워드 인수 동시 사용

### 주의!!! ###
# print(studnet_info(gender='남',age=22,'choi'))
# SyntaxError: positional argument follows keyword argument
# -> 위치인수는 키워드 인수 앞에 위치해야 합니다!

