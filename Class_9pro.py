import os
os.system('cls')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#         PROJECT_SAMPLE
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

text='What is CD?, Computer Disk, Compact Disk, Code Disk, Compact Disk|What is TS?, Telangana State, Tesla Site, Technical Support, Telangana State|What is Python in IT?, Snake, Book, Language, Language|What is RAM?, Phone, Memory, Pen, Memory|What is Mouse?, ComputerDevice, Pet, Computer, ComputerDevice'
# print(text)
# print(type(text))
# print(len(text))
c_no = 0
q_no = 0
print(f'{q_no}.' ,end=" ")
for i in text:
    if i=='|':
        print()
        c_no=0
        q_no+=1
        user_selected=input('select option>')
        os.system('cls')
        print(f'{q_no}.' ,end=" ")
        
    else: 
     if i==",":
        c_no += 1
        print(c_no)
        if c_no == 1:
         print('  A:',end="")
        if c_no==2:
         print('  B:',end="")
        if c_no==3:
          print('  c:',end="")
     else:
        if c_no !=4:
         print(i ,end="") 
  
  
    
     