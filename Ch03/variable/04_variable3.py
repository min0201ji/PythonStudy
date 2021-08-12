# 화씨 온도를 섭씨 온도로 변환
fTemp = 90 # 정수변수
cTemp = (fTemp - 32)*5/9 #정수연산

print(cTemp)
print('%f' %cTemp)
print('%.3f'%cTemp)
print('%10.3f'%cTemp) # 소수점 포함 열자리

# 실수 %f 사용시 %전체자리수, .소수이하자리수f

print('화씨온도 %d 를 섭씨온도로 변환하면 %.3f 입니다.'%(fTemp, cTemp))
# 포맷문자를 위해서 반드시 변수를 괄호()로 묶어준다!