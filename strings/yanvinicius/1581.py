s_List = []
x = 0
z = 0

N = int(input())

while x < N:

    K = int(input())

    while z < K:

        S = input()        
        s_List.append(S)
        z += 1

    if all(S == s for s in s_List):

        print(S)
            
    else:

        print("ingles")
        
    s_List.clear()

    S = None

    z = 0
    x += 1