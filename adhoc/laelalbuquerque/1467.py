while True:
    try:
        A,B,C = list(map(int,input().split()))

        if (A == B): 
            if (A == C) :
                print('*')
            else:
                print('C')
        elif (A == C) :
            print('B')
        else:
            print('A')
    except (EOFError):
        break