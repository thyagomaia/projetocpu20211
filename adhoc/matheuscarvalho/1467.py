while True:
    try:
        a, b, c = list(map(int,input().split()))
       
        if a == b == c :
            print("*")
        else:
            if a == b != c :
                print("C")
            else:
                if a == c != b :
                    print("B")
                else:
                    print("A")
    except  EOFError :
        break