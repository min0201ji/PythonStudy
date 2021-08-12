# sort(): 리스트를 정렬, 원본 리스트 변경
scores = [90,78,81,64,89] ; print()
scores.sort() # 기본 오름차순 정렬
print(scores) #[64,78,81,89,90]

scores = [90,78,81,64,89] ; print()
scores.sort(reverse=True) #내림 차순 정렬
print(scores)

scores = [90,78,81,64,89] ; print()
scores.reverse() # 원소의 위치를 역순으로 변경(정럴은 안함)
print(scores) # [89,64,81,78,90]

## 문자의 정렬 - 대문자 < 소문자, A~Z, a~z(아스키코드때문) ##
char = ['b','A','d','C']
char.sort() #오름차순 정렬
print(char)

char = ['b','A','d','C']
char.sort(reverse=True) #내림차순 정렬
print(char)

# 대소문자 구별없이 정렬 #
# key = str.lower (전부다 소문자로 생각하고 정렬 부탁하3 이란 의미)
char = ['b','A','d','C']
char.sort(key=str.lower)
print(char)

# 대소문자 구별없이 내림차순 정렬
char = ['b','A','d','C']
char.sort(key=str.lower, reverse=True)
print(char)

# 문자열은 첫 문자로 정렬됨
ids = ['SKY','BLUE','red','eBook','GREEN']
ids.sort() # 오름차순 정렬 - 첫 문자로 정럴
print(ids)

# 대소문자 구별 없이 정렬
ids = ['SKY','BLUE','red','eBook','GREEN']
ids.sort(key=str.lower) # 오름차순 정렬 - 첫 문자로 정럴
print(ids)

# sorted(): 원본을 유지하면서 정렬된 새로운 리스트 반환
a = [3,5,2,1,4]
b = sorted(a)
print('a: ',a)
print('b: ',b)