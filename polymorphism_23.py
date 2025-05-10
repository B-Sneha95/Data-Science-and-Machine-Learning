import os
os.system('cls')
################################
#ACCESS MODIFIERS
#PUBLIC,PRIVATE,PROTECTED

class student:
    def __init__(self,name,rollno,age):
        self.name=name #public member
        self.rollno=rollno #public member
        self.__age=age #private member

    def TC(self):
        print(f'{self.name}, rollno {self.rollno} and age{self.__age} is transfered from hyderabad to nellore')
    
    def get_age(self):
        return self.__age
    
s1=student('Arya','101','12')
#accesing public members
print(s1.name,s1.rollno)
print()
#accessing private members
print(s1.get_age())#we can access the private member by using get()method
print()
print(s1.TC())
print()
#print(s1.__age) #here we will get error because we cannot access a private member directly
                #outside the function
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
logged_user='sneha'
class student:
    def __init__(self,name,rollno,age):
        self.name=name #public member
        self.rollno=rollno #public member
        self.__age=age #private member

    def TC(self):
        print(f'{self.name} with rollno {self.rollno} and age {self.__age} is transfered from hyderabad to nellore')
###GETTER METHOD :TO READ
    def get_age(self):
        if logged_user!='guest':
         return self.__age
        else:
            return('please login')
#SETTER METHOD :TO STORE     
    def set_age(self,age):
        if logged_user!="guest":
            if age> 25:
               self.__age=age
            else:
              print('Not Eligible')
        else:
            print('please login')

    
s1=student('Arya','101','12')
#accesing public members
print(s1.name,s1.rollno)
print()
#accessing private members
print(s1.get_age())#we can access the private member by using get()method
print()
print(s1.TC())
print()
#print(s1.__age) #here we will get error because we cannot access a private member directly
                #outside the function

s1.set_age(30)
print(s1.get_age())

################################################################
#ITER FUNCTION
#iter function is used to iterate the elements 
#we use next funtion to print the iteration

user=['kiran','madhu','sonu','raju','prakash']
print(type(user))
user2=iter(user)
print(type(user2))

print(next(user2))
print(next(user2))
print(next(user2))
print(next(user2))
print(next(user2))
#print(next(user2))
print()
#################################################################
#POLYMORPHISM-many forms
#METHOD OVERRIDING:Functions with same same will override the function 

class Fruits:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

    def info(self,winter):
        self.winter=winter
        print(f'{self.name} is a {self.winter} fruit')
        

class Availablility(Fruits):
    def __init__(self,name,colour,season,budget):
        Fruits.__init__(self,name,colour)
        self.season=season
        self.budget=budget

    def info(self,winter):    #method overriding
        self.winter=winter
        print(f'Fruit - {self.name} is a {self.winter} fruit')

F1=Fruits('Orange','orange_yellow')
A1=Availablility('Orange','orange_yellow','winter','budget_friendly')

print(F1.name,F1.colour)
print()
print(A1.season,A1.budget)
print()
F1.info('winter')
A1.info('low')
print()



























