#Solucion: Mision kit seguro

nombre = input("nombre :").upper().strip()
kit = input("Tipo de kit : ").lower().strip()
autorizacion = input("Tiene autorizacion (si/no)").lower().strip()=='si'
try:
    cantidad = int(input("Cantidad de kits? :"))
except:
    print("Cantidad de kits invalida, digite del 1 al 100")
    cantidad = -1
    print("Error la cantidad minima es 1")

try:
    dias = int(input("Dias de prestamo :"))
except:
    print("Cantidad de Dias de prestamo es incorrecto, digite del 1 al 100")
    dias = -1

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazaado: revise los datos ingresados!"

elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"solicitud aprobada para {nombre}: {cantidad} kits(s) de {kit}"

else:
    resultado = "Solicitud enviada a revision "

print("-" * 50)
print(resultado)



