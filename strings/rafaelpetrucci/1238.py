number = int(input())
for _ in range(number):
    palavra_A, palavra_B = input().split()
    aux = [list(palavra_A), list(palavra_B)]
    frase_Final = ''
    total_A = len(aux[0])
    total_B = len(aux[1])
    while True:
        i = 0
        if total_A == total_B == 0:
            break
        if i < total_A:
            frase_Final += aux[0][i]
            aux[0].pop(i)
            total_A -= 1
        if i < total_B:
            frase_Final += aux[1][i]
            aux[1].pop(i)
            total_B -= 1
    print(frase_Final)