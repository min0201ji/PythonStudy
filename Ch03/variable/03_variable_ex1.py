name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5
level = 10

print('성명: '+ name) # '+' 대신 ',' 도 가능
print('학번: '+ str(no))
print('학년: '+ str(year))
print('학점: '+ grade)
print('평균: '+ str(average))

# 포맷코드 사용
# 문자열: %s
# 실수: %f
# 정수: %d
# 문자하나: %c

print('성명: %s' % name)
print('학번: %d' % no)
print('학년: %d' % year)
print('학점: %c' % grade)
print('성명: %.2f' % average)
print('등급: %d %%' % level) # %문자를 출력할땐 %%