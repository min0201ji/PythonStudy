# 정수 2개를 입력 받아서 두수 사이의 합을 구하는 프로그램 작성 (for문 사용)

x = int(input('숫자1 입력: '))
y = int(input('숫자2 입력: '))
sum = 0

for z in range(x,y+1):
    print(z)
    sum += z
print('%d 부터 %d 까지의 합: %d'%(x, y, sum))

# # 선생님 답
# print('숫자 1이 더 작은 정수를 입력하세요')
# num1 = int(input('숫자1 입력: '))
# num2 = int(input('숫자2 입력: '))
#
# sumx = 0
#
# for x in range(num1, num2+1):
#     sumx += x
# print(sumx)

