while True:
    try:
        lista = []
        a = input().split(" ")
        lista.append(a)
        if(a[0] != a[1] and a[0] != a[2]):
            print("A")
        elif(a[1] != a[0] and a[1] != a[2]):
            print("B")
        elif(a[2] != a[0] and a[2] != a[1]):
            print("C")
        else:
            print("*")

    except EOFError:
        break