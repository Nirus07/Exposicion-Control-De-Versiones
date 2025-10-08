import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("356x568")
ventana.config(bg="#231673")

texto_Numerico = tk.StringVar()
numeros = ""


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b


etiqueta = tk.Label(ventana,
                    textvariable=texto_Numerico,
                    font=("Arial",14), justify="right",
                    bg="black", width= 31, height=6, anchor="ne", fg="white")
etiqueta.grid(row=1, column=1, columnspan=4, padx=0)


boton0 = tk.Button(ventana, text="0",
                   command=lambda: mostrar_boton("0"),
                   width=24,height=5, bg="cyan",)
boton1 = tk.Button(ventana, text="1",
                   command=lambda: mostrar_boton("1"),
                   width=11,height=5, bg="cyan", )
boton2 = tk.Button(ventana, text="2",
                   command=lambda: mostrar_boton("2"),
                   width=11,height=5, bg="cyan", )
boton3 = tk.Button(ventana, text="3",
                   command=lambda: mostrar_boton("3"),
                   width=11,height=5, bg="cyan", )
boton4 = tk.Button(ventana, text="4",
                   command=lambda: mostrar_boton("4"),
                   width=11,height=5, bg="cyan", )
boton5 = tk.Button(ventana, text="5",
                   command=lambda: mostrar_boton("5"),
                   width=11,height=5, bg="cyan", )
boton6 = tk.Button(ventana, text="6",
                   command=lambda: mostrar_boton("6"),
                   width=11,height=5, bg="cyan", )
boton7 = tk.Button(ventana, text="7",
                   command=lambda: mostrar_boton("7"),
                   width=11,height=5, bg="cyan", )
boton8 = tk.Button(ventana, text="8",
                   command=lambda: mostrar_boton("8"),
                   width=11,height=5, bg="cyan",)
boton9 = tk.Button(ventana, text="9",
                   command=lambda: mostrar_boton("9"),
                   width=11,height=5, bg="cyan",)

boton_suma = tk.Button(ventana, text="+",
                       command=lambda: mostrar_boton("+"),
                       width=11, height=5, bg="cyan")
boton_res = tk.Button(ventana, text="-",
                       command=lambda: mostrar_boton("-"),
                       width=11, height=5, bg="cyan")
boton_multi = tk.Button(ventana, text="*",
                       command=lambda: mostrar_boton("*"),
                       width=11, height=5, bg="cyan")
boton_div = tk.Button(ventana, text="÷",
                       command=lambda: mostrar_boton("/"),
                       width=11, height=5, bg="cyan",)
boton_C = tk.Button(ventana, text="C",
                   command=lambda: mostrar_boton("C"),
                   width=24,height=5, bg="cyan", )
boton_borrar = tk.Button(ventana, text="CE",
                   command=lambda: mostrar_boton("<-"),
                   width=23,height=5, bg="cyan", )
boton_Igual = tk.Button(ventana, text="=",
                        command=lambda: mostrar_boton("="),
                        width=11, height=5, bg="cyan")




# Signos

boton_Igual.grid(row=6, column=3)
boton_div.grid(row=6, column=4)
boton_multi.grid(row=5, column=4)
boton_res.grid(row=4, column=4)

boton_C.grid(row=2, column=3, columnspan=2)
boton_borrar.grid(row=2, column=1, columnspan=2)
# Row 3

boton2.grid(row=3, column=2)
boton3.grid(row=3, column=3)
# Row 4
boton4.grid(row=4, column=1)

boton6.grid(row=4, column=3)

# Row 5
boton7.grid(row=5, column=1)
boton8.grid(row=5, column=2)

# Row 6
boton0.grid(row=6, column=1, columnspan=2)

def mostrar_boton(btn):
    global numeros
    if(btn == "="):
        try:
            resultado = str(eval(numeros))
            texto_Numerico.set(resultado)
            numeros = resultado
        except:
            texto_Numerico.set("Error")
            numeros = ""
    elif(btn == "C"):
        numeros = ""
        texto_Numerico.set("")
    elif(btn == "<-"):
        numeros = numeros[:-1]
        texto_Numerico.set(numeros)
    else:
        numeros += btn
        texto_Numerico.set(numeros)


ventana.mainloop()














