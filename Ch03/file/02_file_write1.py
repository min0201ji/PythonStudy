# 7월6일 (화) - 3교시

# 파일에 쓰기: 파일을 쓰기모드(w)로 열고
# 파일 객체 변수와 write()메서드 출력값을 파일에 기록

# data='hi'
data = '안녕하세요'
# f=open('file2.txt','w')
f=open('file3.txt','w',encoding='utf-8')
f.write(data) # 파일에 data 쓰기
f.close()
## window는 ansi가 기본 , 맥은 알아서 되는거 같다...##
# 한글인 경우 utf를 정확하게 명시해 주어야 한다!!!




