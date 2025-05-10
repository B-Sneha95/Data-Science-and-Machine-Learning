import os
os.system('cls')
###################################

myfam={"child1":{'name':'Ramu','year':'2014'},"child2":{'name':'tulasi','year':'2007'},"child3":{'name':'laxmi','year':'2011'}}
print(myfam)
print('\n')

for k,v in myfam.items():
    if isinstance(v,dict):
        print(f'{(k)}:')
        for k1,v1 in v.items():
            print(f'  {k1}:{v1}')


#create 3 dictionaries,then create 1 dictionary that will contain the other three dictionaries

child1={"name":"ramu","year":2024}
child2={"name":"tulasi","year":2007}
child3={"name":"laxmi","year":2011}
# oputput should be:myfam={"child1":'child1',
#                          "child2":'child2',
#                           "child3":'child3'}


myfam1={"child1":child1,"child2":child2, "child3":child3}
 
myfam={}
for key in myfam1:
    myfam[key]=key
print(myfam)

















# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# user={'Name':'Kishan',
#       'age':34,
#       'phone':['987986756','87879879','6442627273'],
#       'adress':{'h.no':'4-91',
#                 'city':'Hyd',
#                 'State':'Telangana',
#                 'pin':'52354'}}

# user1=list(user.values())
# user1=list(user.keys())
# print(user1)

