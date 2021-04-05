while True:

    try:

        a,b,c,d,e = map(int, input().split())

        v,w,x,y,z = map(int, input().split())

        if (a != v and b != w and c != x and d != y and e != z):

            print("Y")

        else:

            print("N")

    except (EOFError):
       
        break