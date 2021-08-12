x = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))

if x == 1:
    r1 = eval(input('가로 입력: '))
    r2 = eval(input('세로 입력: '))
    print('사각형의 면적 = ', (r1*r2))
elif x ==2:
    t1 = eval(input('밑변 입력: '))
    t2 = eval(input('높이 입력: '))
    print('삼각형의 면적 = ', (t1*t2)/2)

elif x==3:
    c1 = eval(input('반지름 입력: '))
    print('원의 면적 = ', (c1**2)*3.141592)
else:
    pass

