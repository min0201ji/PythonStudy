# 나는 X

"""
# 사용자가 입력하는 상품명을 리스트에 추가하되 상품명 없이 엔터키를 누르면
# 입력을 종료 시키고 등록된 상품 리스트를 출력하는 프로그램

# 빈 리스트 생성
products = []

# 상품명 입력받아 리스트에 저장하는 코드
while True:
    # 입력받기
    product = input('상품 등록(엔터키 누르면 종료):')

    if product == '': # 종료 검사 코드
        break
    products.append(product)

print('등록된 상품: ',end='')

for product in products :
    print(product, end='')

"""