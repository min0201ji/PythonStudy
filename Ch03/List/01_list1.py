# 리스트 만들기
# 변수명 = [값1,값2,....값n]
# 변수명 = [] - 빈리스트 생성

# 단일 자료형 리스트
ints = [1,2,3,4,5]
floats = [1,1,2,2,3,4,5,5]
names = ['박민지','박민정','박준형']

# 복합 자료형 리스트
mix = [1,5.0,'박민지']

# 리스트 안에 리스트를 포함 할 수 있다.
numbers = [100,200,300,[10,20,30]]

# 리스트 반환
# 리스트 이름(명)으로 접근/ index로 각자 접근 가능
print(ints)
print(floats)
print(names)
print(numbers)
print(mix)

# 각 원소 접근 - 원소 각각을 반환
for name in names:
    print(name)
    print(type(name))

# 각 원소를 인덱스를 통해 접근(직접접근)
for i in range(0, len(ints)): # 숫자로 고정보다 따로 만들기
    print(ints[i]) # 원소의 값을 확인하기 위해 인덱싱한다

for i in range(0, len(ints)): # 숫자로 고정보다 따로 만들기
    print(i)

# 인덱스를 통해 원소에 접근
print(numbers[3])

# 리스트 각각의 값을 변수에 저장
nums = [1,2,3]
# 리스트 nums의 원소값 각각을 a,b,c 변수에 저장하시오.
# a=nums[0]
# b=nums[1]
# c=nums[2]
# 위의 방법 - 리스트각각에 저장
# 변수넣기 ex) a=b=c=0
# a,b,c = 1,2,3
a,b,c = nums #리스트 각각의 값을 차례대로 앞의 변수에 저장
print(nums)
print(a,b,c)

## 리스트 특징 ##
nums1 = [10,20,30]
# a1,b1 = nums1
# ValueError: too many values to unpack (expected 2)(list쓸 때 꼭 수를 맞춰주기)
# 왼쪽 변수의 갯수가 오른쪽 리스트 원소의 개수보다 작으면 안된다.
# a1,b1 =10,20,30

# a1,b1,c1,d1 = nums1 #ValueError: not enough values to unpack (expected 4, got 3)
# 왼쪽 변수의 개수가 오른쪽 리스트 원소의 개수보다 많아도 안됨!
# a1,b1,c1,d1 = 10,20,30
# print(a1,b1,c1,d1)

