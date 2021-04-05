P, N = V = input().split()
P = int(P)
N = int(N)

V = input().split()                    
V = [int(i) for i in V]

#V
D = [0 for i in V]
acabou = 0

for i in range(0, N-1):
    D[i] = V[i+1] - V[i]
    if(D[i] > P or D[i] < -P):
        acabou = 1
        print("GAME OVER")
        break

if(acabou == 0):
    print("YOU WIN")