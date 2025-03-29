nmr = []
impar = []
par = []
for n in range(1,8):
    nmr.append(int(input(f"digite o {n}° numero: ")))

for c in nmr:
    if c%2 == 0:
      par.append(c)
    else:
      impar.append(c)

print("Numeros pares digitados: ", par)
print("Numeros impares digitados: ", impar)