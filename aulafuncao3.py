def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos += 1

valores = [0,3,5,70,6]
dobra(valores)
print(valores)