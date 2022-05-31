from ctypes import resize
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image

# # # ______________________________
# Tkinter Init & Variables

raiz = Tk()
raiz.resizable(False, False)

    # Add Frame

menu_superior = Menu(raiz)
raiz.config(menu=menu_superior, width=900, height=600)

    # Game Counter Variable

raiz.poder_del_click = 1

raiz.contador_huevos = 0
raiz.contador_tortillas = 0


# # # ______________________________
# Functions

    # Close Game

def cerrar_juego():
    valor = messagebox.askokcancel("Salir al escritorio", "¿Seguro que deseas salir?")
    if valor == True:
        raiz.destroy()

    # Check Egg Counter

def comprobar_cantidad_huevos(value:int):
    return raiz.contador_huevos >= value
    

    # Increase Egg Counter

def sumar_huevo_contador(value:int):
    raiz.contador_huevos += value
    egg_counter_label.config(text= f" x {raiz.contador_huevos}")

def restar_huevo_contador(value:int):
        raiz.contador_huevos -= value
        egg_counter_label.config(text= f" x {raiz.contador_huevos}")

    # Increase Tortilla Counter

def sumar_tortilla_contador():
    if comprobar_cantidad_huevos(5) == False:
        return
    else:
        restar_huevo_contador(5)
        raiz.contador_tortillas += 1
        tortilla_counter_label.config(text= f" x {raiz.contador_tortillas}")
        
        

# # # ______________________________
# Create and Add Elements

    # Add Chicken Image

chicken_img = Image.open("src\\img\\main_chicken.png")
chicken_img_final = ImageTk.PhotoImage(chicken_img)

chicken_label = tkinter.Label(raiz, image=chicken_img_final)

    # Add Create Chicken Button

chicken_button = tkinter.Button(raiz, command=lambda:sumar_huevo_contador(raiz.poder_del_click), borderwidth=0)

chicken_button.place(x=375, y=125)
chicken_button.config(image=chicken_img_final)

    # Add Egg Image

egg_img = Image.open("src\\img\\egg_to_add.png")
egg_img_final = ImageTk.PhotoImage(egg_img)

egg_label = Label(raiz, image=egg_img_final)
egg_label.place(x=75, y=450)

    # Add Egg Counter

egg_counter_label = Label(raiz, text= f" x {raiz.contador_huevos}")
egg_counter_label.place(x=150, y=525)

    # Create Tortilla Button

tortilla_button = tkinter.Button(raiz, text="Hacer Tortilla (5)", command=sumar_tortilla_contador)
tortilla_button.place(x=300, y=350)

    # Add Tortilla Image

tortilla_img = Image.open("src\\img\\tortilla.png")
tortilla_img_final = ImageTk.PhotoImage(tortilla_img)

tortilla_label = tkinter.Label(raiz, image=tortilla_img_final)
tortilla_label.place(x=225, y=450)

    # Add Tortilla Counter

tortilla_counter_label = Label(raiz, text="")
tortilla_counter_label.place(x=300, y=525)


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