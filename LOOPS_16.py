import os
os.system('cls')
####################################
#        LOOPS
####################################
# i=0
# while i<10:
#  print(f'{'hi'} {'goodmorning'}')
#  if i==5:
#       break
#  i=i+1

# i=0
# while i<10:
#     i+=1
#     if i%2==0:
#         continue
#     print(f'{i}')

# print()
# j=0
# while j<10:
#     j=j+1
#     if j==7:
#         continue
#     print(f'{j}')

# print()
# k=0
# while k<12:
#     k=k+1
#     if k%2 == 1:#even numbers
#      continue
#     print(k)

# print()
# k=0
# while k<12:
#     k=k+1
#     if k%2 == 0:#odd numbers
#      continue
#     print(k)

 #@@@@@@@@@@@ NESTED LOOP @@@@@@@@@@@@@
# i=0
# while i<10:
#     i+=1
#     j=0
#     print('---------------')
#     while j<10:
#      j+=1
#      print(f'{i}*{j}={i*j}')

# k=1000
# i=k-1
# while i<k:
#     i+=1
#     j=0
#     print('='* 12)
#     while j<10:
#      j+=1
#      print(f'{i}*{j}={i*j}')

# s=10
# for i in range(s):
#     print(i)  #break
#     if i==5:
#         break
# else:
#  print('bye')
# print('\n')

# s=10
# for i in range(s):
#     if i==5:
#         continue  # continue
#     print(i) 
# else:
#      print('bye')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# i=0

# while i<10:
#     print('  #' * i)
#     i=i+1


# i=0
# j=0
# while i<20:
#       i=i+1
#       if i<10:
#           j=j+1
#       else:
#        j-=1
#        print("  #"  *j)



# print('\n')

# k=0
# while k<10:
#     k=k+1
#     if k%2 == 0:#odd numbers
#      print("  #" *(k))
#     l=0
#     while l<10:
#       l=l-1
#       if l%2==0:
#             print("  #" *l)
      

################################################
#        PATTERN PROGRAMS
################################################

n=5
for i in range(n):
    for j in range(n):
      print("*", end="  ")
    print()

print('\n','11111111111111111')

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end="  ")
    print()
    
print('\n','22222222222222222')

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="  ")
    print()

print('\n','33333333333333333')
n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print('\n')
n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()


print('\n')
n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print('\n')
n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

###################################################
# diamond star pattern
###################################################
print('\n')
n=6
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
















 


























