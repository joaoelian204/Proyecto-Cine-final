import tkinter as tk
from colores import COLOR_BOTON_HOVER, COLOR_TEXTO_HOVER, COLOR_BOTON_NORMAL, COLOR_TEXTO_NORMAL

def on_enter(event, button):
    """
    Cambia el color del botón cuando el cursor está encima.

    Args:
        event (tk.Event): El evento de entrada del cursor.
        button (tk.Button): El botón al que se le aplica el cambio.
    """
    button.config(bg=COLOR_BOTON_HOVER, fg=COLOR_TEXTO_HOVER)

def on_leave(event, button):
    """
    Restaura el color original del botón cuando el cursor sale de él.

    Args:
        event (tk.Event): El evento de salida del cursor.
        button (tk.Button): El botón al que se le aplica el cambio.
    """
    button.config(bg=COLOR_BOTON_NORMAL, fg=COLOR_TEXTO_NORMAL)

def bind_hover_events(button):
    """
    Asocia eventos de hover (entrada y salida del cursor) a un botón.

    Args:
        button (tk.Button): El botón al que se le asocian los eventos.
    """
    button.bind("<Enter>", lambda event: on_enter(event, button))  # Asocia evento de entrada del cursor
    button.bind("<Leave>", lambda event: on_leave(event, button))  # Asocia evento de salida del cursor

def toggle_panel(menu_lateral):
    """
    Muestra u oculta el menú lateral.

    Args:
        menu_lateral (tk.Frame): El marco del menú lateral que se va a mostrar u ocultar.
    """
    if menu_lateral.winfo_ismapped():  # Si el menú lateral está visible
        menu_lateral.pack_forget()  # Oculta el menú lateral
    else:
        menu_lateral.pack(side=tk.LEFT, fill=tk.Y)  # Muestra el menú lateral
