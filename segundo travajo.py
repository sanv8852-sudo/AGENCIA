import tkinter
import base64
from tkinter import PhotoImage
from io import BytesIO

# ======================================================
# Imágenes en base64 (integradas directamente en el código)
# ======================================================

# Pequeñas imágenes representativas (iconos base64)
mole_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABbElEQVR4nO3bsUoDURAF0FfIgo8gISLJo5gR2iMxS3gJcYYMZbC7/AZDJTjQwAfx4RJpPp2wZZ6qqgAAAAAAAAAAAAAAAAAAAAAAAID8O0kFXd4XfH/d+w8vmnSGWqL+V8o2FzX8Rbn5sqq/TVmupxJP3GVxVav6m3Rtq7dUuO2vIazpD5L69nptZ2upbbgEae3g1F8xS5qYb9IcmcvGHF7T1p64wKofrHEDqR0qS9UR/3mhbp5dsTTGmXw3BbeQucLLRZ48Xle03MXWWTfs2g3E0KxPYD8QemJMW1a76mPf2kGy8KhzEZ7hHy2D9huXRFrhO0ZBz+n1o6Dlqz/h9crFr/U95xT6NjeWzQIAAAAAAAAAAAAAAAAAAAAAAADA/28XAgM9ux9HoAAAAABJRU5ErkJggg=='
bistec_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABVUlEQVR4nO3bsUoDQRAG4O8JgkuECA0YiEgi4gS5bG9haeMIZfAD+PSk0O7uM3I1mqqiAAAAAAAAAAAAAAAAAAAAAABgf5ckys/4Cj5+3/sfl+18Aauu/GUo31zUVH3mps+F5Yb7nFVn6uKzpA92ql1FfL5tfU/pq6v9B6qLStLtoP7zFzXc0B0qS3UZ7z2lhq5U8qykP0+F2mu4UsU9gFq2lXUqXQj9qTL1nZcKqtnRk7zRnYxmsRr+We4hcK7MUtctN/A9JbZTNfZtMiz3UjD5jvS34qfH65RVrR+0VtbIt3mMei3y3NeEJ2XfuwIAAAAAAAAAAAAAAAAAAAAAAABgP38WAwTnxdAhAAAAAElFTkSuQmCC'
huevos_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABXElEQVR4nO3bsUoDQRSG4S8JgkuECA0YiEgi4gS5bG9haeMIZfAD+PSk0O7uM3I1mqqiAAAAAAAAAAAAAAAAAAAAAABgf5ckys/4Cj5+3/sfl+18Aauu/GUo31zUVH3mps+F5Yb7nFVn6uKzpA92ql1FfL5tfU/pq6v9B6qLStLtoP7zFzXc0B0qS3UZ7z2lhq5U8qykP0+F2mu4UsU9gFq2lXUqXQj9qTL1nZcKqtnRk7zRnYxmsRr+We4hcK7MUtctN/A9JbZTNfZtMiz3UjD5jvS34qfH65RVrR+0VtbIt3mMei3y3NeEJ2XfuwIAAAAAAAAAAAAAAAAAAAAAAABgP38WAwTnxdAhAAAAAElFTkSuQmCC'
sopa_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABYUlEQVR4nO3bsUoDQRSG4S8JgkuECA0YiEgi4gS5bG9haeMIZfAD+PSk0O7uM3I1mqqiAAAAAAAAAAAAAAAAAAAAAABgf5ckys/4Cj5+3/sfl+18Aauu/GUo31zUVH3mps+F5Yb7nFVn6uKzpA92ql1FfL5tfU/pq6v9B6qLStLtoP7zFzXc0B0qS3UZ7z2lhq5U8qykP0+F2mu4UsU9gFq2lXUqXQj9qTL1nZcKqtnRk7zRnYxmsRr+We4hcK7MUtctN/A9JbZTNfZtMiz3UjD5jvS34qfH65RVrR+0VtbIt3mMei3y3NeEJ2XfuwIAAAAAAAAAAAAAAAAAAAAAAABgP38WAwTnxdAhAAAAAElFTkSuQmCC'
chilaquiles_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABZUlEQVR4nO3bsUoDQRSG4S8JgkuECA0YiEgi4gS5bG9haeMIZfAD+PSk0O7uM3I1mqqiAAAAAAAAAAAAAAAAAAAAAABgf5ckys/4Cj5+3/sfl+18Aauu/GUo31zUVH3mps+F5Yb7nFVn6uKzpA92ql1FfL5tfU/pq6v9B6qLStLtoP7zFzXc0B0qS3UZ7z2lhq5U8qykP0+F2mu4UsU9gFq2lXUqXQj9qTL1nZcKqtnRk7zRnYxmsRr+We4hcK7MUtctN/A9JbZTNfZtMiz3UjD5jvS34qfH65RVrR+0VtbIt3mMei3y3NeEJ2XfuwIAAAAAAAAAAAAAAAAAAAAAAABgP38WAwTnxdAhAAAAAElFTkSuQmCC'
enchiladas_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABXElEQVR4nO3bsUoDQRSG4S8JgkuECA0YiEgi4gS5bG9haeMIZfAD+PSk0O7uM3I1mqqiAAAAAAAAAAAAAAAAAAAAAABgf5ckys/4Cj5+3/sfl+18Aauu/GUo31zUVH3mps+F5Yb7nFVn6uKzpA92ql1FfL5tfU/pq6v9B6qLStLtoP7zFzXc0B0qS3UZ7z2lhq5U8qykP0+F2mu4UsU9gFq2lXUqXQj9qTL1nZcKqtnRk7zRnYxmsRr+We4hcK7MUtctN/A9JbZTNfZtMiz3UjD5jvS34qfH65RVrR+0VtbIt3mMei3y3NeEJ2XfuwIAAAAAAAAAAAAAAAAAAAAAAABgP38WAwTnxdAhAAAAAElFTkSuQmCC'

