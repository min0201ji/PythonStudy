# # int(문자열): 문자열을 정수로 변환
# # float(문자열): 문자열을 실수로 변환
# # str(정수 또는 실수): 정수 또는 실수를 문자열로 변환
#
# print("나는 현재"+ str(23) + "살 입니다.")
# #정수와 문자열 결합은 안되기 때문에 정수 리터럴을 문자열로 형변환
# print("나는 현재" + str(160.7) + "cm 입니다.")
#
# #----------- 시용자로부터 숫자를 입력박아 100과 더한 결과를 출력하는 프로그램
# # 사용자로부터 키보드를 이용해서 값을 입력받기 : input() - 컴퓨터는 사용자 입력을 대기하는 상태가 된다
# # 키보드로 입력되는 모든데이터는 무자열로 입력이 된다.
# # 키보드로 입력되는 숫자 데이터로 처리하고자 할때는 형변환을 진행해야 된다.
# """
# num = input("숫자를 입력하세요: ")
# # print(type(num)) class type -> str
# print(int(num) + 100)
#
# num1 = int(input('100과 더할 값을 입력하세요: '))
# print(num1 +100)
# """
#
# ##### 실수 입력
# # x = input('실수 입력: ')
# x = 'a'
# y = x * 3 # *는 문자열의 반복연산자로 사용가능
# print(y)
#
# x = float(input("실수 입력:"))
# y=x*3
# print(y)
#
# print(int(3.0))
#
# ####### 정수 -> 실수(float), 실수 -> 정수(int)
# print(int(3.456789))
#
# # format()
# # 구분자를 삽입해 줌
print(type(format(3456,','))) #문자열은 0~9 만 처리 가능
int('3456')
int(format(3456,',')) #3,456


