#[Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:
#Debe tomar 1 argumento que será un número entero positivo.
#En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
#** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**
#>  3647
#** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **
#>  0007
#   0040
#   0600
#   3000
#Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

## Ingreso y conversión de string a Lista
print("Ingresa un numero positivo para descomponerlo en unidades, decenas, centenas, miles.")
user = input("")
print()

numero=[int(i) for i in user] # lista numeros

## descomposición 

largo = len(numero)
multiplos = [1, 10, 100, 1000, 10000]



for n,i in enumerate(numero):
    muestra = numero[-i]
    print(f"{muestra:0{largo}d}")

print(muestra)
print(numero)


'''
if numero > 0:
    if numero > 10:
        pass
    elif 10 >= numero <= 99:
        pass
    elif 100 >= numero <= 999:
        pass
    elif 1000 >= numero <= 9999:
        pass
    else:
        print("El número ")

else:
    print("Error: Ingresa los parámetros de forma correcta!!")
    print("Ejemplo: 1111")'''

