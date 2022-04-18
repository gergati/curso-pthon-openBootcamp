
from math import ceil, floor


peso = input("Cuanto pesas?")
peso2 = int(peso)
altura = input("Cual es tu estatura?")
altura2 = float(altura)
print(altura2*2)
imc = peso2 / (altura2*2)
imc2 = floor(imc)
print(" Tu índice de masa corporal es ", imc2)