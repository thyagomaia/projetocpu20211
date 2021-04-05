N = int(input())
lista = []

for i in range(0, N, 1):
    K = int(input())

    for y in range(0, K, 1):
        S = input()
        lista.append(S)
    Coisa = True
    for item in range(0, K, 1):
        if (lista[item] != lista[item-1]):
            print("ingles")
            Coisa = False
            break    
    if(Coisa == True):
        print(lista[0])
    lista.clear()