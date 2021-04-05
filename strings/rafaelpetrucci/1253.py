alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
total = len(alfabeto) - 1
number = int(input())
for _ in range(number):
    frase = list(input().lower())
    index = int(input())
    total_Frase = len(frase)
    for i in range(total_Frase):
        indice = alfabeto.index(frase[i]) - index
        frase[i] = alfabeto[indice]
    frase = "".join(frase).upper()
    print(frase)