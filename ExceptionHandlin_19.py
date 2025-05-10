import os
os.system('cls')
###########################################
##Exception Handling######
#try block lets you test an error
#Except lets you solves the error
#finally block lets you execute the code regardless of the result of the try-except blocks

#######################################################################
x=16               #if given x='16' it will throws an type error
y=8                #if given y=0 it will throws an zero division error

# try:                #one try block can have many except bloCks but repetition of error type is not allowed
#    print(x)
#    print(y)
#    #print(z)  #not declared thats why it throws the error
#    print(x/y)
# except TypeError :
#    try:
#       print(int((x)/y))
#    except ZeroDivisionError as e:
#       print(int(x)/1)
#    except Exception as e:
#       print('Errorrrrrrrrrrrrrrrrr',e)
#       print()
# except ZeroDivisionError as e:
#       print((x)/0)
#       print('error:',e) 
# except Exception as e:
#    print('error:',e)
# else:                 #it runs only if try blocks runs succesfully eith out any errors,else block and finally block should be only 1
#    print("HIIIIIIIIIIIIIIIIIIII")
# finally:
#        print('Byeeeeeeeeeeeeeeee')    #it runs only if try block runs irrespective of whether it is error or not
   
##########################################################################
#RAISING EXCEPTION
x=16 
y=8
z=2
age=5
try:                #one try block can have many except bloCks but repetition of error type is not allowed
   print(x)
   print(y)
   if age < 20:
        raise Exception('not eligible')
   else:
       print('Age:',age)
       print(z)  #not declared thats why it throws the error
       print(x/y)
except TypeError :
   try:
      print(int((x)/y))
   except ZeroDivisionError as e:
      print(int(x)/1)
   except Exception as e:
      print('Errorrrrrrrrrrrrrrrrr',e)
      print()
except ZeroDivisionError as e:
      print((x)/0)
      print('error:',e) 
except Exception as e:
   print('error:',e)
else:                 #it runs only if try blocks runs succesfully eith out any errors,else block and finally block should be only 1
   print("HIIIIIIIIIIIIIIIIIIII")
finally:
       print('Byeeeeeeeeeeeeeeee')    #it runs only if try block runs irrespective of whether it is error or not
   


