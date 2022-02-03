from tkinter import Button,PhotoImage,Scale,colorchooser,Canvas,Tk,HORIZONTAL

raiz=Tk()

col="black"
rectangulo = PhotoImage(file="_rectangulo.png")
goma = PhotoImage(file="goma.png")
lapis = PhotoImage(file="lapis.png")
linia = PhotoImage(file="linia.png")
hancho=Scale(raiz,from_=0,to=100,orient=HORIZONTAL)
hancho.grid(row=4,column=11,columnspan=4) 
lienzo=Canvas(raiz,bg="white",height=600,width=600)
lienzo.grid(row=1,column=1,rowspan=10,columnspan=10,padx=20,pady=20)
goma_boton=Button(raiz,image=goma,command=lambda:main(goma_boton,"goma"))
goma_boton.grid(row=3,column=11)
rectangulo_boton=Button(raiz,image=rectangulo,command=lambda:main(rectangulo_boton,"rectangulo"))
rectangulo_boton.grid(row=3,column=12)
lapis_boton=Button(raiz,image=lapis,command=lambda:main(lapis_boton,"lapis"))
lapis_boton.grid(row=3,column=13)
linia_boton=Button(raiz,image=linia,command=lambda:main(linia_boton,"linia"))
linia_boton.grid(row=3,column=14)

botones_lista=[goma_boton,rectangulo_boton,lapis_boton,linia_boton]

def main(boton_selecionado,material):
    for i in botones_lista:
        if i==boton_selecionado:
            i.config(bg="red")
        else:
            i.config(bg="#F0F0F0")
    if material=="lapis":
        lienzo.bind('<Button-1>', motion2)
        lienzo.bind('<B1-Motion>', motion2)
    elif material=="goma":
        lienzo.bind('<Button-1>', motion)
        lienzo.bind('<B1-Motion>', motion)
    elif material=="linea":
        lienzo.bind('<Button-1>',linea)
    elif material=="rectangulo":
        lienzo.bind('<Button-1>',recta)
cord=[]
def motion2(event):
  x, y = event.x, event.y
  lienzo.create_rectangle(x-hancho.get(),y+hancho.get(),x+hancho.get(),y-hancho.get(),fill=col,outline=col,tags="kk")
def motion(event):
  x, y = event.x, event.y
  lienzo.create_rectangle(x-hancho.get(),y+hancho.get(),x+hancho.get(),y-hancho.get(),fill="white",outline="white")

def linea(event):
    x,y=event.x,event.y
    cord.append(x)
    cord.append(y)
    if len(cord)==4 or len(cord)>4:
        lienzo.create_line(cord[0],cord[1],cord[2],cord[3],fill=col,tags="kk",width=hancho.get()*2,)
        cord.clear()
def recta(event):
    x,y=event.x,event.y
    cord.append(x)
    cord.append(y)
    if len(cord)==4 or len(cord)>4:
        lienzo.create_rectangle(cord[0],cord[1],cord[2],cord[3],outline=col,width=hancho.get()*2,tags="kk")
        cord.clear()



raiz.mainloop()