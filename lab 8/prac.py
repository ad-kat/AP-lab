from tkinter import *
import sys
win=Tk()
win.columnconfigure(0,weight=1)
win.rowconfigure(0,weight=1)
text=Text(win,text="Here is the text area")
text.grid(row=0,column=0,sticky="nesw")
ver_scroll=Scrollbar(win,orient="vertical")
ver_scroll.grid(row=0,column=2, sticky="ns")


b1=Button(win,text="Goodbye",command=sys.exit)
b1.grid(row=0,column=0)

but1=Button(win,text="Hello!!",foreground="#ccd099",background="#e43839")
but1.grid(row=0,column=1)

label=Label(win,text="helloWorld",background="#fff001",foreground="#000ff3",font="Times 20", relief="groove",borderwidth=3)
label.grid(row=1,column=0)
hor_scroll=Scrollbar(win,orient="horizontal")
hor_scroll.grid(row=2,column=0,sticky="ew")

mainloop()

