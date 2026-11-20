"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0

    for minuto in minutos:
        # TODO: acumule cada minuto en total.
        total += minuto
    
    horas = total / 60
    

    return horas
    return total

resultado = sumar_esperas(ESPERAS)
print("El tiempo total en horas: ", resultado)

total = sumar_esperas(ESPERAS)
print(sumar_esperas(ESPERAS))


totales = []
totales.append(sumar_esperas([20,60,20,30,]))
totales.append(sumar_esperas([10,60,180,20]))

#TODO: llame a la función sumar_esperas y guarde el resultado en una variable. Luego, imprima el resultado en horas.