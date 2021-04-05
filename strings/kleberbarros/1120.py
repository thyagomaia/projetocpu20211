D, N = input().split()


while(D != '0' and N != '0'):
    tam = len(N)

    N = ["" if N[i] == D else N[i] for i in range(tam)]

    strg = ''.join(N)

    if(strg == '' or int(strg) == 0):
        print(0)
    else:
        print(int(strg))
    
    D, N = input().split()