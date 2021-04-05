def entry():

    P, N = map(int,input().split())
    
    X = input().split()
    
    X_list = list(X)

    for i in range(len(X_list)):

        X_list[i] = int(X_list[i])


    return P, N, X


def verify(a,b,p):

    if abs(int(a) - int(b)) > p:
        
        return True
    
    else:
    
        return False


def main():


    P, N, X = entry()
    
    a = False
    
    for i in range(N-1):
    
        a = verify(X[i], X[i+1], P)
    
        if a == True:
    
            print('GAME OVER')
    
            break
    
    if a == False:
    
        print('YOU WIN')


main()