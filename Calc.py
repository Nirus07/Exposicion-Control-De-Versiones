import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")
ventana.config(bg="#231673")

etiqueta = tk.Label(ventana,
                    text="Botones presionados: ", font=("Arial",12),
                    bg="white", width=33, height=4, anchor="nw", justify="right")
etiqueta.grid(row=0, column=0, columnspan=5, pady= 20)

      
boton1 = tk.Button(ventana, text="1",
                   command=lambda: mostrar_boton("1"),
                   width=8,height=4)
boton2 = tk.Button(ventana, text="1",
                   command=lambda: mostrar_boton("2"),
                   width=8,height=4)
boton3 = tk.Button(ventana, text="1",
                   command=lambda: mostrar_boton("3"),
                   width=8,height=4)
boton4 = tk.Button(ventana, text="1",
                   command=lambda: mostrar_boton("4"),
                   width=8,height=4)
boton5 = tk.Button(ventana, text="1",
                   command=lambda: mostrar_boton("5"),
                   width=8,height=4)
boton6 = tk.Button(ventana, text="6",
                   command=lambda: mostrar_boton("6"),
                   width=8,height=4)
boton7 = tk.Button(ventana, text="7",
                   command=lambda: mostrar_boton("7"),
                   width=8,height=4)
boton8 = tk.Button(ventana, text="8",
                   command=lambda: mostrar_boton("8"),
                   width=8,height=4)
boton9 = tk.Button(ventana, text="9",
                   command=lambda: mostrar_boton("9"),
                   width=8,height=4)

boton1.grid(row=1, column=1, padx= 2, pady= 20)
boton2.grid(row=1, column=2, padx= 2, pady= 20)
boton3.grid(row=1, column=3, padx= 2, pady= 20)
boton4.grid(row=2, column=1, padx= 2, pady= 20)
boton5.grid(row=2, column=2, padx= 2, pady= 20)
boton6.grid(row=2, column=3, padx= 2, pady= 20)
boton7.grid(row=3, column=1, padx= 2, pady= 20)
boton8.grid(row=3, column=2, padx= 2, pady= 20)
boton9.grid(row=3, column=3, padx= 2, pady= 20)




















