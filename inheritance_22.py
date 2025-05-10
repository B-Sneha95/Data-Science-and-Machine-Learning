import os
os.system('cls')
# INHERITANCE:Aquiring the properties from part class to a child class 
# it will be applicable only one direction from parent to child
#__init__ is a magic method which does'nt need a function call seperates,it automaticalls calls
#super class is used to inherit the properties from parent to child 
#we can have as many child classes but only one parent class
#self is a keyword which is passed as a parameter in magic method which helps to indicate
#the object when the object is initiated and called

class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand   #proprties=parameter
        self.color=color   #self.brand=brand

    def details(self):
        print(f'Brand={self.brand},Color={self.color}')


class car(Vehicle):
    def __init__(self,brand,color,Wheels,type,version):
        Vehicle.__init__(self,brand,color)
        self.Wheels=Wheels
        self.type=type
        self.version=version
    def displaydetails(self):
        #self.details()
        print(f'Number of wheels: {self.Wheels}, Type: {self.type}, Version: {self.version}')

class bike(Vehicle):
    def __init__(self,brand,color,wheels,rpm,type,has_gears):
        Vehicle.__init__(self,brand,color)
        self.wheels=wheels
        self.rpm=rpm
        self.type=type
        self.hasgears=has_gears

    def displaydetails(self):
        #self.details()
        print(f'Number of wheels: {self.wheels}, RPM: {self.rpm}, Type: {self.type}, Has Gears: {self.hasgears}')

V1=Vehicle('Toyota','Black') #object instantiation
C1=car('Toyota','Black',4,'Automatic','Diesel')
B1=bike('Toyota','Black',2,'100cc','sports','has_gears')
print(V1.brand,V1.color)
print(C1.Wheels,C1.type,C1.version)
print(B1.wheels,B1.rpm,B1.type)
print()
print(C1.displaydetails())
print(B1.displaydetails())




# print(V1.brand, V1.color)
# C1.details()
# B1.details()
print()
################################################################
 #USING SUPER CLASS: SUPER():
 #Super() will call self by itself
print('****USING SUPER CLASS****')
class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand   #proprties=parameter
        self.color=color   #self.brand=brand
    def details(self):
        print(f'Brand={self.brand},Color={self.color}')
class car(Vehicle):
    def __init__(self,brand,color,Wheels,type,version):
        super().__init__(brand,color)
        self.Wheels=Wheels
        self.type=type
        self.version=version
class bike(Vehicle):
    def __init__(self,brand,color,wheels,rpm,type,has_gears):
        super().__init__(brand,color)
        self.wheels=wheels
        self.rpm=rpm
        self.type=type
        self.hasgears=has_gears 
V1=Vehicle('Toyota','Black') #object instantiation
C1=car('Toyota','Black',4,'Automatic','Diesel')
B1=bike('Toyota','Black',2,'100cc','sports','has_gears')
print(V1.brand,V1.color)
print(C1.Wheels,C1.type,C1.version)
print(B1.wheels,B1.rpm,B1.type)

print()

