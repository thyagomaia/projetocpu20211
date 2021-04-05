N = int(input())

for j in range(N): 
    s1, s2 = input().split()
    tam1 = len(s1)
    tam2 = len(s2)
    tmenor = 0

    if(tam1 > tam2):
        tmenor = tam2
        strg = s2 + s1
    else:
        tmenor = tam1
        strg = s1 + s2

    tam = len(strg)

    cont1 = 0
    cont2 = 0

    strgvet = [strg[i] for i in range(tam)]
    s1vet = [s1[i] for i in range(tam1)]
    s2vet = [s2[i] for i in range(tam2)]

    for i in range(2*tmenor):
            if(i % 2 == 0):
                strgvet[i] = s1vet[cont1]
                cont1 += 1
            else:
                strgvet[i] = s2vet[cont2]
                cont2 += 1
                
    strg = ''.join(strgvet)

    print(strg)