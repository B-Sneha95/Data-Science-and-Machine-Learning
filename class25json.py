import os
os.system('cls')

# from datetime import datetime
# x=datetime.now()
# print(x)
# print(x.isoformat())
# print(type(x))
# print(x.date()) #date and time are functions so we have given ()
# print(x.time()) 
# # The below items are the properties of datetime object so we dont give ()
# print(x.day)
# print(x.month)
# print(x.year)
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)
# print('\n')
# print('*****DATE FORMAT*****')
# x=datetime(2024,12,3,4,23,56,456778)
# print(x)
# ####  DATE FORMAT  ##########
# print(x.strftime('%y')) #gives end 2 digits of the year eg:2024,o/p:24
# print(x.strftime('%Y')) #gives 4 digits in a year
# print(x.strftime('%m')) #gives month as a number
# print(x.strftime('%M')) #gives minutes
# print(x.strftime('%d')) #gives day of month
# print(x.strftime('%a')) #gives weekday short version eg:mon
# print(x.strftime('%A')) #gives fullname of weekday
# print(x.strftime('%D')) #gives date in format DD/MM/yy
# print(x.strftime('%B')) #month name full version
# print(x.strftime('%b')) #month name short version eg:jan
# print(x.strftime('%w')) #weekday as a number 0-6,0 is sunday
# print(x.strftime('%d-%B-%Y %H-%M-%S %p'))
# print()
# #############################################################
# ###################       JSON    #################
# print('*****JSON-JAVA SCRIPT OBJECT NOTATION*******')
# #JSON is a standardised format commonly used to transfer data as text that can be sent over a network
# #JSON is a syntax for storing and exchanging data,python has a inbuilt package called json,
# #which can be used to work with JSON data,it is in the form of python dictionary
# #Parse JSON:Convert from JSON to python.If you have a JSON string,you can parse it by using "json.loads()" method
# #Convert from python to JSON:If you have python object ,you can convert it in to a json string by using
# #json.dumps() method
# import json
# user={'name':'Sneha','Age':25,'Phone':'9695969443'}
# print(user)
# print(type(user))
# user=json.dumps(user) #python to json conversion ,o/p:in the form of string
# print(user)
# print(type(user))

# user=json.loads(user) #json to python conversion ,o/p:in the form of dict
# print(user)
# print(type(user))
# print(user['name'])
# print()
# ###############################################################
# ################    RANDOM    ##################
# print('@@@@@@@  RANDOM MODULE  @@@@@@@')
# import random
# import string
# x=random.random() #generates a numbers between 0 and 1
# print(x)
# print(type(x))
# # x=str(x)[1:]
# # print(x)
# x=str(x)[2:12]
# print(x)

# x=random.randint(10000,50000)
# print(x)
# y=[1,2,3,4,5]
# x=random.choice(y)
# print(x)
# print()
# users=['Arun','Sony','Reyansh','Rakul']
# print(set(users))
# print('shuffle')
# print(random.shuffle(users))
# print(users)
# x=random.choice(users)
# print(x)
# x=random.choices(users,k=3)
# print(x)

# print()
# #####CAPTCHA CODE##########
# S=random.choices(string.ascii_letters+string.digits,k=6)
# print(S)
# S=" ".join(S)
# print(S)
# print()

# #############  STRINGS   ##############
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)

#########   PATH LIBRARY   ############
from pathlib import Path
import shutil     #used for copying one file in to another folder with same name
mypath=Path('G:\My Drive\DSML')

# print(mypath.exists())
# print(mypath.name)
# print(mypath.suffix)
# print(mypath.stem)
# print(mypath.parent)

# path2=mypath.with_name('DSML')
# #path2=mypath.with_suffix('.py')
# print(mypath)
# print(path2)
# if mypath.exists():
#     mypath.rename(path2)
# else:
#     print(f'error: {mypath} file not found')

# print(mypath.exists())
# print(mypath.is_dir())
# print(mypath.is_file())

# fc=0 #folder count
# dc=0 #directory_count
# for file in mypath.iterdir():
#     if file.is_file():
#         fc+=1
#     else:
#         dc+=1
#     print(file)

# print(f'\n Total {dc} Folders and {fc} Files found \n')

# # Program for file Searching ###########
# for file in mypath.glob('*.*'):  #*.* means any file name with any extension
#           print(file)                        

# for file in mypath.glob('*.txt'):  #gives txt files
#           print(file)             

# for file in mypath.glob('*.csv'):  #gives csv files
#           print(file)             

# for file in mypath.rglob('*.*'):  #gives all types of files including subdirectories
#           print(file)             

# for file in mypath.glob('*.pbix'):  #gives only powerbi files
#           print(file)             

######## FILE COPY #####################
#we use import.shutil for this  file copy operation

mypath1=Path('G:\\My Drive\\DSML\\data1\\bired.txt')
mypath2=Path('G:\\My Drive\\DSML\\data2\\bired.txt')

shutil.copy(mypath1,mypath2)




















































































