from tkinter import *
from tkinter import colorchooser



root = Tk()


material="lapis"
col="black"

ancho_linia=Scale(root,from_=0,to=100,orient=HORIZONTAL)
ancho_linia.grid(row=2,column=10,columnspan=8)
ancho_linias=Scale(root,from_=1,to=30,orient=HORIZONTAL)
ancho_linias.grid(row=6,column=10,columnspan=8)
lienzo=Canvas(root,width=600,height=400,bg="white")
lienzo.grid(padx=20,pady=20,row=1,columnspan=10,column=0,rowspan=10)
boton_borador=Button(root,text="borrador",command=lambda:set_material("goma"))
boton_borador.grid(row=1,column=10,columnspan=4)
boton_lapis=Button(root,text="lapis",command=lambda:set_material("lapis"))
boton_lapis.grid(row=1,column=14,columnspan=2)
boton_linia=Button(root,text="linea",command=lambda:set_material("linea"))
boton_linia.grid(row=1,column=16,columnspan=2)
boton_rectangulo=Button(root,text="rectangulo",command=lambda:set_material("rect"))
boton_rectangulo.grid(row=1,column=18,columnspan=4)
boton_eliminacion=Button(root,text="bora todo",command=lambda:des()).grid(row=1,column=22,columnspan=4)
boton_FF6A00=Button(root,bg="#FF6A00",command=lambda:set_color("#FF6A00"),height=1,width=1).grid(row=3,column=10)
boton_black=Button(root,bg="black",command=lambda:set_color("black"),height=1,width=1).grid(row=3,column=11)
boton_F0F0F0=Button(root,bg="#F0F0F0",command=lambda:set_color("#F0F0F0"),height=1,width=1).grid(row=3,column=12)
boton_color=Button(root,bg="#F0F0F0",command=lambda:asck_color(),height=1,width=1)
boton_color.grid(row=4,column=12)
def asck_color():
    c2=colorchooser.askcolor()[1]
    print(c2)
    set_color(c2)
    boton_color.config(bg=c2)
def set_color(c):
  global col
  col=c
  boton_color.config(bg=c)
cord=[]
def des():
  lienzo.delete("all")
def set_material(m):
  global material
  material=m
  if material=="lapis":
    lienzo.bind('<Button-1>', motion2)
    lienzo.bind('<B1-Motion>', motion2)
    las.config(bg="red")
    bor.config(bg="#F0F0F0")
    lin.config(bg="#F0F0F0")
    rect.config(bg="#F0F0F0")
  elif material=="goma":
    lienzo.bind('<Button-1>', motion)
    lienzo.bind('<B1-Motion>', motion)
    bor.config(bg="red")
    las.config(bg="#F0F0F0")
    lin.config(bg="#F0F0F0")
    rect.config(bg="#F0F0F0")
  elif material=="linea":
    lienzo.bind('<Button-1>',linea)
    bor.config(bg="#F0F0F0")
    las.config(bg="#F0F0F0")
    lin.config(bg="red")
    rect.config(bg="#F0F0F0")
  elif material=="rect":
    lienzo.bind('<Button-1>',recta)
    bor.config(bg="#F0F0F0")
    las.config(bg="#F0F0F0")
    lin.config(bg="#F0F0F0")
    rect.config(bg="red")

def motion2(event):
  x, y = event.x, event.y
  lienzo.create_rectangle(x-hancho.get(),y+hancho.get(),x+hancho.get(),y-hancho.get(),fill=col,outline=col,tags=col)
def motion(event):
  x, y = event.x, event.y
  lienzo.create_rectangle(x-hancho.get(),y+hancho.get(),x+hancho.get(),y-hancho.get(),fill="white",outline="white",tags=col)

def linea(event):
    x,y=event.x,event.y
    cord.append(x)
    cord.append(y)
    if len(cord)==4 or len(cord)>4:
        lienzo.create_line(cord[0],cord[1],cord[2],cord[3],fill=col,tags=col,width=hancho.get()*2,)
        cord.clear()
def recta(event):
    x,y=event.x,event.y
    cord.append(x)
    cord.append(y)
    if len(cord)==4 or len(cord)>4:
        lienzo.create_rectangle(cord[0],cord[1],cord[2],cord[3],outline=col,width=hancho.get()*2,tags=col)
        cord.clear()
def spray (event):
    x,y=event.x,event.y
    dis=(hancho.get()*2)+dis_linias.get()
    lienzo.create_rectangle(x-hancho.get(),y+hancho.get(),x+hancho.get(),y-hancho.get(),fill=col,outline=col,tags=col)
    lienzo.create_rectangle(x-hancho.get()+dis,y+hancho.get()-dis,x+hancho.get()+dis,y-hancho.get()-dis,fill=col,outline=col,tags=col)
def getcolor(event):
    for item_id in lienzo.find_all():
      tag = lienzo.gettags(item_id)[0]
      lienzo.tag_bind(tag, '<Button-2>', lambda _, ta=tag: set_color(ta))
     
lienzo.bind('<Button-2>',getcolor)
lienzo.bind("<B3-Motion>",spray)
root.mainloop()

