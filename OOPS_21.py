import os
os.system('cls')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#class is a factory
#object is a blue print of class which have several properties and methods
#properties are the variables defined with in the class with __init__ constructor with self keyword
#methods are functions that are defined with in the class 
#one should access the variables with the self keyword 

class Car:
    def __init__(self,name,brand,color):  #__init__ is a magic method where it is called by default
        self.name=name
        self.brand=brand
        self.color=color

    def info(self):
        print(f'{self.name} of {self.brand} brand with {self.color} color is moving at 100km per hour')

    def type(self):
        x=input("Does the car have clutch pedal:")
        if x=='yes':
            print(f'{self.name} is Manual type')
        else:
            print(f'{self.name} is Automatic type')
         

#Object instantiaion
C1=Car(name='Hexa',brand='Tata',color='Blue')
C2=Car(name='Nexon',brand='Tata',color='Black')
C3=Car(name='Swift',brand='Suzuki',color='white')


print(C1.name,C1.brand,C1.color)
print(C2.name,C2.brand,C2.color)
print(C3.name,C3.brand,C3.color)

C1.info()
C2.info()
C3.info()

C1.type()
C2.type()
C3.type()