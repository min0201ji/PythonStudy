# for_ex6 -1번 문제
# for a in range(4):
#     for b in range(5):
#         print('*', end=" ")
#     print()
#
# print('================')

# for_ex6 -2번 문제
# for a in range(1,6):
#     print('*'*a)
#
# print("=================")
#FT박선익 선생님의 도움을 받았다!

# for_ex6 -3번 문제
# for a in range(5,0,-1):
#     print('*'*a)
#
# print('==================')

# for_ex6 -4번 문제
# for a in range(0,10):
#     if a % 2 != 0:
#         print('*'*a)

"""
#선생님 강의
for i in range(0,5):
    #스페이스 찍기
    for j in range(4,i,-1): # i값 -> 0,1,2,3,4(우리가 원하는것)
        print(' ',end='')
    # 별 찍기
    for k in range(0,i*2+1): #i값의 변화: 0,1,2,3,4, -> 1,3,5,7,9->(i*2+1)
        print('*',end='')

    print()
"""

# for_ex6 -5번 문제

# for a in range(9,0,-1):
#     if a % 2 != 0:
#         print('*'*a)

"""
#선생님 강의

# 행을 늘리면 찍히는 별도 늘어나게 수정
n=5
for i in range(0,n):
    # 스페이스 찍기
    for j in range(0,i):
        print(' ', end='')
    # 별 찍기
    for k in range(n*2-1,i*2,-1):
        print('*',end='')

    print()
"""




