import os
os.system('cls')

S="kiran is a good boy"
print(S)

print(S.replace ('good','bad'))
print(S.count('good'))
print(S.split(' ',4))
print(S.index('a',5))

# x=45
# x=str(x)   #00045
# print(x.zfill(5))

# x=457352526
# x=str(x)   #00045
# print(x.zfill(5))

# print(''.join(S))
# print('^' .join(S))

# print(S.isupper())
# print(S.islower())

# firstname='pavan'
# lastname='singh'
# fullname=firstname+" "+ lastname
# print(fullname)

# #user input
# x=input('enter number>')



# x=input('enter number>')
# if x.isdigit(): #isdigit() is a string method so we have to give input for x in ''
#     x=int(x)
#     print(x+5)
# else:
#      print('please enter number only')

# x='45'
# if isinstance(x,str):
#       if x.isdigit(): #isdigit() is a string method so we have to give input for x in ''
#          x=int(x)
#          print(x+5)
#       else:
#         print('error::please enter number only')
# else:
#     print(x+20)


# #to print the words that contain capital letters in them
# Z = 'RENU and Raju are FRIENDS'
# uppercase_words = [word for word in Z.split() if word.isupper()]
# print('Words in uppercase are:', uppercase_words)


# name='sneha'
# age=26
# place='banglore'
# D=f'Name: {name},Age:{age},Place: {place}'
# print(D)
# #D=D.format(name,age,place)
# #D='name:{},age:{},palce:{}'.format(name,age,place)

# text='heyansh is a mathematician'
# print(text.replace('mathematician','physician'))

# print(' % '.join(text))

# w='sneha is a programmer'
# print(type(w))
# if isinstance(w,str):
    
#     #if w.isstr():
#         w=str(w)
#         print(w + ' and tester')
#     #else:
#         #90
#         # print('error message')
# else:
#     print('in amazon')

text='we are humans'
print(text)
print(len(text.split()))

# wordcount=0
# for char in text:
#     if char==' ':
#       wordcount=wordcount+1
# print(wordcount+1)

# import sys
# print(sys. version)