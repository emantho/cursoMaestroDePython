import sys
script = sys.argv

# Completa el ejercicio aquí
if len(script) >= 2:
    def separar(lista):
        pares = []
        impares = []

        for arg in lista[1:]:
            if int(arg) % 2 == 0:
                pares.append(arg)
            else:
                impares.append(arg)
        pares.sort()
        impares.sort()
        return pares, impares

    pares, impares = separar(script)
    print(pares)
    print(impares)

else:
    print("ERROR - Ingrese los valores correctamente")
    print("Ejemplo: script.py 5 8 4 3 -5 -8 4")
