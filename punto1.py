"""1. Desarrollar una función recursiva que permita contar cuantas veces
aparece una determinada palabra, en un vector de palabras."""

def palabrasr(vector, palabra, contador=0):
    if not vector:
        return contador
    else:
        if vector[0] == palabra:
            contador += 1
        return palabrasr(vector[1:], palabra, contador)

vector = ["buenas", "tardes", "parcial",
           "python", "visual", "mate","parcial",
           "pila","cola","lista","recursividad","parcial",
           "programacion","objetos","clase","parcial","termo" ]


palabra = "parcial"
cantidad = palabrasr(vector, palabra)
print(f"La palabra {palabra} aparece {cantidad} veces en el vector.")
