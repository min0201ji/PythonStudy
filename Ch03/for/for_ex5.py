# 다중 for문을 사용하여 다음과 같이 출력
for y in range(3):
    for x in range (1,5):
        print(x, end=' ')
    print()


"""
a = 0
for i in range(3):
    # a += 1 # 이 문장의 수행 횟수는? 3회
    for j in range(4):
        a += 1 # 이 문장의 수행 횟수는? 12회
        print(a, end="\t")
        a += 1 # 최종 a의 값은? 12회
    print()
"""

