from tkinter import *

Draw=False
x1=0
y1=0
def callback(event):
    print(event.x,event.y)
    c.create_oval(event.x -5,event.y -5, event.x +5,event.y +5,fill="Green")

def Draw(event):
    print(event.x,event.y)
    c.create_oval(event.x - 5,event.y -5,event.x +5,event.y +5,fill="Black")

def drawRectangle(event):
    global Draw,x1,y1
    if Draw:
        c.create_rectangle(x1,y1,event.x,event.y,fill="Red")
        Draw=False
    else:
        x1=event.x
        y1=event.y
        Draw=True




window=Tk()
c=Canvas(window,width=400,height=400)
c.pack()
c.bind("<Button-1>",callback)
c.bind("<B1-Motion>",Draw)
c.bind("<Button-3>",drawRectangle)

#End of our paint application





window.mainloop()