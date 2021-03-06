# 7월6일(화) - 8교시~~~

# super/부모/base 클래스
class person:
    # 생성자 함수
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self,food):
        print('{}은 {}를 먹습니다.'.format(self.name,food))

    def sleep(self, minute):
        print('{}은 {}분동안 잠니다.'.format(self.name,minute))

    def work(self, minute):
        print('{}은 {}분동안 일합니다.'.format(self.name, minute))

# 상속 : class 클래스명(부모클래스명)

# child/자식/sub 클래스 생성(Student, Employee)
class Student(person):
    def __init__(self,name,age):
        self.name = name
        self.age = age

# 하위 클래스에서 부모 클래스가 갖고 있는 함수(매서드)를 재 정의 하는것 -> 매서드 오버라이드
# 하위클래스(자식 클래스)에서 부모클래스의 method를 호출할 때 사용 -> super()

    def work(self,minute):
        super().work(minute) #부모클래스(super()) 메서드 work을 호출해서 실행)
        print('{}은 {}분동안 강의를 듣습니다'.format(self.name,minute))

class Employee(person): # person 상속받음
    def __init__(self,name,age):
        self.name = name
        self.age = age

bob = Employee('Bob',25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)

lee = Student('lee',19)
lee.eat('NOODLE')
lee.sleep(60)
lee.work(30) # 부모클래스의 work() 매서드와 하위 클래스의 work 매서드가 같이 호출되게 됨

