# 가위, 바위, 보 게임

# 데이터 입력 받기
sohee = input('이소희 입력: ')
sojin = input('문소진 입력: ')

# 소희가 이기는 모든 경우의 수를 if 조건으로 생성
if (sohee == '가위' and sojin == '보') or (sohee == '바위' and sojin == '가위') or (sohee == '보' and sojin == '바위'):
    print('소희가 이겼습니다!')
elif sohee == sojin: # 비기는 경우
    print('비겼습니다!')
else:
    print('소진이가 이겼습니다!')





