N = int(input())

while(N != 0):
    for i in range(0,N):
        Q, A, B = input().split()
        Q = float(Q)
        A = float(A)
        B = float(B)

        X = "{0:.2f}".format(Q*(A + B)*5.0/2)
        I = i + 1
        print("Size #" + str(I) + ":")
        print("Ice Cream Used:", X, "cm2")
    print("")
    N = int(input())