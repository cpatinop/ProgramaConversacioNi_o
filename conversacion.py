from random import choice  # Libreria la importamos para usar el metodo choice

preguntas = [
"Por que el cielo es azul?: ",
"Por que hay una cara en la luna?: ",
"Donde estan los dinosuarios?: "
]

pregunta = choice(preguntas)  # creamos una variable llamada pregunta 
respuesta = input (pregunta).lower().strip()

while respuesta != "porque si":
    respuesta = input("Porque?:   ").strip().lower()


print ( "Oh entiendo")  