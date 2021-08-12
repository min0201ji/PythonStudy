# 사용자가 입력한 이름이 명단 리스트에 있는지 검색 후 결과를 출력

# 입력 양식
# 이름 입력: 박민지

# 출력 양식:
# 명단에 있습니다. 또는 명단에 없습니다.

namelist = ['박민지','박민정','박준형','박웅이']

# 이름 입력
search_name = input('이름 입력: ')

for name in namelist:
    if search_name == name: # 명단에서 이름을 찾은 경우 - 반복 중단
        find = True
        break # 반복을 탈출하는 제어코드
    else: #명단에서 못 찾은 경우 - 반복을 계속되게 만든다.
        find = False

# print(find)
if find: # if find == True:
    print('명단에 있습니다.')
else:
    print('명단에 없습니다')

