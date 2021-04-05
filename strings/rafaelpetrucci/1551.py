alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
total = len(alfabeto)
number = int(input())
for _ in range(number):
    frase = input()
    aux = alfabeto.copy()
    for alfa in alfabeto:
        if alfa in frase:
            aux.remove(alfa)
    valor_Aux = len(aux)
    if valor_Aux == 0:
        print('frase completa')
    elif valor_Aux <= total//2:
        print("frase quase completa")
    else:
        print("frase mal elaborada")