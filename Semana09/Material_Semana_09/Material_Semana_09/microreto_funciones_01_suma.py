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

resultado = sumar_esperas(ESPERAS)

print("El tiempo total en horas: ", resultado)


#TODO: llame a la función sumar_esperas y guarde el resultado en una variable. Luego, imprima el resultado en horas.