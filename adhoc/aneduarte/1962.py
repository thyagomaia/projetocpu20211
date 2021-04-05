# -*- coding: utf-8 -*-

N = int(input())
anos = []

for i in range(0, N, 1):
    T = int(input())
    if (T > 2015):
        ano = str(T-2015+1) + " A.C."
        anos.append(ano)
    elif(T < 2015):
        ano = str(2015-T) + " D.C."
        anos.append(ano)
    else:
        ano = "1 A.C."
        anos.append(ano)
        
for i in range(0, N, 1):
    print(anos[i])