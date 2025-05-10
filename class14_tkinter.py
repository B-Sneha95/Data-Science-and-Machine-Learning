import os
os.system('cls')

user={'Name':'Kishan',
      'age':34,
      'phone':['987986756','87879879','6442627273'],
      'adress':{'h.no':'4-91',
                'city':'Hyd',
                'State':'Telangana',
                'pin':'52354'}}

print(user)

print(user['adress']['city'])
print(user['phone'][1])
print()
print(user['phone'][0],user['phone'][1]) #accesing list inside a dictionary via index value


#iteration
for data in user:
    print(data) #only keys will print
print()
   
for k,v in user.items(): 
    if isinstance(v,list):
         print(f'{k}s :')
         for i,p in enumerate(v,1):
          print(f'  phone{i}:{p}') 
    else:
        if isinstance(v,dict):
           print(f'{k}:')     
           for k1,v1 in v.items():                   #both keys and values will print 
            print(f'   {k1} : {v1}')

        else:
            print(f'{k}:{v}')
    
print("\n")
#Repetition for practice
# for k,v in user.items():
#        if isinstance(v,list):
#             print(f'{k}s:')
#             for i,p in enumerate(v,1):
#                   print(f'    phone{i}:{p}')
#        print(f'{k}:{v}')
# else:
#         if isinstance(v,dict):
#             print(f'{k}:')
#             for k1,v1 in v.items():
#                   print(f'   {k1} : {v1}')
#             else:
#                   print(f'{k}:{v}')

