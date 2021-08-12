# 7월2일(금) - 5교시_7월1일 연습문제 풀이

# 다음 함수를 포함하는 프로그램 작성
# 함수 이름: get_interest()
# 예금액과 이자율을 전달받아서 이자액을 구하여 반환
# deposit, int_rate, interest

# 함수 정의
def get_interest(deposit, int_rate): # 매개변수
    interest = deposit * int_rate /100
    return int(interest) # 정수형으로 반환

### 함수 호출 테스트 ###
dps = int(input('예금액 입력: '))
rate = float(input('이자율 입력(%): '))

inter = get_interest(dps,rate)
#*inter = format(get_interest(dps,rate),',') -> inter변수는 문자열


print('이자액: %d원' % inter)
#*print('이자액: %d원' % inter)
