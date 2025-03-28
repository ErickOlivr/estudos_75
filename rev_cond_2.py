lados = []

for c in range (0,3):
     lados.append(float(input("Digite um lado do triangulo")))
print(lados)
if lados[0] == lados[1] and lados[1] == lados[2]:
    print("é um triangulo isosceles")
else:
    print("não é um triangulo isosceles")
