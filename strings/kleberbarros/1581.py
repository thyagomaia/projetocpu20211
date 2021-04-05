N = int(input())
for i in range(N):
    K = int(input())
    Vstrg = [input() for i in range(K)]
    tam = len(Vstrg)
    cont = 0

    for i in range(K-1):
        if(Vstrg[i+1] == Vstrg[i]):
            cont += 1

    if(cont != tam-1):
        print('ingles')
    else:
        print(Vstrg[0])