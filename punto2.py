
avengers = [
    ("Black Widow" ,'Scarlett Johansson', "Avengers", 2010),
    ("Capitana Marvel", "Carol Danvers", "", 2012),
    ("Iron Man", "Tony Stark", "Avengers", 1963),
    ("Spider-Man", "Peter Parker", "Avengers", 1962),
    ("Thor",'Chris Hemsworth', "Avengers", 1962),
    ("Star Lord", "", "Guardianes de la galaxia", 1976),
    ("Gamora",'', "Guardianes de la galaxia", 1975),
    ("Rocket Raccoon",'', "Guardianes de la galaxia", 2008),
    ("Groot",'', "Guardianes de la galaxia", 1960),
]

def buscarpersonaje(personajes, superheroe):
    for personaje in personajes:
        if personaje[0] == superheroe:
            return personaje[1]
    return None

superheroe = "Capitana Marvel"
n_personaje = buscarpersonaje(avengers, superheroe)

if n_personaje:
    print("------------------------------------------------------------------")
    print("Capitana Marvel esta en la lista.")
    print(f"El nombre de Capitana Marvel es: {n_personaje}")
    print("------------------------------------------------------------------")

else:
    print("------------------------------------------------------------------")
    print("Capitana Marvel no se encuentra en la lista de personajes.")
    print("------------------------------------------------------------------")


def almacen(listapersonajes, grupo):
    cola = []
    for personaje in listapersonajes:
        if personaje[2] == grupo:
            cola.append(personaje[0])
    return cola

grupo = "Guardianes de la galaxia"
cola_guardianes = almacen(avengers, grupo)
cantidad_guardianes = len(cola_guardianes)
print("------------------------------------------------------------------")
print(f"Hay {cantidad_guardianes} superhéroes de Guardianes de la Galaxia:")

for superheroe in cola_guardianes:
    print(superheroe)

print("------------------------------------------------------------------")
