# 소희와 컴터의 대결!

# 랜덤 모듈 가져오기
from random import randint

# 난수 발생: 1번 -> 가위, 2번 -> 바위, 3번 -> 보
n = randint(1,3)

if n == 1:
    com = '가위'
elif n == 2 :
    com = '바위'
else:
    com = '보'
# 소희의 가위바위보 데이터 입력 받기
sohee = input('이소희 입력: ')

# 소희가 이기는 모든 경우의 수를 if 조건으로 생성
if (sohee == '가위' and com == '보') or (sohee == '바위' and com == '가위') or (sohee == '보' and com == '바위'):
    print('소희가 이겼습니다!')
elif sohee == com: # 비기는 경우
    print('비겼습니다!')
else:
    print('컴퓨터가 이겼습니다!')




