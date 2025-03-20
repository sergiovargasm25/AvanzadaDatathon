import tkinter as tk
from tkinter import scrolledtext
from main import obtener_respuesta
from PIL import Image, ImageTk
import os

def enviar_consulta():
    consulta = text_entrada.get("1.0", tk.END).strip()
    if consulta:
        respuesta = obtener_respuesta(consulta)
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, respuesta)

        # Mostrar gráfico si se generó
        if "grafico.png" in respuesta:
            mostrar_imagen("grafico.png")
        else:
            # Limpiar la imagen si no hay gráfico
            panel.config(image="")
            panel.image = None

def mostrar_imagen(nombre_archivo):
    if os.path.exists(nombre_archivo):
        img = Image.open(nombre_archivo)

        # Obtener el tamaño real de la imagen
        ancho_original, alto_original = img.size

        # Definir un tamaño máximo para mostrar
        max_ancho, max_alto = 800, 500  # Ajusta según necesidad

        # Calcular la escala manteniendo la proporción
        ratio = min(max_ancho / ancho_original, max_alto / alto_original)
        nuevo_ancho = int(ancho_original * ratio)
        nuevo_alto = int(alto_original * ratio)

        img = img.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)  # Redimensionar con buena calidad
        img = ImageTk.PhotoImage(img)

        # Ajustar el tamaño del panel y mostrar la imagen
        panel.config(image=img, width=nuevo_ancho, height=nuevo_alto)
        panel.image = img
    else:
        text_resultado.insert(tk.END, "\nError: No se pudo cargar la imagen.")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Asistente Inteligente")
ventana.geometry("1000x900")  # Ventana más grande

# Entrada de texto
label_entrada = tk.Label(ventana, text="Escribe tu consulta:")
label_entrada.pack(pady=10)

text_entrada = scrolledtext.ScrolledText(ventana, width=120, height=10)
text_entrada.pack(pady=10)

# Área de resultado
label_resultado = tk.Label(ventana, text="Respuesta:")
label_resultado.pack(pady=10)

text_resultado = scrolledtext.ScrolledText(ventana, width=120, height=20)
text_resultado.pack(pady=10)

# Botón para enviar consulta
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_consulta)
boton_enviar.pack(pady=20)

# Panel para imágenes (gráficos)
panel = tk.Label(ventana)
panel.pack()

# Iniciar interfaz
ventana.mainloop()