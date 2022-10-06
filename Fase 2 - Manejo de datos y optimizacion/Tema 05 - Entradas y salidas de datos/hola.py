#print("Hola, bienvenido a tu primer script!")

import sys

print(sys.argv)

print(sys.argv[1:])

for argumento in sys.argv[1:]:
    print(argumento)

