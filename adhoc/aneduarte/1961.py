# -*- coding: utf-8 -*-

dados = input().split(" ")
P = int(dados[0])
N = int(dados[1])

pulos = input().split(" ")
pulo = int(pulos[0])

for i in range(1, N, 1):
    pulo_seguinte = int(pulos[i])
    if (abs(pulo-pulo_seguinte) > P):
        print("GAME OVER")
        break
    pulo = pulo_seguinte
    if (i == N-1):
        print("YOU WIN")