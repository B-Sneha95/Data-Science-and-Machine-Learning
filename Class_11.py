import os
os.system('cls')
#**************************
F= ['kiwi','apple','banana','Orange']
print(F)

F.sort() #sort based on ASCII values not alphabetical order
print(F)
F.sort(reverse=True)
print(F)

F=sorted(F,reverse=True)
F=sorted(F)
print(F[::-1]) #temporary reverse
F.reverse() #reveres the original

text1= ['kiwi','apple','banana','Orange','raspberry','strawberry']
print(text1)
text2=[]
for i in text1:
    if len(i)==4:
        text2.append(i)
print(text2)
# #or
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# #list comprehension
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
text3=[i for i in text1 if len(i)==4]
print(text3)

text1= ['kiwi','apple','banana','Orange','raspberry','strawberry']
upper=[i.upper() if 'a' in i else i for i in text1]
print(upper)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#LIST CONSTRUCTOR
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
S=list('ABHAYA')
print(S)

y=range(10)
print(y)

x=list(y)
print(x)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#         RANGE
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#range starts from 0,stop value is exclusive,step value will be default 1
#start stop step (position, number, stepvalue)
D=range(2,100,2)
A=list(D)
print(A)

#example:
for i in range(10):
    if i%2==0:
     print(i)

text2=['sachin','sehwag','Dhoni','Dravid','kohli']
x=map(str.upper,text2)
print(list(x))
print('\n')
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                  MAP
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#if we want to use map function we should have a function first, map compulsily expect a return
#Map is used for calling built in functions like upper,lower etc
text2=['sachin','sehwag','Dhoni','Dravid','kohli']
def myfunc(value): #value is a special variable that acts as a pipe for a container to store a value
   return value.upper()

x=map(myfunc,text2)
print(list(x))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#                  FILTER
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#filter is used for filtering data one by one in a list
text2=['sachin','sehwag','Dhoni','Dravid','kohli']
def myfunc1(value):
      if len(value)>=3:#value is a special variable that acts as a pipe for a container to store a value
        return value

y=filter(myfunc1,text2)
print(list(y))
#if we use map in case of filter it will return 'NONE' in the output incase of which it fails in doing filtering


# enumerate()
text=['Hello world']
for index, char in enumerate(text):
 print(f'index:{index}and char:{char}')

#Zip()
text1="Hello"
text2="World"
for char1,char2 in zip(text1,text2):
    print(f'char1:{char1} char2:{char2}')

# #reversed()
text = "Hello, World!"
for char in reversed(text):
 print(f'reversed text:{char}')   

#iter()
text="i am a humanbeing" 
for char in iter(text):
    print(f'iteraton:{char}')







































#reversed
# F1=[]
# for f in F:
#     if len(f)==4:
#         F1.append(f)

# print(f)






# F.reverse()
# print(F[::-1])

# F.sort()
# F=sorted(F)
# print(F)
