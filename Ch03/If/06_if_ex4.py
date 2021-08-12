x = int(input('정수1 입력: '))
y = int(input('정수2 입력: '))
z = int(input('정수3 입력: '))

if x>y and x>z:
    print('제일 큰 수 : %d' %x)
elif y>x and y>z:
    print('제일 큰 수 : %d' %y)
else:
    print('제일 큰 수: %d' %z)