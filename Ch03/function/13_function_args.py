# 가변 길이 매개변수: 1개의 배개변수로 개수가 정해지지 않은
# 여러개의 값을 전달 받을 때 사용하는 매개변수
# 매개변수형태: *매개변수이름

def show_players(*players):
    print(players)
    print(type(players)) #<class 'tuple'> 가변길이 매개변수의 *args 형태는 튜플 형태로 전달된다
    for player in players:
        print(player, end=' ')
    print()

show_players() # 가변길이는 0~(0부터 시작)
# show_players('박지성')
# show_players('박민지','박민정')
# show_players('박준형','곤흥민','배고파')









