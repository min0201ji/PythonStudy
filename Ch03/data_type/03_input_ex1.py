x = eval(input("국어 점수 입력: "))
y = eval(input("영어 점수 입력: "))
z = eval(input("수학 점수 입력: "))
total = x+y+z
average = total/3
print("총점: %d" % total)
print("평균: %.2f" % average)