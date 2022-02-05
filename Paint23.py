from email.mime import image
from tkinter import Button,PhotoImage,Scale,colorchooser,Canvas,Tk,HORIZONTAL,messagebox,filedialog

raiz=Tk()

col="black"

lienzo=Canvas(raiz,bg="white",height=600,width=600)
lienzo.grid(row=1,column=1,rowspan=10,columnspan=10,padx=20,pady=20)

def info():
    messagebox.showinfo('no implementado','la eramienta no esta implementada')
def getcolor(event):
    print(event.x,event.y)
lienzo.bind('<Button-2>',getcolor)
cord=[]


raiz.mainloop()