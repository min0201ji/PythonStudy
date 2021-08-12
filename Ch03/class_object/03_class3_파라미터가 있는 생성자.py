# 7월6일(화) - 7교시

# 생성자 함수 추가 2
# __init__(self, 초기값 파라미터1, 초기값 파리미터2...)

# 클래스 정의
# name, age 2개의 속성을 정의 - 생성자 파라미터로 기본값을 저장
class person:
    # 생성자 함수
    def __init__(self,name,age=10):
        self.name = name
        self.age = age
        print(self,'is generated')

# width, height 2개의 속성을 정의 - 생성자 파라미터로 기본값을 저장
class Rectangle:
    # 생성자 함수
    def __init__(self,width,height):
        self.width = width
        self.height = height

# person 객체생성
p1 = person('Bob',30)
p2 = person('Kate',20)
p3 = person('Aaron',)

print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)

# Retangle 객체 생성
# r0 = Rectangle() - 파이썬이 만들어주는 기본 생성자
r1 = Rectangle(3,4)
r2 = Rectangle(10,2)

print(r1.width,r1.height)
print(r2.width,r2.height)
