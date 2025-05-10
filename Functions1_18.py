import os
os.system('cls')

# *args:ARBITRARY ARGUMENTS
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

# Calling the function with multiple arguments
greet("Sneha", "Anhilash", "Samvidh")
print()

#KEYWORD ARGUMENTS
def my_func(child3,child2,child1):
    print('youngest child is:'+ child3)

my_func(child1='Surya',child2='Sonam',child3='Pranith')

# **kwags:ARBITRARY KEYWORD ARGUMENTS,these are in the form of dictionary

def info(**kwags):
    for k,v in kwags.items():
        print(k.title(),":",v)

info(name='sneha',age='26',phone='9596958695')
# RETURN
def add(x,y):
    return x+y #every function must have only one return value

x=add(10,20)
print(x)  #it returns none by default with out giving error 

#LAMBDA FUNCTION
summ=lambda x,y:x+y
# print(type(summ))
print(summ(10,49))

add=lambda a,b:a+b
print(add(20,50))

def addd(a,b):
    return lambda z:a+b+z
addd2=addd(2,4)
print(addd2(3))
print()
#RECURSIVE FUNCTIONS
#it runs 1000 times
x=0
def slno():
    global x
    x+=1
    print(x)
    # slno()

slno()
slno()
slno()
slno()

######     DECORATOR    ##########

def greet():
    print('have a nyc day')

x=greet #assigning a function in a variable
x()

#decorator 
def Hi():
    print('Good Morning')

def person(func): 
    func()
    print('kiran')

person(Hi) #we have passed a function as an argument inside another function
print()
##########################################
def Hi():
    return 'Good Morning'

def person(func): 
    x=func()
    def abc():
        return " kiran"
    return x ,abc

y,fun=person(Hi) 
print(y+fun())

#########################################

def decor(func):
    def inner(*args,**kwags):
        print('************************')
        x=func(*args,**kwags)
        print('**************************')
    return inner
def decor2(func):
    def inner(*args,**kwags):
        print('************************')
        x=func(*args,**kwags)
        print('**************************')
    return inner


user='guest'
def login_required(func):
    def inner(*args,**kwags):
        if user!='guest':
            func(*args,**kwags)
        else:
          print('please login:')
    return inner

@decor
@login_required
@decor2

def Hi():
    print('good morning')

Hi()




























    