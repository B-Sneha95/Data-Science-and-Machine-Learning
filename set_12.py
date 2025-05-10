import os
os.system('cls')

i=0
while i<5:
    print("Hello people")
    print("Have a good day")
    i=i+1

user=['pink','orange','yellow','blue','red','white','black','purple']
i=0
while i<8:
    print(user[i])
    i=i+1
print('\n')
#print(user(9)) #throws error if the index is out of range

user=['pink','orange','yellow','blue','red','white','black','purple']
i=0
while i<len(user):
    print((user[i]))
    i=i+1

user=['pink','orange','yellow','blue','red','white','black','purple'] #accessing
for user1 in range(len(user)):
    print(user1)
    


# user=['pink','orange','yellow','blue','red','white','black','purple'] #iterating
# i=0
# while i<len(user):
#       print(user[i])
#       x =input("Enter an option\n N for Next and B for back : ")
#       if x.upper() =='N':
#         i+=1
#       if x.upper() =='B':
#         i-=1
#####################################################################
#         SET
#unordered,immutable(but not like tuple),we can add or remove from set
##set cannot be accessed through index numbers.if we want we can but after converting in to list or tuple
#we can acess and iterate

users={}
print(type(users))

users={'surya'}
print(type(users))

users={'colour':'red','clas':'first'}
print(type(users))

users=set({})
set={}
print(set)

S={"pen","pencil","eraser","sharpner","Scale","rounder"}
print(S)

print("pen"in S)
S.add('divider')
x=S.pop()
print(x) #random deletion
# S.remove('rounder')
# print(S)
# S.clear()
# print(S)
print('\n')

for i in S:
    print(i)

user1={'A','B','C','D','E'}
user2={'Ant','A','Ball','B','Cat','D','Dog','Egg'}

user1.update(user2) #it will change original set
print(user1)
print('\n')

user3=user1.union(user2) #it will not change original set
print(user3)

print('\n')
user4=user1.intersection(user2)#keep only common elements
print(user4)
print('\n')
user4=user1.symmetric_difference(user2)#keep remaining except repeated elements
print(user4)

