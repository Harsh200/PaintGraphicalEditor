from tkinter import *


def callback(event):
    print(event.x,event.y)
    c.create_oval(event.x -5,event.y -5, event.x +5,event.y +5,fill="Green")


window=Tk()
c=Canvas(window,width=400,height=400)
c.pack()
c.bind("<Button-1>",callback)
c.bind("<B1-Motion>",draw)






window.mainloop()