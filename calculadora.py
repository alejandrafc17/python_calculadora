import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import math

# Configuración de la ventana principal
ventana = ttk.Window(themename="darkly")
ventana.title("Calculadora Científica")
ventana.geometry("500x650")
ventana.resizable(False, False)

# Campo de entrada
entrada = ttk.Entry(ventana, font=("Aptos narrow", 40), justify="right", bootstyle="success")
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

# Funciones para la calculadora
def click_boton(valor):
    entrada.insert(ttk.END, valor)

def borrar():
    entrada.delete(0, ttk.END)

def limpiar_ultimo():
    texto = entrada.get()
    if texto:
        entrada.delete(len(texto)-1, ttk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, ttk.END)
        entrada.insert(ttk.END, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")

def funciones_avanzadas(operacion):
    try:
        valor = float(entrada.get())
        if operacion == "sin":
            resultado = math.sin(math.radians(valor))
        elif operacion == "cos":
            resultado = math.cos(math.radians(valor))
        elif operacion == "tan":
            resultado = math.tan(math.radians(valor))
        elif operacion == "sqrt":
            resultado = math.sqrt(valor)
        elif operacion == "log":
            resultado = math.log10(valor)
        elif operacion == "ln":
            resultado = math.log(valor)
        elif operacion == "exp":
            resultado = math.exp(valor)
        entrada.delete(0, ttk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")

# Función que mapea las teclas del teclado a las operaciones
def teclado(event):
    tecla = event.keysym
    if tecla.isdigit():  # Números
        click_boton(tecla)
    elif tecla in ['plus', 'minus', 'asterisk', 'slash', 'period']:
        equivalencias = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/', 'period': '.'}
        click_boton(equivalencias[tecla])
    elif tecla == "BackSpace":  # Retroceso
        limpiar_ultimo()
    elif tecla == "Return":  # Enter como igual
        calcular()
    elif tecla.lower() == "c":  # Tecla 'C' para borrar todo
        borrar()

# Vincula las teclas a las funciones
ventana.bind("<Key>", teclado)

# Botones estándar
botones = [
    "7", "8", "9", "/", "sin",
    "4", "5", "6", "*", "cos",
    "1", "2", "3", "-", "tan",
    
    "C", "0", ".", "+", "sqrt",
    
    "(", ")", "**", "=", "log",
    
    "π", "e", "ln", "//", "exp",
]

# Posicionar botones en la cuadrícula
fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        ttk.Button(
            ventana, text=boton, style="success.TButton", command=calcular
        ).grid(row=fila, column=columna, padx=5, pady=5, sticky=NSEW)
    elif boton == "C":
        ttk.Button(
            ventana, text=boton, style="danger.TButton", command=borrar
        ).grid(row=fila, column=columna, padx=5, pady=5, sticky=NSEW)
    elif boton in ["sin", "cos", "tan", "sqrt", "log", "ln", "exp"]:
        ttk.Button(
            ventana, text=boton, style="primary.TButton", 
            command=lambda op=boton: funciones_avanzadas(op)
        ).grid(row=fila, column=columna, padx=5, pady=5, sticky=NSEW)
    elif boton == "π":
        ttk.Button(
            ventana, text=boton, style="info.TButton", 
            command=lambda: click_boton(str(math.pi))
        ).grid(row=fila, column=columna, padx=5, pady=5, sticky=NSEW)
    elif boton == "e":
        ttk.Button(
            ventana, text=boton, style="info.TButton", 
            command=lambda: click_boton(str(math.e))
        ).grid(row=fila, column=columna, padx=5, pady=5, sticky=NSEW)
    else:
        ttk.Button(
            ventana, text=boton, style="light.TButton", 
            command=lambda valor=boton: click_boton(valor)
        ).grid(row=fila, column=columna, padx=5, pady=5, sticky=NSEW)
    
    columna += 1
    if columna > 4:
        columna = 0
        fila += 1

# Botón de retroceso
ttk.Button(
    ventana, text="←", style="warning.TButton", command=limpiar_ultimo
).grid(row=fila, column=0, columnspan=5, padx=5, pady=10, sticky=NSEW)

# Ajustar tamaño de las columnas y filas
for i in range(5):
    ventana.grid_columnconfigure(i, weight=1)

for i in range(fila + 1):
    ventana.grid_rowconfigure(i, weight=1)

# Ejecutar la ventana principal
ventana.mainloop()
