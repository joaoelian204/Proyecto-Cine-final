import tkinter as tk
import sqlite3
from tkinter import messagebox
import re

# Función para guardar datos en la base de datos SQLite
def guardar_datos(nombre, correo, contraseña, genero):
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()

    # Creación de la tabla usuarios con las columnas correctas
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, correo TEXT, contraseña TEXT, genero TEXT)''')

    cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña, genero) VALUES (?, ?, ?, ?)",
                   (nombre, correo, contraseña, genero))
    conexion.commit()

    user_id = cursor.lastrowid  # Obtener el ID del usuario recién registrado

    messagebox.showinfo("Registro exitoso", "Registro guardado correctamente")

    cursor.close()
    conexion.close()
    
    return user_id  # Retornar el ID del usuario

def verificar_credenciales(usuario, contraseña):
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE correo=? AND contraseña=?", (usuario, contraseña))
    usuario_registrado = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario_registrado  # Devuelve una tupla con los datos del usuario o None

# Función para abrir la ventana de registro
def abrir_ventana_registro():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Formulario de Registro")
    ventana_registro.geometry("450x300")
    ventana_registro.configure(bg="#2c3e50")
    ventana_registro.resizable(False, False)

    # Componentes del formulario de registro
    label_nombre = tk.Label(ventana_registro, text="Nombre de usuario:", bg="#2c3e50", fg="#ecf0f1")
    label_nombre.grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana_registro, width=30)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    label_correo = tk.Label(ventana_registro, text="Correo electrónico:", bg="#2c3e50", fg="#ecf0f1")
    label_correo.grid(row=1, column=0, padx=10, pady=5)
    entry_correo = tk.Entry(ventana_registro, width=30)
    entry_correo.grid(row=1, column=1, padx=10, pady=5)

    label_contraseña = tk.Label(ventana_registro, text="Contraseña:", bg="#2c3e50", fg="#ecf0f1")
    label_contraseña.grid(row=2, column=0, padx=10, pady=5)
    entry_contraseña = tk.Entry(ventana_registro, show="*", width=30)
    entry_contraseña.grid(row=2, column=1, padx=10, pady=5)

    label_genero = tk.Label(ventana_registro, text="Género:", bg="#2c3e50", fg="#ecf0f1")
    label_genero.grid(row=3, column=0, padx=10, pady=5)
    genero_var = tk.StringVar(value="Hombre")
    opciones_genero = ["Hombre", "Mujer", "Otros"]
    entry_genero = tk.OptionMenu(ventana_registro, genero_var, *opciones_genero)
    entry_genero.grid(row=3, column=1, padx=10, pady=5)

    def guardar_registro():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        contraseña = entry_contraseña.get()
        genero = genero_var.get()

        # Verificar que todos los campos estén llenados
        if nombre == "" or contraseña == "" or correo == "":
            messagebox.showerror("Error", "Por favor, complete todos los campos del formulario.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "Ingrese un correo electrónico válido.")
        else:
            user_id = guardar_datos(nombre, correo, contraseña, genero)  # Obtener el ID del usuario registrado
            ventana_registro.destroy()
            return user_id  # Retornar el ID del usuario registrado

    boton_guardar = tk.Button(ventana_registro, text="Registrar", command=guardar_registro, width=30, bg="blue", fg="white")
    boton_guardar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="WE")


