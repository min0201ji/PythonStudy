# 사용자로부터 숫자를 입력받아 입력된 숫자가 7이면 종료 문자를 내보내고 프로그램을 종료
# 7이 아니면 다시 입력을 받는다(while문 이용해서 작성)

# 입력양식
# 처음 입력 시:
# 숫자 입력:

# 다시 입력 시
# 다시 입력: 7

# 출력 양식
# 7 입력! 종료...

# 입력 코드

num =int(input('숫자 입력(정수): '))

# 입력 숫자가 7인지 확인
# 다시입력 반복

while num != 7:
    num = int(input("다시 입력: "))

print(num, "입력! 종료...")

# 증가값 필요없이, 조건 자체를 사용자가 설정함