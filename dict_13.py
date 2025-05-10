import os
os.system('cls')
# DICTIONARY:duplicate keys are not allowed but values are allowed,ORDERED,mutable(changeable)  

dict={"Name":"surya","Age":"29","CITY":"HYD"} #Named Index
print(dict)
print(type(dict))

print(dict["CITY"])
print(dict["Age"])
print(dict["Name"])

###########  METHODS ###############
dict["Name"]="SNEHA" #Changing values
print(dict)

dict["State"]="AndhraPradesh"
dict["CITY"]="Nellore"
print(dict)

dict.update({"Age":30,"CITY":"ANANTAPUR"})
dict.update({"Locality":"RamNagar","Name":"Gayathri"})
print(dict)            
print('\n')
#READ
user={"Name":"Saranya","Course":"DSML"}
print(user)    
user['EMAIL']='sara@gmail.com'
user.update({"age":40,"Phone":"9900898907"})
print(user)
print(user.keys())
print(user.values())    
print(user.items())
#print(user.popitem()) #print last item

print('Saranya'in user.values()) # Not recommended 
print(user['Name'] == 'Saranya') #Recommended
print(user.get('Name'))
print('\n')

for x in user.items():
    print(x)

print('\n')   
for key,value in enumerate(user.items(),1):
    print(key,value)
print('\n')
for x in zip(user.items()):
    print(x)
    









            
