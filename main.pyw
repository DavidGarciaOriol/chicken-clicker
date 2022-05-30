from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image

# # # ______________________________
# Tkinter Init & Variables

raiz = Tk()

    # Add Frame

menu_superior = Menu(raiz)
raiz.config(menu=menu_superior, width=900, height=600)

    # Game Counter Variable

raiz.contador_huevos = 0

# # # ______________________________
# Functions

    # Close Game

def cerrar_juego():
    valor = messagebox.askokcancel("Salir al escritorio", "¿Seguro que deseas salir?")
    if valor == True:
        raiz.destroy()
    

    # Increase Egg Counter

def sumar_huevo_contador():
    raiz.contador_huevos += 1
    egg_counter_lavel.config(text= f" x {raiz.contador_huevos}")


# # # ______________________________
# Create and Add Elements

    # Add Chicken Image

chicken_img = Image.open("src\\img\\main_chicken.png")
chicken_img_final = ImageTk.PhotoImage(chicken_img)

chicken_label = tkinter.Label(raiz, image=chicken_img_final)

    # Add Egg

egg_img = Image.open("src\\img\\egg_to_add.png")
egg_img_final = ImageTk.PhotoImage(egg_img)

egg_label = Label(raiz, image=egg_img_final)
egg_label.place(x=75, y=450)

    # Add Egg Counter

egg_counter_lavel = Label(raiz, text= f" x {raiz.contador_huevos}")
egg_counter_lavel.place(x=150, y=550)

    # Create Chicken Button

chicken_button = tkinter.Button(raiz, command=sumar_huevo_contador, borderwidth=0)
chicken_button.place(x=375, y=125)
chicken_button.config(image=chicken_img_final)

# # # ______________________________
# Menus

    # Create Main Menu

menu_principal = Menu(menu_superior, tearoff=0)
menu_principal.add_command(label="Guardar")
menu_principal.add_command(label="Cerrar", command=cerrar_juego)

    # Add Main Menu
    
menu_superior.add_cascade(label="Juego", menu=menu_principal)

# # # ______________________________
# Main Loop

    # Yep, the main loop.

raiz.mainloop()