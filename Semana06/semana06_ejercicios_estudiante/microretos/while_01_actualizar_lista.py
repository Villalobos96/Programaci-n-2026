"""Micro-reto 3: actualizar una lista por índice con while.

Contexto: puntajes ficticios de una actividad universitaria expresados como
porcentajes. Para un análisis, se transformarán a valores entre 0 y 1.

Prediga la lista final. Complete la actualización y siga el valor del índice.
"""
#
puntajes = [72, 85, 90]
indice = 0
#Mientras 0 menor 4
while indice < len(puntajes):
    # TODO: actualice el puntaje de esta posición dividiéndolo entre 100.
    #print("Seleccion por indice", puntajes[indice])
    puntajes[indice] = puntajes[indice] / 100
    print(puntajes)
    indice += 1

print("Puntajes normalizados:", puntajes)

# Resultado esperado: [0.72, 0.85, 0.9]
