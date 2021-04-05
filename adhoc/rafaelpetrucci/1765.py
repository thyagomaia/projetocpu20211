while True:
    number = int(input())
    if number == 0:
        break
    for i in range(1, number + 1):
        aux = list(map(float, input().split()))
        resultado = aux[0] * (((aux[1] + aux[2]) * 5)/2)
        print('Size #{}:\nIce Cream Used: {:.2f} cm2'.format(i, resultado))
    print()