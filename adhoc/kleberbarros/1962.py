N = int(input())
v = [int(input()) for i in range(0,N)]

#v = 2015 - np.array(V)

for i in range(0, N):
    v[i] = 2015 - v[i]
    if(v[i] <= 0):
        print(abs(v[i] - 1), "A.C.")
    else:
        print(abs(v[i]), "D.C.")