def cargar_imagen(b64_data):
    return PhotoImage(data=base64.b64decode(b64_data))

# ======================================================
# FUNCIÓN DE ORDENAR
# ======================================================

def ordenar():
    cadena = ""
    txtComidas.delete("1.0", tkinter.END)
    if ch1.get() == 1: cadena += "Mole poblano\n"
    if ch2.get() == 1: cadena += "Bistec encebollados\n"
    if ch3.get() == 1: cadena += "Huevos Rancheros\n"
    if ch4.get() == 1: cadena += "Sopa azteca\n"
    if ch5.get() == 1: cadena += "Chilaquiles\n"
    if ch6.get() == 1: cadena += "Enchiladas Suizas\n"
    txtComidas.insert("1.0", cadena)

# ======================================================
# CONFIGURACIÓN DE LA VENTANA
# ======================================================

ventana = tkinter.Tk()
ventana.title("Menú de comidas mexicanas 🇲🇽")
ventana.geometry("950x700")

# Variables
ch1 = tkinter.IntVar()
ch2 = tkinter.IntVar()
ch3 = tkinter.IntVar()
ch4 = tkinter.IntVar()
ch5 = tkinter.IntVar()
ch6 = tkinter.IntVar()

# Cargar imágenes embebidas
img_mole = cargar_imagen(mole_b64)
img_bistec = cargar_imagen(bistec_b64)
img_huevos = cargar_imagen(huevos_b64)
img_sopa = cargar_imagen(sopa_b64)
img_chilaquiles = cargar_imagen(chilaquiles_b64)
img_enchiladas = cargar_imagen(enchiladas_b64)

# Título
lblmensaje1 = tkinter.Label(ventana, text="🍴 Bienvenido al menú de comidas", font=("Arial", 18, "bold"))
lblmensaje1.pack(pady=10)

lblmensaje2 = tkinter.Label(ventana, text="Seleccione los platillos que desea ordenar y presione 'Pedir Orden'", font=("Arial", 11))
lblmensaje2.pack()

# Frame del menú
frame_menu = tkinter.Frame(ventana)
frame_menu.place(x=50, y=100)

def crear_platillo(texto, variable, imagen, fila):
    lbl = tkinter.Label(frame_menu, image=imagen)
    lbl.grid(row=fila, column=0, padx=15, pady=15)
    chk = tkinter.Checkbutton(frame_menu, text=texto, variable=variable, font=("Arial", 11))
    chk.grid(row=fila, column=1, sticky="w")

crear_platillo("Mole poblano", ch1, img_mole, 0)
crear_platillo("Bistec encebollados", ch2, img_bistec, 1)
crear_platillo("Huevos Rancheros", ch3, img_huevos, 2)
crear_platillo("Sopa azteca", ch4, img_sopa, 3)
crear_platillo("Chilaquiles", ch5, img_chilaquiles, 4)
crear_platillo("Enchiladas Suizas", ch6, img_enchiladas, 5)

btnOrdenar = tkinter.Button(ventana, text="Pedir Orden", command=ordenar, bg="#008000", fg="white", font=("Arial", 12, "bold"))
btnOrdenar.place(x=100, y=620)

txtComidas = tkinter.Text(ventana, width=40, height=20, font=("Arial", 10))
txtComidas.place(x=480, y=100)

ventana.mainloop()