producto = ["cafe", 5000, 20]

porcentaje_aumento = 20
descuento = producto[1]* 15 / 100
print(descuento)
precio_promocional = producto[1] - descuento

ingreso_actual = producto[1] * producto[2]
print(ingreso_actual)

aumento = producto[2] * porcentaje_aumento / 100
print(aumento)

suma_unidades = producto[2] + aumento
print(suma_unidades)

ingreso_proyectado = precio_promocional * suma_unidades
print(ingreso_proyectado)

diferencia = ingreso_proyectado - ingreso_actual
print(diferencia)

if diferencia > 0:
    print("Lanzar descuento")

else:
    print("no lanzar descuento")

print("\n\n")
print("-" * 70)
print("Analisis de Datos")
print("-" * 70)

print("Producto: cafe")
print(f"Precio actual: {producto[1]}")
print(f"Unidades actuales: {producto[2]}")
print(f"Ingreso actual: ₡{ingreso_actual:.0f}")
print(f"Descuento: ₡{descuento:.0f}")
print(f"Precio promocional: ₡{precio_promocional:.0f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {suma_unidades:.0f}")
print(f"Ingreso con promoción: ₡{ingreso_proyectado:.0f}")
print(f"Diferencia: ₡{diferencia:.0f}")