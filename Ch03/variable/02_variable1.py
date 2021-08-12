# 변수는 할당해놓고 사용하지 않으면 메모리 공간을 차지하게 됨
# 변수 삭제 명령어 : del
# del 변수명

c_var = 100
print(c_var)
del c_var
#print(c_var)

# 코드 블럭 주석처리: ctrl + / (window), command+/(mac)

# 무자열 값 저장
# 문자열은 큰따옴표 사용(작은따옴표도 가능)
# 여러 종류의 따옴표를 사용시에는 짝을 맞춰야 함
name = '박민지'
std_name = '박민정'
pro_name = "박춘식 '교수'"

print(name)
print(std_name)
print(pro_name)

print(name,
      std_name,
      pro_name)

address = '부산시 북구'

# 문자열을 연결하는 작업을 할때: + 연산자 사용
print(name+address) # -> 결합해서 하나로 출력
print(name, address) # -> 2개의 문자열출력
print(name+ '는 ' + address + '에 삽니다')

result = name + '는 ' + address + '에 삽니다.'
print(result)

# 문자와 숫자의 결합(연결)
age = 23

# print(name + '는 ' + age + '살 입니다.')
# 박민지는 23살 입니다.

# 값은 숫자형이지만 문자열로 처리해야 될때는 일시적으로 형태(type)를 변경시킨다
# 숫자 -> 문자 str(변수명)
print(name + '는 ' + str(age) + '살 입니다.')
# 박민지는 23살 입니다.

print(5 + age)

# 사각형의 면적을 구해서 출력하는 프로그램
# 넓이 : 100
# 높이 : 200
width = 100
height = 200

area = width * height

print('면적: '+ str(area)) #값 1개

print('면적:',area) # 값 2개

