while True:
    try:
        X = list(map(int, input().split(" ")))
        if X[0] != X[1] and X[1] == X[2]:
            print("A")
        elif X[0] == X[1] and X[1] != X[2]:
            print("C")
        elif X[0] == X[2] and X[0] != X[1]:
            print("B")
        else:
            print("*")
    except:
        break;