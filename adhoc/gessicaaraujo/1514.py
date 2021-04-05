# -*- coding: utf-8 -*-

while True:
  
    n, m = input().split() #entrada de dados
    n, m = int(n), int(m) #transf. em inteiro
    if n == m == 0:
        break
    verdade = 4 #n.vdds
    concorrente = []
    for i in range(n):
        concorrente.append([int(x) for x in input().split()])

    # verdade 1
    for i in range(n):
        p = concorrente[i].count(1)
        if p == m:
            verdade -= 1
            break

    # verdade 2
 
    problema = [0] * m
    for i in range(n):
        for j in range(m):
            if concorrente[i][j] == 1:
                problema[j] += 1
    if problema.count(0) > 0:
        verdade -= 1

    # verdade 3

    for j in range(m):
        if problema[j] == n:
            verdade -= 1
            break

    # verdade 4

    for i in range(n):
        p = concorrente[i].count(0)
        if p == m:
            verdade -= 1
            break

    print(verdade)