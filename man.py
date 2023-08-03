from tkinter import *
import pyshorteners
from PIL import ImageTk,Image

app=Tk()
app.title("URL Short")
app.resizable(False,False)

img = Image.open("img/img.jpg")
bg=ImageTk.PhotoImage(img)

app.geometry("700x300")
def test():
    url=e1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry_fild2.insert(END,s)
    print(s)
label = Label(app,image=bg).place(x = 0,y = 0)

Label(app,text="Enter Your Url Link",font="impack 24 bold",bg="black",fg="#7FFF00").pack(fill="x")
e1 = Entry(app,font="18", width=40,bg="black",fg="#7FFF00")
e1.pack(pady=30)

Button(app,text="Click Me",font="impack 12 bold",bg="black",fg="#7FFF00",width=14,command=test).place(x=270 , y=150)
entry_fild2=Entry(app,font="impack 16 bold",bg="black",width=40,bd=0,fg="#7FFF00")
entry_fild2.place(x=150,y=200)


app.mainloop()