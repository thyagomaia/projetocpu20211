while(True):
    try:
        cont = 0    #contador
        strg = ""   #string final
        entrada = input()   #string auxiliar (linha)
        entrada = entrada.lower()   #mudando para minusculo

        for i in range(len(entrada)):
            if(entrada[i] == ' '):
                strg += entrada[i]  #concatenando espacos (se houverem)
            elif(cont == 0):    #o primeiro caracter deve ser maiusculo
                strg += entrada[i].upper()  #mudando para maiusculo e adiciona na string
                cont += 1   #incrementa contador
            elif(cont == 1):  #se o contador for positivo
                strg += entrada[i] #adiciona minusculo na string
                cont -= 1

        print(strg)
    except EOFError:
        break