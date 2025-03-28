notas = []
c = 1
nome = input("Digite seu nome: ")
for c in range(1,3):
    notas.append(float(input(f"{nome}Digite sua {c}° nota: ")))
media = (notas[0] + notas[1])/2
if media >= 7 and media <=10:
    print(f"sua média é {media}: passou")
elif media >= 3:
    print(f"sua média é {media}: prova final")
else:
    print(f"sua média é {media}: reprovação")
