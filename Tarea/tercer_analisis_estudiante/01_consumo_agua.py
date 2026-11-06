"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

consumo_total = sum(consumos_litros)

#Promedio Diario
promedio_diario = consumo_total / len(consumos_litros)

#Comparar primer dia con el ultimo

primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[4]
litros_ahorrados = primer_dia - ultimo_dia
porcentaje_reduccion = (litros_ahorrados / primer_dia) * 100

#Clasificar

if porcentaje_reduccion >=15:
    clasificacion = "Reduccion alta"
elif porcentaje_reduccion > 0:
    clasificacion = "Reduccion moderada"
else:
    clasificacion = "Sin reduccion"


print(f"consumo total:  {consumo_total} L")
print(f"Promedio diario: {promedio_diario} L")
print(f"Litros ahorrados: {litros_ahorrados} L")
print(f"Porcentaje de reduccion: {porcentaje_reduccion: .0f} %")
print(f"Clasificacion:  {clasificacion}")








# TODO: Calcule el consumo total y el promedio diario.
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
