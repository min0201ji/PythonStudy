# 나는 못함!
"""

# 빈리스트 생성
scores = []
for i in range(5):
    score = int(input('학생' + str(i+1) + '점수 입력: '))
    # 리스트에 추가하고
    scores.append(score)

# 누적 변수 생성
sum_s = 0
count = 0 # 80점 이상인 학생 수를 세기위한 변수
# 리스트의 각 점수 합계
for s in scores:
    sum_s += s # 총점계산
    if s >= 80:
        count += 1

# 평균 계산
avg = sum_s/len(scores)

# 총점 평균 출력
print('총점: %d' %sum_s)
print('평균: %.2f' %avg)
print('80점 이상 학생: %d명' % count)

"""