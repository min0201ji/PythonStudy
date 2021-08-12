x = eval(input("예금액 입력: "))
y = eval(input("이자율 입력(%): "))
interest = x * y * 0.01
balance = interest + x
print('-------------------------------')
print('예금액: %d 원' % x)
print('이자율: %.1f %%' % y)
print('예금이자: %d 원' % interest)
print('잔액: %d 원' % balance)
print('-------------------------------')
print('예금액: %s 원' % format(x,','))
print('이자율: %.1f %%' % y)
print('예금이자: %s 원' % format(int(interest),','))
print('잔액: %s 원' % format(int(balance),','))
