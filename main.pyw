from tkinter import *
from tkinter import messagebox

# # # ______________________________
# Tkinter Init & Variables

    # Inicializador Tkinter

raiz = Tk()
raiz.resizable(False, False)

    # Variables del Juego

raiz.poder_del_click = 1
raiz.poder_de_cocina = 1

raiz.contador_huevos = 0
raiz.contador_tortillas = 0
raiz.contador_trigo = 0
raiz.contador_pan = 0
raiz.contador_bocata_tortilla = 0

# # # ______________________________
# Funciones

    # Cerrar Juego

def cerrar_juego():
    valor = messagebox.askokcancel("Salir al escritorio", "¿Seguro que deseas salir?")
    if valor == True:
        raiz.destroy()

    # Controladores de Cantidades

def comprobar_cantidad_huevos(value:int):
    return raiz.contador_huevos >= value

def comprobar_cantidad_tortillas(value:int):
    return raiz.contador_tortillas >= value

def comprobar_cantidad_trigo(value:int):
    return raiz.contador_trigo >= value

def comprobar_cantidad_pan(value:int):
    return raiz.contador_pan >= value
    
    # Manejo Contador Huevos

def sumar_huevo_contador(value:int):
    raiz.contador_huevos += value
    egg_counter_label.config(text= f" x {raiz.contador_huevos}")

def restar_huevo_contador(value:int):
        raiz.contador_huevos -= value
        egg_counter_label.config(text= f" x {raiz.contador_huevos}")

    # Manejo Contador Trigo

def sumar_trigo_contador(value:int):
    raiz.contador_trigo += value
    trigo_counter_label.config(text= f" x {raiz.contador_trigo}")

def restar_trigo_contador(value:int):
        raiz.contador_trigo -= value
        trigo_counter_label.config(text= f" x {raiz.contador_trigo}")

    # Manejo Contador Tortilla

def sumar_tortilla_contador(value:int):
    if comprobar_cantidad_huevos(5) == False:
        return
    else:
        restar_huevo_contador(5)
        raiz.contador_tortillas += value
        tortilla_counter_label.config(text= f" x {raiz.contador_tortillas}")

def restar_tortilla_contador(value:int):
    raiz.contador_tortillas -= value
    tortilla_counter_label.config(text= f" x {raiz.contador_tortillas}")

    # Manejo Contador Pan

def sumar_pan_contador(value:int):
    if comprobar_cantidad_trigo(3) == False:
        return
    else:
        restar_trigo_contador(3)
        raiz.contador_pan += value
        pan_counter_label.config(text= f" x {raiz.contador_pan}")

def restar_pan_contador(value:int):
    raiz.contador_pan -= value
    pan_counter_label.config(text= f" x {raiz.contador_pan}")

    # Manejo Contador Bocata Tortilla

def sumar_bocata_tortilla_contador(value:int):
    if comprobar_cantidad_tortillas(2) == False or comprobar_cantidad_pan(1) == False:
        return
    else:
        restar_tortilla_contador(2)
        restar_pan_contador(1)
        raiz.contador_bocata_tortilla += value
        bocata_tortilla_counter_label.config(text= f" x {raiz.contador_bocata_tortilla}")

def restar_bocata_tortilla_contador(value:int):
    raiz.contador_bocata_tortilla -= value
    bocata_tortilla_counter_label.config(text= f" x {raiz.contador_bocata_tortilla}")


# # # ______________________________
# Crear y Agregar Elementos

    # Agregar Imagen Gallina

chicken_img= PhotoImage(file="src\\img\\main_chicken.png")

    # Agregar Botón Gallina

chicken_button = Button(raiz, command=lambda:sumar_huevo_contador(raiz.poder_del_click), borderwidth=0)
chicken_button.config(image=chicken_img)
chicken_button.place(x=375, y=125)

    # Agregar Imagen Huevo

egg_img = PhotoImage(file="src\\img\\egg_to_add.png")
egg_label = Label(raiz, image=egg_img)
egg_label.place(x=75, y=450)

    # Agregar Contador Huevo

egg_counter_label = Label(raiz, text= "", font="arial")
egg_counter_label.place(x=150, y=525)

    # Agregar Imagen Tortilla

tortilla_img = PhotoImage(file="src\\img\\tortilla.png")
tortilla_label = Label(raiz, image=tortilla_img)
tortilla_label.place(x=225, y=450)

    # Agregar Botón Crear Tortilla

tortilla_button = Button(raiz, text="Hacer Tortilla (5 Huevos)", command=lambda:sumar_tortilla_contador(raiz.poder_de_cocina))
tortilla_button.place(x=250, y=310)

    # Agregar Contador Tortilla

tortilla_counter_label = Label(raiz, text="", font="arial")
tortilla_counter_label.place(x=300, y=525)

    # Agregar Imagen Trigo

trigo_img = PhotoImage(file="src\\img\\el_trigo.png")
trigo_label = Label(raiz, image=trigo_img)
trigo_label.place(x=375, y=450)

    # Agregar Botón Trigo

trigo_button = Button(raiz, command=lambda:sumar_trigo_contador(raiz.poder_del_click), borderwidth=0)
trigo_button.config(image=trigo_img)
trigo_button.place(x=675, y=75)

    # Agregar Contador Trigo

trigo_counter_label = Label(raiz, text="", font="arial")
trigo_counter_label.place(x=450, y=525)

    # Agregar Imagen Pan

pan_img = PhotoImage(file="src\\img\\pan.png")
pan_label = Label(raiz, image=pan_img)
pan_label.place(x=525, y=450)

    # Agregar Botón Crear Pan

pan_button = Button(raiz, text="Hacer Pan (3 Trigo)", command=lambda:sumar_pan_contador(raiz.poder_de_cocina))
pan_button.place(x=250, y=340)

    # Agregar Contador Pan

pan_counter_label = Label(raiz, text="", font="arial")
pan_counter_label.place(x=600, y=525)

    # Agregar Imagen Bocata Tortilla

bocata_tortilla_img = PhotoImage(file="src\\img\\bocata_tortilla.png")
bocata_tortilla_label = Label(raiz, image=bocata_tortilla_img)
bocata_tortilla_label.place(x=675, y=450)

    # Agregar Botón Crear Bocata Tortilla

bocata_tortilla_button = Button(raiz, text="Hacer Bocata Tortilla (2 Tortillas / 1 Pan)", command=lambda:sumar_bocata_tortilla_contador(raiz.poder_de_cocina))
bocata_tortilla_button.place(x=250, y=370)

    # Agregar Contador Bocata Tortilla

bocata_tortilla_counter_label = Label(raiz, text="", font="arial")
bocata_tortilla_counter_label.place(x=750, y=525)


# # # ______________________________
# Menús

    # Agregar Menú Superior

menu_superior = Menu(raiz)
raiz.config(menu=menu_superior, width=900, height=600)

    # Agregar Menú Principal

menu_principal = Menu(menu_superior, tearoff=0)
menu_principal.add_command(label="Guardar")
menu_principal.add_command(label="Cerrar", command=cerrar_juego)

    # Introducir Menú Principal -> Menú Superior
    
menu_superior.add_cascade(label="Juego", menu=menu_principal)

# # # ______________________________
# Loop Principal

    # Sí. El Loop Principal. Nada que ver aquí.

raiz.mainloop()