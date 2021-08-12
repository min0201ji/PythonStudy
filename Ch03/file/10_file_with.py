# 7월6일 (화) - 5교시

with open('test3.txt','w') as f:
    f.write('hello')

file = 'test4.txt'
data = 'Python Programming\n' \
       'R programming\n' \
       'web programming'

with open(file,'w')as f:
    f.write(data)