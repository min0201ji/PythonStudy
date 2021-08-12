# 7월6일 (화) 7교시

# 1. 숫자를 하나 증가하는 메서드
# 2. 숫자를 0으로 초기화 하는 메서드
# 3. 숫자를 저장하는 속성(멤버변수) - 생성자 함수
# 4. 현재 숫자값을 출력하는 메서드

class Counter:
    def __init__(self):
        self.num = 0

    def increment(self):
        self.num += 1

    def reset(self):
        self.num = 0

    def print_current_value(self):
        print('현재 저장되어 있는 숫자값은: ', self.num)

# 객체 생성
c1 = Counter()
c2 = Counter()
c3 = Counter()

# 질문: c1 인스턴스와 c2 인스턴스는 공통의 멤버변수 num을 사용한다. (O, X)
# => X (메모리 공간 자체가 다름!)

c1.increment()
c2.increment()
c1.increment()
c2.increment()
c1.increment()
c2.reset()
c1.print_current_value()
print(c1.num)
c2.print_current_value()
print(c2.num)
print(c3.num)

# instance method - 객체로 호출(일반 method)
# 메쏘드는 객체 레벨로 호출 되기 때문에, 해당 메쏘드를 호출한 객체에만 영향을 미침
# class method(static method) – @staticmethod 사용
# 클래스 메쏘드의 경우, 클래스 레벨로 호출되기 때문에, 클래스 멤버 변수만 변경 가능
# class Math:    @staticmethod    def add(a, b):        return a + b    @staticmethod    def multiply(a, b):        return a * bMath.add(10, 20)Math.multiply(10, 20)
