# 7월2일(금) - 8교시
'''
# 내가 풀다가 만거

def order(price, qty):
    amount = price * qty

    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0

    total = amount - discount

    return int(amount,discount,total)

p = int(input('상품 가격 입력: '))
q = int(input('주문 수량 입력: '))
a = order(p,q)

print('주문액: %d원 ' % a)
'''

# 선생님의 문제풀이 7월7일(수) - 1교시

# order(qt,pr)

def order(qt,pr):
    # 주문액 구하기
    amt = pr * qt

    # 할인액 구하기
    if amt >= 100000:
        dis = int(amt*0.1)
    elif amt >= 50000:
        dis = int(amt*0.05)
    else:
        dis = 0

    # 총 지불액 구하기
    tot = amt - dis

    return amt, dis, tot

# main 부분
# 사용자로부터 가격과 수량 입력
price = int(input('상품 가격 입력: '))
qty = int(input('주문 수량 입력: '))

print('==============================')

# 처리: order() 호출
amount, discount, total = order(price,qty)

# 출력:
print('주문액: %d 원' %amount) # 천단위 구분하고 싶으면 %s, %format(amount)
print('할인액: %d 원' %discount)
print('지불액: %d 원' %total)


