# input("프롬프트 문자열") -> 입력되는 모든 값은 문자열로 변환
# x = int(input("숫자 1 입력(정수만 입력하세요!): ")) #실수 형태 입력시 에러
# y = float(input("숫자 2 입력: "))
# z = eval(input("숫자 3 입력 :"))
# # eval은 사용자가 입력하는 type에 따라서 바꿔준다.(ex- 3-int, 3.132134 - float)
#
# print(type(z))

# 수식을 입력해도 수식의 계산값으로 변환을 진행함
a = eval(input('수식입력: '))
print(a)
print(type(a))