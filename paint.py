from tkinter import *


def callback(event):
    print(event.x,event.y)


window=Tk()
c=Canvas(window,width=400,height=400)
c.pack()
c.bind("<Button-1>",callback)







window.mainloop()