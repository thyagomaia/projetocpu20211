while True:
    try:
        entrada = int(input())
        while (entrada):
            diferenca = int(input())
            diferenca = 2015 - diferenca 
            if(diferenca < 1):
                diferenca = abs(diferenca-1)
                print("%i A.C." %diferenca)
            else:
                print("%i D.C." %diferenca)
            entrada -=1
                
    except (EOFError):
        break