import sys

#print(sys.argv)

if len(sys.argv) == 3:
    if 1 <= int(sys.argv[1]) <= 9 and 1 <= int(sys.argv[2]) <= 9:
        fila, columna = int(sys.argv[1]), int(sys.argv[2])
        #print(f"Fila = {fila}, Columna = {columna}")

        for x in range(fila):
            for y in range(columna):
                print("*", end = "")
            print()

else:
    print("ERROR - Ingrese los parámetros correctamente")
    print("Ejemplo: ejercicio_optativo2 1 5")



