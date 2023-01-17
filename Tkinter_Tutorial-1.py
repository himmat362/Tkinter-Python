from tkinter import *


window=Tk()
window.geometry('500x500')
#Label(window,text='Hello World!',font='arial 20').pack
#cant use pack and grid in same window
Label(window,text='Hello World!',font='arial 20').grid(row=0,column=0)
Label(window,text='Tinter Tutorial',font='arial 20').grid(row=1,column=0)


window.mainloop()
