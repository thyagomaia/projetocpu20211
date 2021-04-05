while True:
    contest = list(map(int, input().split()))
    if contest[0] == contest[1] == 0:
        break
    matriz = []
    validation = {1: 1, 2: 1, 3: 1, 4: 1}
    for _ in range(contest[0]):
        aux = input().split()
        matriz.append(aux.copy())

    for i in range(contest[0]):
        if '0' not in matriz[i]:
            validation[1] = 0
        if '1' not in matriz[i]:
            validation[4] = 0
        if i == 0:
            for coluna in range(contest[1]):
                aux = []
                for linha in range(contest[0]):
                    aux.append(matriz[linha][coluna])
                if '1' not in aux:
                    validation[2] = 0
                if '0' not in aux:
                    validation[3] = 0
    soma = validation[1] + validation[2] + validation[3] + validation[4]
    print(soma)