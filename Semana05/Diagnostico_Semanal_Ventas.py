"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) # Total de ventas semanal
cantidad_centro = len(ventas_centro) #Catidad de días registrados

menor_centro = min(ventas_centro) #Venta minima centro
mayor_centro = max(ventas_centro) #Venta maximo centro
promedio_centro  = total_centro / cantidad_centro

porcentaje_centro = total_centro * 100 / meta_centro

print(porcentaje_centro)

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte) # Total de ventas semanal
cantidad_norte = len(ventas_norte) #Catidad de días registrados

menor_norte = min(ventas_norte) #Venta minima norte
mayor_norte = max(ventas_norte) #Venta maximo norte
promedio_norte  = total_norte / cantidad_norte

porcentaje_norte = total_norte * 100 / meta_norte

print(porcentaje_norte)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro == meta_centro:
    estado_centro == "meta alcanzada exactamente"
else:
    estado_centro = "meta NO alcanzada"
    
if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte == "meta alcanzada exactamente"
else:
    estado_norte = "meta NO alcanzada"
# TODO: compara los totales y los rangos.
if total_centro > total_norte :
    tienda_gano = "Tienda centro"
elif total_norte > total_centro:
    tienda_gano = "Tienda del Norte"
else:
    tienda_gano = "Ambas tiendas tiene el mismo total"
    
print("COMPARACION SEMANAL DE TIENDAS")
print("-" * 70)

print(f"Centro | total ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro: {estado_centro}")

print("-" * 70)

print(f"Norte - total ₡{total_norte: ,.2f} - meta ₡ {meta_norte: ,.2f} - cumplimiento {porcentaje_norte:.0f}%")
print(f"Norte logro : {estado_norte}")




# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.