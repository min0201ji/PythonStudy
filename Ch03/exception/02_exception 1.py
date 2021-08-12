# 7월 6일 (화) - 5교시
"""
# 예외처리 예제

# 에러종류와 상관없이 모든 에러 처리
# try~exception 구문

try:
    # print(10/0) # 에러가 발생하면 무조건
    print('나이: ' + 23 + '살')
except: # 본 구문으로 포커스가 넘어옴
    print('오류 발생!')

print('===== Exception 클래스 사용 =====')

try:
    # print(10/0) # 에러가 발생하면 무조건
    print('나이: ' + 23 + '살')
except Exception: # 본 구문으로 포커스가 넘어옴
    print('오류 발생!')
"""

# 에러 종류 명시

# try:
#     print(10/0) # ZeroDivisionError 발생 -> except로 바로 감
#     # print('나이: ' + 23 + '살') # type 에러 발생/ if 첫번째로 실행하면 -> 에러 발생 이후 문장은 실행 안함
# except ZeroDivisionError: # 0 으로 나눈 논리에서만 처리, type에러는 처리 안함
#     print('오류 발생!')

# 숫자를 입력하지 않은경우
# try:
#     num = int(input('숫자를 입력하세요: '))
#
# except ValueError:
#     print('숫자가 아닙니다')

# 에러종류 명시: as 에러 메세지 변수
# try:
#     num = int(input('숫자를 입력하세요: '))
#
# except ValueError as e:
#     print('숫자가 아닙니다',e)

## 여러개의 except 구문을 생성: 첫번째 에러만 처리 됨 ##
a = [1,2,3]

try:
    print(a[4])
    print(10/0)
except ZeroDivisionError as e:
# except (ZeroDivisionError,IndexError) as e: -> 로 한번에 처리
    print('0으로 나눌 수 없습니다')
except IndexError as e :
    print(e)
