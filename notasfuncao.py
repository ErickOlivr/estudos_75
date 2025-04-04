def notas(a,b,c,d):
    media= (a+b+c+d)/4
    nota= [a,b,c,d]
    nota.sort(reverse=True)

    
    escola ={
'quantidade de notas': len(nota),
'maior nota':nota[0],
'menor nota':nota[3],
'media':media
    }
    return escola



resp = notas(5.5,9.5, 10, 6.5)
print(resp)