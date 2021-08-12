# 7월6일(화) -4교시
# append(): 파일 긑에 추가하는 기능
# 파일 열기 모드: a

f=open('test2.txt','a')

append_data = '\nPython programming'
f.write(append_data)

#
f=open('test2.txt','r') # window에서 ansi때문에 오류나면 encoding='utf-8' 로 지정!
print(f.read())

f.close()
