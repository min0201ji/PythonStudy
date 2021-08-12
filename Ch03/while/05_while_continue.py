# continue문
# 반복문 수행 중에 continue문을 만나면
# 현재 시점에서 중단하고, 다음 문장을 수행하지 않음
# 다음 반복을 계속 수행한다.

x = 0
while x < 10:
    x += 1
    if x % 2 == 0: #짝수이면
        continue # 특정 조건만 건너뜀
    print(x)