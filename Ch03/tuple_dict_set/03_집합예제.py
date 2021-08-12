# 파티에 참석한 사람이 다음과 같을 때 집합 생성하고 그림과 같이 출력
# partyA : "Park", "Kim", "Lee"
# partyB : "Park", “길동“, “몽룡”

# 집합생성
# partyA = set(['Park','Kim','Lee']) -> 도 가능
partyA = {'Park','Kim','Lee'}
partyB = {'Park','길동','몽룡'}

# print(partyA)
# print(partyB)
# set은 랜덤이기 때문에 결과도 랜덤으로 나옴!

# 파티에 참석한 모든 사람
print('파티에 참석한 모든 사람: ', partyA.union(partyB))

# 2개의 파티에 참석한 모든 사람
print('2개의 파티에 참석한 모든 사람: ', partyA.intersection(partyB))

# 파티 A에만 참석한 사람
print('파티 A에만 참석한 사람: ', partyA.difference(partyB))

# 파티 B에만 참석한 사람
print('파티 B에만 참석한 사람: ', partyB.difference(partyA))


