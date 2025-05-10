import os
os.system('cls')

# **************************
# **************************
# a=12 #global
# b=6
# x=a+b
# print('x:',x)

# a=25
# b=4
# z=a-b
# print('z:',z)

# def multiply():
#     global a,b
#     a=10 #local variable
#     b=3
#     y=a*b+x
#     print('multiplication of a and b is:',y)

#     if (a>b):
#         print('a is greater than b')
#     elif(a<b):
#          print('a is smaller than b')

# multiply()

# def subtract():
#     T=a-b
#     print('subraction of a and b is:',T)

# subtract()

k=10
l=2
def divide():
    global k,l
    k=100
    l=25
    z=k/l
    print(f'Division of two numbers is:{z}')

divide()
   