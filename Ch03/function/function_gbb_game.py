# 7월7일 (수) 1교시
# 매개변수 연습문제 2 - 문제풀이, 나는 아직 안해봄

# 함수를 활용한 가위바위보 게임
# 함수명: gbb_game()
# 랜덤으로 COM 숫자를 생성해서
# 전달받은 YOU 숫자와 비교하여
# 결과 출력

# 필요 패키지 임포트: 랜덤패키지
from random import randint

# 함수 정의
def gbb_game(you_n):
    com_n = randint(1,3)

    if com_n - you_n == 1 or com_n - you_n == -2 :
        print('컴퓨터가 이겼습니다!')
    elif com_n == you_n:
        print('비겼습니다!')
    else:
        print('당신이 이겼습니다!')

    print('com: %d' %com_n)

# main(프로그램 시작점)
YOU = int(input('YOU 입력(1:가위 2:바위 3:보): '))
gbb_game(YOU)



