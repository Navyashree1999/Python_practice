num = [1, 2, 5, 8, 0, 6, 4, 6, 9]
find = 0
i = 0
while i < len(num):
     if num[i] == find:
        i+=1
        continue
     print(num[i])
     i+=1
else:
    print("Sucessfull")

i=0
name = 'navya'
while i < len(name):
    if name[i]=='v':
        i += 1
        continue
    print(name[i])
    i+=1
print('\n')

num = [1,2,3,4,5,6,7]
i=0
while i < len(num):
    if num[i]==5:
        i+=1
        continue
    print(num[i])
    i+=1

print('\n')

num = [1,2,3,4,5,6,7]
i=0
while i < len(num):
    if num[i]==5:
        i+=1
        break
    print(num[i])
    i+=1
print('\n')

name = 'Hello World'
i=len(name)-1
reverse_string= ""
while i>=0:
    reverse_string+= name[i]
    i-=1
print(reverse_string)

print('\n')

num = [1,2,3,4,5,6,7,8,9]
i=len(num)
rev_num = []
while i>0:
    rev_num.append(i)
    i-=1
print(rev_num)











