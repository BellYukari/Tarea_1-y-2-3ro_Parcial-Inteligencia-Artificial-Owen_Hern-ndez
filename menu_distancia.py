import tkinter as tk
from tkinter import messagebox
import subprocess
import os
# Verificar que los scripts existan
ARCHIVO_MANUAL = "distancia_manual.py"
ARCHIVO_AUTOMATICO = "distancia_automatica.py"
ENVIO_CORREO = "enviar_distancia.py"

def verificar_archivos():
    faltantes = []
    if not os.path.exists(ARCHIVO_MANUAL):
        faltantes.append(ARCHIVO_MANUAL)
    if not os.path.exists(ARCHIVO_AUTOMATICO):
        faltantes.append(ARCHIVO_AUTOMATICO)
    if not os.path.exists(ENVIO_CORREO):
        faltantes.append(ENVIO_CORREO)
    return faltantes

def ejecutar_manual():
    faltantes = verificar_archivos()
    if faltantes:
        tk.messagebox.showerror("Error", f"No se encontraron los archivos: {', '.join(faltantes)}")
        return
    try:
        subprocess.run(["python3", ARCHIVO_MANUAL], check=True)
    except subprocess.CalledProcessError:
        tk.messagebox.showerror("Error", "Hubo un error al ejecutar el modo manual.")
    except FileNotFoundError:
        tk.messagebox.showerror("Error", "No se encontró 'python3'. Asegúrate de tener Python instalado.")

def ejecutar_automatico():
    faltantes = verificar_archivos()
    if faltantes:
        tk.messagebox.showerror("Error", f"No se encontraron los archivos: {', '.join(faltantes)}")
        return
    try:
        subprocess.run(["python3", ARCHIVO_AUTOMATICO], check=True)
    except subprocess.CalledProcessError:
        tk.messagebox.showerror("Error", "Hubo un error al ejecutar el modo automático.")
    except FileNotFoundError:
        tk.messagebox.showerror("Error", "No se encontró 'python3'. Asegúrate de tener Python instalado.")

def enviar_resultados():
    try:
        # Ejecutar el script manual o automático (asegúrate de que ya se hayan generado los archivos)
        # Aquí asumimos que los archivos 'resultado_con_puntos.jpg' y 'resultados.txt' ya están disponibles
        
        # Llamar al script de envío de correo
        subprocess.run(["python3", ENVIO_CORREO], check=True)
        
        print("Correo electrónico enviado correctamente.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al enviar el correo electrónico: {e}")

# --- Ventana del menú ---
def menu_principal():
    # Verificar archivos al iniciar
    faltantes = verificar_archivos()
    if faltantes:
        tk.messagebox.showwarning("Advertencia", f"No se encontraron: {', '.join(faltantes)}\nAsegúrate de que estén en la misma carpeta.")

    # Crear ventana
    root = tk.Tk()
    root.title("📏 Calculadora de Distancia")
    root.geometry("400x300")
    root.resizable(False, False)

    # Título
    tk.Label(root, text="Selecciona una opción", font=("Arial", 18, "bold")).pack(pady=20)

    # Botones
    tk.Button(
        root,
        text="Modo Manual",
        font=("Arial", 14),
        width=20,
        bg="#2196F3",
        fg="white",
        command=ejecutar_manual
    ).pack(pady=10)

    tk.Button(
        root,
        text="Modo Automático",
        font=("Arial", 14),
        width=20,
        bg="#4CAF50",
        fg="white",
        command=ejecutar_automatico
    ).pack(pady=10)

    tk.Button(
        root,
        text="Enviar Resultados",
        font=("Arial", 14),
        width=20,
        bg="#FF9800",
        fg="white",
        command=enviar_resultados
    ).pack(pady=10)

    # Nota
    tk.Label(
        root,
        text="Los scripts deben estar en la misma carpeta",
        font=("Arial", 9),
        fg="gray"
    ).pack(pady=10)

    root.mainloop()

# --- Inicio ---
if __name__ == "__main__":
    menu_principal()