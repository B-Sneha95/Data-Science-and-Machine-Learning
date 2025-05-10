import os
os.system('cls')
t='''#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#          LISTS
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
#LISTS=> Ordered,Duplicates are allowed,multiple values can be stored,mutable(changeable)
# print(t)
Names=['Arun','Tharun','varun','kiran']
print(Names)
print(type(Names))
print(Names[-1])
print(Names[0])
print(Names[2::])
print(Names[::-1])
print(Names[-1][0])
print(len(Names))
print(Names[::2])
Names[1]='neha'
Names[2]='WHAT'
Names[len(Names):-1]=['Anu','Manu','Thanu']
Names[1:1]=['God']
Names.append('Raja')
Names.remove('Tharun')
print(Names)
Names.insert('Hema',4)
x=['Banu','Renu']
print(x)
Names.extend(x)
Names=['Lathika']
Names.insert(1,4)
print(Names)

A='sonu is a don'
x=list(A)
print(x)

y=A.split()
print(y)

x='Devid'
print(x)
del x
print(x)
print(Names)

# dict={
#     'customer_id': [1, 2, 3],
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'city': ['New York', 'Chicago', 'Los Angeles']
# }

# dict['name'][0]='George'
# print(dict)
# print('\n')
# dict.get('keys')
# print(dict)
# print('\n')
# dict.get('values')
# print(dict)
#######################################################################################
##################################################################################
#eliminating duplicates in a list


text=[1,1,2,2,3,3,4,4,5]
print(text)

unique=[]
for i in text:
    if i not in unique:
      unique.append(i)
print(unique)



text = [1, 1, 2, 2, 3, 3, 4, 4, 5]
unique_text = [x for i, x in enumerate(text) if x not in text[:i]]
print(unique_text)



