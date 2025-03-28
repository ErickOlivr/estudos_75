lados = []

for c in range (0,3):
     lados.append(float(input("Digite um lado do triangulo")))
lados.sort
print(lados)

if lados[0] == lados[1] and lados[0] != lados[2]:
     print("é um triangulo isosceles")