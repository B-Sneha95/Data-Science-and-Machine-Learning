import os
os.system('cls')
#######################################
#IF,ELIF,ELSE
#######################################
time=5
gender='Male'
if time<10:
 print('Good Morning',end=" ")
elif time<12:
 print('Good Afternoon',end=" ")
elif time<20:
 print('good evening',end=" ")
else:
 print('good night')


if gender == "Male":
   print('sir')
elif gender== "Female":
   print('madam')
else:
  print()

#if with in if
time=5
gender='female'
if time<3:
  if gender=='female':
   print("good morning madam")
  else:
    print('good morning sir') 
print('good morning')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$
print()
time=5
gender='female'
if time<3:
  if gender=='female':
   print("good morning madam")
  elif gender=='male':
    print('good morning sir') 
  else:
    print('good morning')



###############################
# Short hand if
##############################
print()

if time:print('yes') 

print('yes')if time else print('no')


x=10 if time else 20
print(x)