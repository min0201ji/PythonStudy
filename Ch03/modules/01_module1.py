# 7월2일(금) - 6교시(모듈)

# 실행 코드

# 생성한 모듈 new_calculator import 하기
import new_calculator
from new_calculator import sub # sub함수 import
from new_calculator import * # 모듈안에 있는 모든 함수 import

a=new_calculator.add(7,4)
print(a)

# sub함수를 import했으므로
# 앞에 모듈명을 적지 않고 함수명만 적어 사용 가능
s = sub(7,4)
print(s)

m=mul(7,4)
print(m)

print(div(7,4))
