# 7월6일 (화) -5교시
# 에러 (Error)
# 문법적 오류나 실행 시간에 잘못된 메모리 접근 오류, 논리 오류, 사용자의 잘못된 입력 오류 등
# 오류가 발생하면 프로그램 중단되고 에러 메시지 출력
# 발생되는 에러 예 :
# ZeroDivisionError : 0으로 나누었을 경우
# FileNotFoundError : File을 못 찾았을 경우
# IndexError : 리스트 등에서 인덱스 잘못되었을 때

"""
예외 처리 방법
try … except 문 사용
예외 처리 문 형식

try:
	(예외 발생 가능) 문장
except 예외 유형:
	예외 처리 문장
else:
	예외 없을 때 수행 문장
finally:
	예외 유무와 상관 없이 항상 실행되는 문장
"""

print('=== 에러 확인 ===')

# ZeroDivisionError: division by zero
# print(10/0)

# TypeError
# TypeError: can only concatenate str (not "int") to str
# print('나이: ' + 23 + '살')

# NameError
#print(b) #name 'b' is not defined

# ValueError
# c=100
# print('%d%' %c) #: incomplete format

# SyntaxError (문법에러)
# if x > 10 #invalid syntax
#     print('박민지')

# IndexError
# a = [1,2,3,4]
# print(a[5]) #list index out of range

# UnboundLocalError (내부적으로 사용하는 변수의 정의를 못해서 나타난 에러)
# def add():
#     a = a + 1 # local variable 'a' referenced before assignment
#
# add()

# ModuleNotFoundError
# import mydodule # No module named 'mydodule'

# FileNotFoundError
# f = open('exception.txt','r') #[Errno 2] No such file or directory: 'exception.txt'

# OSError : 파일 경로는 운영체제 권한이기 때문에 운영체제에서 나타난 에러
# 경로명에 ₩(\) 사용하면 에러 - ₩₩(\\) 사용하면 에러 안남
# f = open('c:\PythonStudy\file_t2.txt','w')












