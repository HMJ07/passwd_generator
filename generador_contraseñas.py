import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import os

def generar_contrasena():
    """Función que genera la contraseña y la muestra en la interfaz."""
    try:
        n = int(longitud_var.get())
        if n > 0:
            special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?`~"
            characters = string.ascii_letters + string.digits + special_characters
            
            word = "".join(random.choice(characters) for _ in range(n))
          
            contrasena_generada_var.set(word)
            
            entry_contrasena.config(state="readonly")
        else:
            contrasena_generada_var.set("Introduce un número positivo.")
            entry_contrasena.config(state="normal")
    except ValueError:
        contrasena_generada_var.set("Introduce un número válido.")
        entry_contrasena.config(state="normal")

def guardar_contrasena():
    """Función para guardar la contraseña en un archivo de texto."""
    contrasena = contrasena_generada_var.get()
    if not contrasena or "Introduce" in contrasena or "válido" in contrasena:
        messagebox.showwarning("Error", "Primero genera una contraseña para poder guardarla.")
        return

  
    from tkinter import filedialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de Texto", "*.txt")],
        title="Guardar Contraseña"
    )

    if file_path:
        try:
            with open(file_path, "w") as f:
                f.write(f"Password generada: {contrasena}")
            messagebox.showinfo("Guardado", f"Password guardada en:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("450x250")
ventana.configure(bg="#f0f0f0")

longitud_var = tk.StringVar()
contrasena_generada_var = tk.StringVar()

style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"), padding=10)
style.configure("TEntry", font=("Arial", 12))

frame = ttk.Frame(ventana, padding="15", style="TLabel")
frame.pack(expand=True)


label_longitud = ttk.Label(frame, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)

entry_longitud = ttk.Entry(frame, textvariable=longitud_var, width=15)
entry_longitud.pack(pady=5)


boton_generar = ttk.Button(frame, text="Generar Contraseña", command=generar_contrasena)
boton_generar.pack(pady=10)


entry_contrasena = ttk.Entry(frame, textvariable=contrasena_generada_var, width=40, state="readonly")
entry_contrasena.pack(pady=5)


boton_guardar = ttk.Button(frame, text="Guardar Contraseña", command=guardar_contrasena)
boton_guardar.pack(pady=10)

ventana.mainloop()
