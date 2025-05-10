import os
os.system('cls')
###########################
import tkinter
from tkinter import messagebox
text='What is CD?, Computer Disk, Compact Disk, Code Disk, Compact Disk|What is TS?, Telangana State, Tesla Site, Technical Support, Telangana State|What is Python in IT?, Snake, Book, Language, Language|What is RAM?, Phone, Memory, Pen, Memory|What is Mouse?, ComputerDevice, Pet, Computer, ComputerDevice'
data=[q.split(', ')for q in set(text.split('|'))]

home=tkinter.Tk()
home.title('online_test')
home.minsize(600,300)  #shift+alt+down arrow
home.maxsize(600,300)
bg_color='#95f5f7'     #f79595
home.config(bg=bg_color)
index=0
optValue=tkinter.IntVar()
user_selected={}
is_submit='false'

title_lbl=tkinter.Label(home,bg=bg_color,text='Onlinetest',font=('bold',20))
title_lbl.place(x=215,y=5)
status_lbl=tkinter.Label(home,bg=bg_color,text=f'({len(user_selected)}/{len(data)})',font=('bold',15))
status_lbl.place(x=550,y=5)


def user_option():
    x=optValue.get()
    opt=data[index][x]
    result='wrong'
    if data[index][4]==opt:
        result=='correct'
    # print(optValue.get())
    user_selected.update({data[index][0]:[x,opt,result]})
    os.system('cls')

    status_lbl.config(text=f'({len(user_selected)}/{len(data)})')
    if len(data)== len(user_selected):
        # submit_btn.config(state='normal')
        submit_btn.place(x=250,y=220)


qst_lbl=tkinter.Label(home,bg=bg_color,text=f'{index+1}.{data[index][0]}',font=('bold',15))
qst_lbl.place(x=50,y=50)
opt1=tkinter.Radiobutton(home,bg=bg_color,variable=optValue,value=1,command=user_option,text=data[index][1],font=('bold',15))
opt1.place(x=100,y=90)
opt2=tkinter.Radiobutton(home,bg=bg_color,variable=optValue,value=2,command=user_option,text=data[index][2],font=('bold',15))
opt2.place(x=100,y=125)
opt3=tkinter.Radiobutton(home,bg=bg_color,variable=optValue,value=3,command=user_option,text=data[index][3],font=('bold',15))
opt3.place(x=100,y=160)

def next():
    global index
    if index<len(data)-1:
       index+=1
    if index== len(data)-1:
       next_btn.config(state='disabled')
    u_s=user_selected.get(data[index][0],'0')[0]
    
    if is_submit:
        u_result =user_selected.get(data[index][0])[-1]
        if u_result=='correct':
             qst_lbl.config(fg='green')
        else:
            qst_lbl.config(fg='red')
    optValue.set(u_s)
    qst_lbl.config(text=f'{index+1}.{data[index][0]}')
    opt1.config(text=data[index][1])
    opt2.config(text=data[index][2])
    opt3.config(text=data[index][3])
    back_btn.config(state='normal')


def back():
    global index
    if index> 0:
        index-=1
    if index==0:
        back_btn.config(state='disabled')

    u_s=user_selected.get(data[index][0],'0')[0]
    optValue.set(u_s)
    qst_lbl.config(text=f'{index+1}.{data[index][0]}')
    opt1.config(text=data[index][1])
    opt2.config(text=data[index][2])
    opt3.config(text=data[index][3])
    next_btn.config(state='normal')

def submit():
    marks=0
    for m in user_selected.values():
        if m[-1]=='correct':
            marks+=1

    messagebox.showinfo('Result',f"{marks}/{len(user_selected)}")
    global is_submit
    is_submit=True
    submit_btn.config(state='disabled')
    opt1.config(state='disabled')
    opt2.config(state='disabled')
    opt3.config(state='disabled')


next_btn=tkinter.Button(home,text='Next',command=next,font=('bold',15))
next_btn.place(x=450,y=220)

submit_btn=tkinter.Button(home,text='Submit',command=submit,font=('bold',15))
# submit_btn.place_forget()

back_btn=tkinter.Button(home,state='disabled',text='Back',command=back,font=('bold',15))
back_btn.place(x=50,y=220)




home.mainloop()