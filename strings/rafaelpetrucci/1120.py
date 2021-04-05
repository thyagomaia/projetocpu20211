while True:
    valores = input().split()
    if valores[0] == valores[1] == '0':
        break
    valores[1] = valores[1].replace(valores[0], '')
    if valores[1] == '':
        valores[1] = '0'
    valores[1] = int(valores[1])
    print(valores[1])