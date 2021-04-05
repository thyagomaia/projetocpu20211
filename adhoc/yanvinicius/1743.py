while True:

    try:

        X1,X2,X3,X4,X5 = map(int, input().split())

        Y1,Y2,Y3,Y4,Y5 = map(int, input().split())

        if (X1 != Y1 and X2 != Y2 and X3 != Y3 and X4 != Y4 and X5 != Y5):

            print("Y")

        else:

            print("N")

    except (EOFError):
       
        break