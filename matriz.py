matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som =soml= 0
maior = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"digite um valor para [{l}, {c}]: "))
print("#" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        if matriz [l][c]%2 == 0:
            som += matriz[l][c]
    print()        
print(som)
soml = matriz[0][1] + matriz[1][1] + matriz[2][1]
print(soml)
maior.append(matriz[0][1])
maior.append(matriz[1][1])
maior.append(matriz[2][1])
maior.sort()
print(maior[2])
