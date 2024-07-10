import tkinter as tk
from tkinter import filedialog

def seleccionar_imagen():
    filename = filedialog.askopenfilename(title="Seleccionar Imagen", filetypes=[("Archivos de Imagen", "*.png *.jpg *.jpeg")])
    return filename

def bind_hover_events(button):
    button.bind("<Enter>", lambda e: button.config(bg="#4CAF50"))
    button.bind("<Leave>", lambda e: button.config(bg="#2196F3"))

def crear_label_y_entry(parent, texto_label, valor_entry, row, column):
    estilo_label = {'bg': '#ffffff', 'fg': '#333', 'font': ('Arial', 11)}
    estilo_entry = {'bg': '#ffffff', 'fg': '#333', 'font': ('Arial', 11)}

    label = tk.Label(parent, text=texto_label, **estilo_label)
    label.grid(row=row, column=column, padx=10, pady=10, sticky=tk.E)

    entry = tk.Entry(parent, width=40, **estilo_entry)
    entry.grid(row=row, column=column+1, padx=10, pady=10)
    entry.insert(0, valor_entry)

    return entry

def crear_boton(parent, texto, comando, color_fondo, fila, columna, padx=10, pady=10):
    boton = tk.Button(parent, text=texto, command=comando, bg=color_fondo, fg='#fff')
    boton.grid(row=fila, column=columna, padx=padx, pady=pady)
    return boton
