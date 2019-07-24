from tkinter import *

window=Tk()
c=Canvas(window,width=400,height=400)
c.pack()
c.bind("<Button-1>",callback)







window.mainloop()