import sys

link = sys.argv
def mensaje():
    print("Error: Ingrese los datos correctamente.")
    print("Ejemplo: descomposicion.py [0-1234]")



if len(link) == 2:
    num = int(link[1])
    long = len(link[1])

    if 0 <= num <= 9999:
        num = str(num)
        num = [int(i) for i in num]
        for n,i in enumerate(num):
            ind = num[-n]
            print(ind)
            final = ind * 10 ** n
            print(f"{final:0{long}d}")

    else:
        mensaje()
else:
    mensaje()