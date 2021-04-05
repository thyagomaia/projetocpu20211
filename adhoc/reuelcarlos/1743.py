numero = str(input())
numero1 = str(input())
contador = 0
for d in range(0, 9):
    if numero[d] == numero1[d]:
        contador += 1
if contador == 4:
    print('Y')
else:
    print('N')