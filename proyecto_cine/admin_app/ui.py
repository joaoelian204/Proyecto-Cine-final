# ui.py
import tkinter as tk
from tkinter import font
from info_usuario import *
from funciones import toggle_panel, mostrar_cartelera, mostrar_ventana_agregar
from publicidad import gestionar_publicidad  # Importar la función de publicidad

def iniciar_aplicacion():
    root = tk.Tk()
    configurar_ventana(root)

    barra_superior, menu_lateral, cuerpo_principal = crear_paneles(root)
    configurar_barra_superior(barra_superior, lambda: toggle_panel(menu_lateral))
    configurar_menu_lateral(menu_lateral, cuerpo_principal)

    mostrar_cartelera(cuerpo_principal)

    root.mainloop()

def configurar_ventana(root):
    root.title("Plataforma de Cine")
    root.geometry("1920x1010")
    root.resizable(False, False)

def crear_paneles(root):
    from constants import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL

    barra_superior = tk.Frame(root, bg=COLOR_BARRA_SUPERIOR, height=50)
    barra_superior.pack(side=tk.TOP, fill=tk.BOTH)

    menu_lateral = tk.Frame(root, bg=COLOR_MENU_LATERAL, width=200)
    menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

    canvas = tk.Canvas(root, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    cuerpo_principal = tk.Frame(canvas, bg=COLOR_CUERPO_PRINCIPAL)
    canvas.create_window((0, 0), window=cuerpo_principal, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    cuerpo_principal.bind("<Configure>", on_configure)

    return barra_superior, menu_lateral, cuerpo_principal

def configurar_barra_superior(barra_superior, toggle_panel_callback):
    from constants import COLOR_BARRA_SUPERIOR
    font_awesome = font.Font(family='FontAwesome', size=15)

    label_titulo = tk.Label(barra_superior, text="Plataforma Administrador Cine", fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, highlightthickness=0)
    label_titulo.pack(side=tk.LEFT, padx=10)

    button_menu_lateral = tk.Button(barra_superior, text="☰", font=font_awesome, command=toggle_panel_callback, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="#fff", padx=10)
    button_menu_lateral.pack(side=tk.LEFT, padx=10)

    label_info = tk.Label(barra_superior, text="BIENVENIDO ADMIM", fg="#fff", font=("Roboto", 13), bg=COLOR_BARRA_SUPERIOR, padx=10)
    label_info.pack(side=tk.RIGHT)

import tkinter as tk
from constants import COLOR_BOTON_NORMAL
from tkinter import font
from info_usuario import mostrar_ventana_usuarios  # Importa la función del módulo info_usuario
from publicidad import gestionar_publicidad  # Importar la función de publicidad

def configurar_menu_lateral(menu_lateral, cuerpo_principal):
    font_awesome = font.Font(family='FontAwesome', size=15)
    buttons_info = [
        ("Editar Película", "🎬", lambda: mostrar_cartelera(cuerpo_principal)),
        ("Añadir Película", "➕", lambda: mostrar_ventana_agregar(cuerpo_principal)),
        ("Ver Usuario", "👤", lambda: mostrar_ventana_usuarios()), 
        ("Ver Publicidad", "📺", gestionar_publicidad)  # Añadir botón para ver publicidad
    ]
    for txt, icon, command in buttons_info:
        button = tk.Button(menu_lateral, text=f"{icon} {txt}", anchor="w", font=font_awesome, bd=0, bg=COLOR_BOTON_NORMAL, fg="#fff", width=15, height=1, command=command)
        button.pack(side=tk.TOP, pady=10, padx=20, fill=tk.X)



