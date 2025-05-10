import os
os.system('cls')
#@@@@@@@@@ FUNCTIONS @@@@@@@@@@@@@@@@@@@
#Function is a block of code which runs only when it is called
# "def"-command used to create a function,user should give a name to def
# if we want to pass the funtion as parameter or as a reference then we dont need to put paranthesis after function name

def fun1():
    name='kiran'
    print(f'hi good morning,{name}')
fun1()


def wish(time,gender): #time and gender are positional parameters,used to pass data as variables
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
        print('')

wish(10,'Male')
wish(15,'Female')
wish(19,'Male')

print()

def sum():
    print(200+300)
def add(a,b,c):
    print(a+b+c)
sum()
add(10,20,30)
#################################
# PARAMETERS,ARGUMENTS
#PARAMETERS:USED TO PASS DATA IN TO FUNCTION WHILE CREATING THE FUNCTION eg:def add(a,b):,a,b are parameters
#ARGUMENTS:USED WHILE CALLING THE FUNCTION ,eg:add(10,50),10,50 are arguments
# *a- ARBITRARY ARGUMENTS, **a- KEYWORD ARGUMENTS

# ARGS:ARBITRARY ARGUMENTS
def summ(*a):
    print(a)

summ(10,20,30,40,50,80)
summ()
summ(10)
summ(0)
print()

def addd(*args):
    result=0
    for i in args:
        if isinstance(i,int): #checking if the argument is int or not
          result+=i
        elif isinstance(i,str): #checking if the argument is string
              if i.isdigit(): #converting str to int 
                 result+=int(i)
              else:
                  print(i,':pass only numbers')
                 
    print(result)
addd(10,20)   
addd(20,30,'apple') #it ignores apple bcoz we have given isinstance(i,int),so it takes only int parameters
addd(10,10,30,'40')
addd(1,2,3,'dd4')
addd('rjdfjk')
# x=[10,20,30]
# print(sum(x)) #throws an error because sum is a builtin function where as addd is userdefined function
# we cannot use built in functions and keywords as a name of userdefined function,while giving a name to function,
# name which is given next to def should not be a keyword,builtin function names.


