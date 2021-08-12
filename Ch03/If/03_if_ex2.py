x = eval(input('짐의 무게는 얼마입니까? '))

if x <= 20:
    print('수수료 없음\n종료합니다.')
elif x >= 21:
    print('무게 초과. 수수료 20,000원 \n종료합니다.')
else:
    pass