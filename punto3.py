"""Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
cual se almacenaban en una pila en cada misión de caza que
emprendió (con la siguiente información planeta visitado, a quien
capturado, costo de la recompensa), resolver las siguientes
actividades:
a. Mostrar los planetas visitados en el orden hizo las misiones.
b. Determinar cuántos créditos galácticos recaudo en total.
c. Determinar el número de la misión en que capturo a Han Solo
y en que planeta fue, suponga que dicha misión está cargada."""

from pila import Pila

class Bitacora:
    def __init__(self, planeta, capturo, creditos):
        self.planeta = planeta
        self.capturo = capturo
        self.creditos = creditos

"""usare nombres al azar(salvo Han Solo)"""
bitacora_pila = [
    Bitacora("Luna", "Goku", 200),
    Bitacora("Jupiter", "Vegeta", 275),
    Bitacora("Marte", "Freezer", 654),
    Bitacora("Tierra", "Han Solo", 8584),
    ]

print("----------------------------------------------------------------")
print("PLANETAS VISITADOS:")
print("----------------------------------------------------------------")

for bitacora in bitacora_pila:
    print(bitacora.planeta)
    
recaudo = 0
for bitacora in bitacora_pila:
    recaudo += bitacora.creditos

print("----------------------------------------------------------------")    
print(f"CREDITOS RECAUDADOS: {recaudo}")
print("----------------------------------------------------------------")

solo = None
mision = 0
for bitacora in bitacora_pila:
    mision += 1
    if bitacora.capturo == "Han Solo":
        solo = (mision, bitacora.planeta)

if solo:
    print("----------------------------------------------------------------")
    print(f"HAN SOLO HA SIDO CAPTURADO EN LA MISION {solo[0]} .")
    print(f"EN EL PLANETA {solo[1]}")
    print("----------------------------------------------------------------")
