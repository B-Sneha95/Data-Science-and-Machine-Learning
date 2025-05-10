import os
os.system('cls')
#@@@@@@@@@@@@@@@@@@@@@@@@@

import tkinter

home_win=tkinter.Tk()
home_win.minsize(340,375)
home_win.maxsize(340,375)
home_win.title('Calaculator')
home_win.config(bg='#cccccc')
screen='0'
screen_lbl=tkinter.Label(home_win,width=17,text="0",bg='skyblue',pady=6,padx=3,font=('bold',22),anchor='w')
screen_lbl.place(x=20,y=20)

def btn_7():
    global screen
    if screen== '0':
       screen = '7'
    else:
        screen+='7'
    screen_lbl.config(text=screen)    

def btn_8():
    global screen
    if screen== '0':
       screen = '8'
    else:
        screen+='8'
    screen_lbl.config(text=screen)

def btn_9():
    global screen
    if screen== '0':
       screen = '9'
    else:
        screen+='9'
    screen_lbl.config(text=screen)

def btn_4():
    global screen
    if screen== '0':
       screen = '4'
    else:
        screen+='4'
    screen_lbl.config(text=screen)

def btn_5():
    global screen
    if screen== '0':
       screen = '5'
    else:
        screen+='5'
    screen_lbl.config(text=screen)

def btn_6():
    global screen
    if screen== '0':
       screen = '6'
    else:
        screen+='6'
    screen_lbl.config(text=screen)

def btn_0():
    global screen
    if screen== '0':
       screen = '0'
    else:
        screen+='0'
    screen_lbl.config(text=screen)

def btn_dot():
    global screen
    if screen[-1]!= '.':
       screen+= '.'
    screen_lbl.config(text=screen)

def btn_1():
    global screen
    if screen== '0':
       screen = '1'
    else:
        screen+='1'
    screen_lbl.config(text=screen)

def btn_2():
    global screen
    if screen== '0':
       screen = '2'
    else:
        screen+='2'
    screen_lbl.config(text=screen)

def btn_3():
    global screen
    if screen== '0':
       screen = '3'
    else:
        screen+='3'
    screen_lbl.config(text=screen)

def btnc():
    global screen
    if screen== '0':
      screen_lbl.config(text=screen)   

def btnB():
    global screen
    if len(screen)==1:
        screen='0'
    else:
        screen=screen[:-1]
        screen_lbl.config(text=screen)
def btnAdd():
    global screen
    if screen[-1].isdigit():
        screen+='+'
        screen_lbl.config(text=screen)

def btnS():
    global screen
    if screen[-1].isdigit():
        screen+='-'
        screen_lbl.config(text=screen)

def btn_D():
    global screen
    if screen[-1].isdigit():
        screen+='/'
        screen_lbl.config(text=screen)

def btnM():
    global screen
    if screen[-1].isdigit():
        screen+='*'
        screen_lbl.config(text=screen)

def btnC():
    global screen
    if screen =='0':
        screen_lbl.config(text=screen)

def btnB():
    global screen
    if len(screen) == 1:
        screen='0'
    else:
        screen=screen[:-1]
        screen_lbl.config(text=screen)

def btnEqual():
    global screen
    if screen[-1].isdigit():
        screen=str(eval(screen))
        screen_lbl.config(text=screen)


btn_c=tkinter.Button(home_win,width="4",text="c",command=btnC,font=('bold',20))
btn_c.place(x=20,y=73)
btn_back=tkinter.Button(home_win,width="8",text="back",padx=6,command=btnB,font=('bold',20))
btn_back.place(x=95,y=73)
btn_m=tkinter.Button(home_win,width="4",text="*",command=btnM,font=('bold',20))
btn_m.place(x=245,y=73)


btn7=tkinter.Button(home_win,width="4",text="7",command=btn_7 ,font=('bold',20))
btn7.place(x=20,y=130)
btn8=tkinter.Button(home_win,width="4",text="8",command=btn_8,font=('bold',20))
btn8.place(x=95,y=130)
btn9=tkinter.Button(home_win,width="4",text="9",command=btn_9,font=('bold',20))
btn9.place(x=170,y=130)
btn_D=tkinter.Button(home_win,width="4",text="/",command=btn_D,font=('bold',20))
btn_D.place(x=245,y=130)


btn4=tkinter.Button(home_win,width="4",text="4",command=btn_4 ,font=('bold',20))
btn4.place(x=20,y=187)
btn5=tkinter.Button(home_win,width="4",text="5",command=btn_5 ,font=('bold',20))
btn5.place(x=95,y=187)
btn6=tkinter.Button(home_win,width="4",text="6",command=btn_6,font=('bold',20))
btn6.place(x=170,y=187)
btn_s=tkinter.Button(home_win,width="4",text="-",command=btnS,font=('bold',20))
btn_s.place(x=245,y=187)

btn1=tkinter.Button(home_win,width="4",text="1",command=btn_1,font=('bold',20))
btn1.place(x=20,y=244)
btn2=tkinter.Button(home_win,width="4",text="2",command=btn_2,font=('bold',20))
btn2.place(x=95,y=244)
btn3=tkinter.Button(home_win,width="4",text="3",command=btn_3,font=('bold',20))
btn3.place(x=170,y=244)
btn_a=tkinter.Button(home_win,width="4",text="+",command=btnAdd,font=('bold',20))
btn_a.place(x=245,y=244)

btn0=tkinter.Button(home_win,width="4",text="0",command=btn_0,font=('bold',20))
btn0.place(x=20,y=301)
btn_dot=tkinter.Button(home_win,width="4",text=".",padx=7,command=btn_dot,font=('bold',20))
btn_dot.place(x=95,y=301)
btn_e=tkinter.Button(home_win,width="8",padx=7,text="=",command=btnEqual,font=('bold',20))
btn_e.place(x=170,y=301)


home_win.mainloop()

































# text=["SNEHA",'ABHILASH','SAMVIDH']
# def myfun(value):
#     return value.lower()

# x=map(myfun,text)
# print(list(x))

# text1=['cat','rat','bat','mat','on','in','no']
# def countfun(value):
#         if len(text1)>2:
#             return value
# y=filter(countfun,text1)
# print(list(y))

# text2=['sachin','sehwag','Dhoni','Dravid','kohli']
# def myfunc1(value):
#       if len(value)>=3:#value is a special variable that acts as a pipe for a container to store a value
#         return value

# y=filter(myfunc1,text2)
# print(list(y))
# if we use map in case of filter it will return 'NONE' in the output incase of which it fails in doing filtering

