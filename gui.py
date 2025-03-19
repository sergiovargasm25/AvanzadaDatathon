import tkinter as tk
from tkinter import scrolledtext
from main import obtener_respuesta  # Importamos la función de main.py

# Función para manejar el evento de enviar
def enviar_consulta():
    consulta = text_entrada.get("1.0", tk.END).strip()
    if consulta:
        respuesta = obtener_respuesta(consulta)
        text_resultado.delete("1.0", tk.END)  # Limpiar el área de resultados
        text_resultado.insert(tk.END, respuesta)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Asistente de Análisis de Cohortes")
ventana.geometry("600x400")

# Etiqueta y cuadro de entrada para la consulta
label_entrada = tk.Label(ventana, text="Consulta:")
label_entrada.pack(pady=5)

text_entrada = scrolledtext.ScrolledText(ventana, width=70, height=5)
text_entrada.pack(pady=5)

# Etiqueta y cuadro para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack(pady=5)

text_resultado = scrolledtext.ScrolledText(ventana, width=200, height=10)
text_resultado.pack(pady=5)

# Botón para enviar la consulta
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_consulta)
boton_enviar.pack(pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()
