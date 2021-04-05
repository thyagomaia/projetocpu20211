N, M = input().split()
N = int(N)
M = int(M)

while(N != 0 and M != 0):
    V = []
    for i in range(0, N):
        Vaux = input().split()
        Vaux = [int(i) for i in Vaux]
        V.append(Vaux)

    Vt = list(map(list, zip(*V)))

    cond1 = 1
    cond2 = 0
    cond3 = 1
    cond4 = 0

    # 1 - Ninguém resolveu todos os problemas.
    for i in range(N):
        if(sum(V[i]) == M):
            cond1 = 0


    # 2 - Todo problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma).
    cont2 = 0
    for j in range(M):
        if(sum(Vt[j]) > 0):
            cont2 = cont2 + 1
        if(cont2 == M):
            cond2 = 1

    # 3 - Não há nenhum problema resolvido por todos.
    for j in range(M):
        if(sum(Vt[j]) == N):
            cond3 = 0


    #print("cond3 =",cond3)    
    # 4 - Todos resolveram ao menos um problema (não necessariamente o mesmo).        
    cont4 = 0
    for i in range(N):
        if(sum(V[i]) > 0):
            cont4 = cont4 + 1
        if(cont4 == N):
            cond4 = 1

    print(cond1 + cond2 + cond3 + cond4)
    N, M = input().split()
    N = int(N)
    M = int(M)