import os
os.system('cls')

Text='  Apple      is a    fruit '
i=0
n=len(Text)
count=0
while i < n:
    if i < n and Text[i]==' ':
       i+=1
    if i < n and Text[i]!=' ':
       count+=1
print(count)



print('Hi')
print(Text)