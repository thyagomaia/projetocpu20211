T = int(input())
quantidades = [] 
quantidades.append(T)
geral = []

while T != 0:
    for i in range(0, T, 1):
        numeros = input().split(" ")
        Q = int(numeros[0])
        A = float(numeros[1])
        B = float(numeros[2])
        total = ((A+B)*5/2)*Q
        print("Size #{}:" .format(i+1))
        print("Ice Cream Used: {:.2f} cm2" .format(total))
    print("")
    T = int(input())
    quantidades.append(T)