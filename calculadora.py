from tkinter import *

ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")
ventana.config(bg="darkblue")










b7=Button(ventana, text="7")
b7.grid(row=0, column=0, padx=12,pady=25)

b8=Button(ventana, text="8")
b8.grid(row=0, column=1, padx=12,pady=25)

b9=Button(ventana, text="9")
b9.grid(row=0, column=2, padx=12,pady=25)


b4=Button(ventana, text="4")
b4.grid(row=1, column=0, padx=12,pady=25)

b5=Button(ventana, text="5")
b5.grid(row=1, column=1, padx=12,pady=25)

b6=Button(ventana, text="6")
b6.grid(row=1, column=2, padx=12,pady=25)


b1=Button(ventana, text="1")
b1.grid(row=2, column=0, padx=12,pady=25)

b2=Button(ventana, text="2")
b2.grid(row=2, column=1, padx=12,pady=25)

b3=Button(ventana, text="3")
b3.grid(row=2, column=2, padx=12,pady=25)


b0=Button(ventana, text="0")
b0.grid(row=3, column=1, padx=12,pady=25)






bdiv=Button(ventana, text="÷")
bdiv.grid(row=0, column=4, padx=12,pady=25)

bmult=Button(ventana, text="x")
bmult.grid(row=1, column=4, padx=12,pady=25)

bresta=Button(ventana, text="-")
bresta.grid(row=2, column=4, padx=12,pady=25)

bsuma=Button(ventana, text="+")
bsuma.grid(row=3, column=4, padx=12,pady=25)


bres=Button(ventana,text="=")
bres.grid(row=3, column=4, padx=12,pady=25)



ventana.mainloop()


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b






