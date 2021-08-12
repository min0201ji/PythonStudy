# default 매개변수(파라미터)
# 매개변수에 기본값 지정 - 호출할 때 인수가 넘어오면 넘어오는 인수 사용/ 인수가 안넘어오면 기본값을 사용

def greet(name,msg='안녕 :)'): # name 매개변수: 필수 매개변수로 반드시 인수가 전달되어야 함
    print(name +', ' +msg)    # msg 매개변수는 인수가 전달되는 사용, 안넘어오면 기본값 안녕 :) 사용

# 호출
greet('박민지', '잘 지내죠?') # 모든 인수 전달
greet('박민정')

"""
###### 디폴트 매개변수 사용시 주의 사항 ######
## 디폴트 매개변수는 마지막에 위치해야 한다! ##
def greet1(msg='안뇽', name):
    print(name + ', ' + msg)

greet1('박준횽') #SyntaxError: non-default argument follows default argument
# 박준횽이 line 13에 msg에 들어가게 되버림.
# greet1('박준횽','박준항') 처럼 값을 2개 줘도 안됨
"""