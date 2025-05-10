import os
os.system('cls')
###########################
import tkinter
text='What is CD?, Computer Disk, Compact Disk, Code Disk, Compact Disk|What is TS?, Telangana State, Tesla Site, Technical Support, Telangana State|What is Python in IT?, Snake, Book, Language, Language|What is RAM?, Phone, Memory, Pen, Memory|What is Mouse?, ComputerDevice, Pet, Computer, ComputerDevice'
data=[q.split(', ')for q in set(text.split('|'))]

home=tkinter.Tk()
home.title('online_test')
home.minsize(600,300)  #shift+alt+down arrow
home.maxsize(600,300)
home.config(bg='#cccccc')
index=0

title_lbl=tkinter.Label(home,text='Onlinetest',font=('bold',20))
title_lbl.place(x=215,y=5)

qst_lbl=tkinter.Label(home,text=f'{index+1}.{data[index][0]}',font=('bold',15))
qst_lbl.place(x=50,y=50)

def next():
    global index
    index+=1
    print(index)
    qst_lbl.config(text=f'{index+1}.{data[index][0]}')

def back():
    global index
    index-=1
    print(index)
    qst_lbl.config(text=f'{index+1}.{data[index][0]}')

next_btn=tkinter.Button(home,text='next',command=next,font=('bold',15))
next_btn.place(x=450,y=200)

back_btn=tkinter.Button(home,text='back',command=back,font=('bold',15))
back_btn.place(x=50,y=200)





home.mainloop()