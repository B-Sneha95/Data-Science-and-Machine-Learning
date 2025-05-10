import os
os.system('cls')

#$$$$$$$$$$$$$$$$$$
#    Strings
#$$$$$$$$$$$$$$$$$$
# text='python'
# print(text)
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])

# print('\n')

# #reverse index
# print(text[-1])
# print(text[-2])
# print(text[-3])
# print(text[-4])
# print(text[-5])
# print(text[-6])
# print('\n')
# #$$$$$$$$$$$$$$$$$$
# # String functions
# #$$$$$$$$$$$$$$$$$$
# #length
# print(len(text))
# T1="python is a language"
# print(T1)
# print('\n')
# print(T1[::]) 
# print('\n')
# print(T1[0:])
# print('\n')
# print(T1[:-1])
# print('\n')
# print(T1[::1])
# print('\n')
# print(T1[::-1])
# print('\n')
# print(T1[2::])

# print()
# for char in T1:
#     print(char)
#     #print(char,end='\n')
#     # print(char,end=" ")

# #to print how many spaces and words are there in the given string
# word_count=0
# for char in T1:
#     if(char==' '):
#       print('yes')
#       word_count=word_count+1
# print('Total words:',word_count+1)

# print('\n')
# #Methods
# text1='work is worship'
# print(text1.upper())
# print(text1.lower())
# print(text1.capitalize())
# print(text1.title())
# print(text1.split())
# print(text1.count(''))
# print(text1.count('')+1)

# print('\n')
# text3=['work', 'is', 'worship']
# print('work' in text3)

# S='zara is from grade one'
# count=0
# for char in S:
#     if char=='r':
#      count=count+1
    
# print('words that contain char r:',count)

# T='sonu and monu are twins'
# count=1
# for char in T:
#     if char==' ':
#         count=count+1
# print('No of words in T are:',count)

# Z='RENU and Raju are FRIENDS'
# count=0
# for char in Z:
#     if char.isupper():
#         count=count+1

# print('no:of words with capital letters in Z are:',count)

# Z='RENU and Raju are FRIENDS'
# count=0
# for word in Z.split():
#     if word[0].isupper():
#         count=count+1

# print('words with capital letters in Z are:',count)



S="I am a software engineer"
for word in S.split():
    print(word)

C="I am so lucky that i have got a new job"
count=1
for char in C:
    if char==' ':
        count=count+1

print(f'No:of words in the String c are:{count}')

for word in C.capitalize():
    print (word)

for word in C.title():
    print (word)

print(list(C))
















