"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
# TODO: Calcule el promedio y su porcentaje de ocupación.
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.


# Recorrer con for para acumular total y contar bloques > 70%
total = 0
bloques_altos = 0
limite_70 = capacidad * 0.70

for asistencia in asistencias:
    total = total + asistencia
    if asistencia > limite_70:
        bloques_altos = bloques_altos + 1

# Calcule el promedio y su porcentaje de ocupación
promedio = total / len(asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100

# Clasifique el promedio
if porcentaje_ocupacion >= 80:
    estado = "Ocupación alta"
elif porcentaje_ocupacion >= 50:
    estado = "Ocupación media"
else:
    estado = "Ocupación baja"

# Muestre el total, promedio, porcentaje, cantidad de bloques y estado
print(f"Total: {total}")
print(f"Promedio: {promedio}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.0f} %")
print(f"Bloques que superan el 70%: {bloques_altos}")
print(f"Estado: {estado}")