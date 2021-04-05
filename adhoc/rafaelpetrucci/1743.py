conector_A = list(map(int, input().split()))
conector_B = list(map(int, input().split()))
resultado = 0
for i in range(5):
    if conector_A[i] == conector_B[i]:
        resultado += 1
        print('N')
        break
if resultado == 0:
    print('Y')