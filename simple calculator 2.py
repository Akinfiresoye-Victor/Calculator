from atexit import _clear#it is used to clear what is in the register
from  tkinter import *
root=Tk()#the basics before any gui beiing created
root.title('victors calculator')#used to change the title of the gui application
e=Entry(root,width=35,borderwidth=6)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def add_button(number):
    #e.delete ia used to delete what is in the box
    #e.get is used to retrieve the value from the button
    current=e.get()
    e.delete(0,END)#Deleting from index 0
    e.insert(0,str(current) + str(number))#to insert what ever the number is in the button   
def button_clear():
        e.delete(0,END)
def addition_button():
    first_num=e.get()
    global f_num 
    global math
    math='addition'       
    f_num=int(first_num)
    e.delete(0,END)
        
def button_equal():
    second_num=e.get()
    e.delete(0, END)
    if math=='addition':
        e.insert(0, f_num+int(second_num))
    if math=='subtraction':
        e.insert(0, f_num-int(second_num))
    if math=='multiplication':
        e.insert(0, f_num*int(second_num))
    if math=='division':
        e.insert(0, f_num/int(second_num))    
        
def but_subtract():
    first_num=e.get()
    global f_num 
    global math
    math='subtraction'       
    f_num=int(first_num)
    e.delete(0,END)  

def but_multiply():
    first_num=e.get()
    global f_num 
    global math
    math='multiplication'       
    f_num=int(first_num)
    e.delete(0,END)  

def but_divide():
    first_num=e.get()
    global f_num 
    global math
    math='division'       
    f_num=int(first_num)
    e.delete(0,END)  
    
    
    
    
    
    
    
    
#define buttons,any func can be used
but_1=Button(root,text='1',padx=40,pady=20,command=lambda: add_button(1))
but_2=Button(root,text='2',padx=40,pady=20,command=lambda: add_button(2))
but_3=Button(root,text='3',padx=40,pady=20,command=lambda: add_button(3))
but_4=Button(root,text='4',padx=40,pady=20,command=lambda: add_button(4))
but_5=Button(root,text='5',padx=40,pady=20,command=lambda: add_button(5))
but_6=Button(root,text='6',padx=40,pady=20,command=lambda: add_button(6))
but_7=Button(root,text='7',padx=40,pady=20,command=lambda: add_button(7))
but_8=Button(root,text='8',padx=40,pady=20,command=lambda: add_button(8))
but_9=Button(root,text='9',padx=40,pady=20,command=lambda: add_button(9))
but_0=Button(root,text='0',padx=40,pady=20,command=lambda: add_button(0))
but_add=Button(root,text='+',padx=39,pady=20,command=addition_button)
but_equal=Button(root,text='=',padx=90,pady=20,command=button_equal)
but_clear=Button(root,text='c',padx=79,pady=20,command=button_clear)

but_subtract=Button(root,text='-',padx=45,pady=20,command=but_subtract)
but_multiply=Button(root,text='*',padx=44,pady=20,command=but_multiply)
but_divide=Button(root,text='/',padx=45,pady=20,command=but_divide)

#to put button on screen and arrange it using grid
but_1.grid(row=3,column=0)
but_2.grid(row=3,column=1)
but_3.grid(row=3,column=2)

but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)

but_7.grid(row=1,column=0)
but_8.grid(row=1,column=1)
but_9.grid(row=1,column=2)

but_0.grid(row=4,column=0)
but_clear.grid(row=4,column=1,columnspan=2)
but_add.grid(row=5,column=0)
but_equal.grid(row=5,column=1,columnspan=2)

but_subtract.grid(row=6, column=0)
but_multiply.grid(row=6, column=1)
but_divide.grid(row=6, column=2)




root.mainloop()
