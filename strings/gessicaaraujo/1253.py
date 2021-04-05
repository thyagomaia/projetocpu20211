qte = int(input())

for i in range(qte):
    texto = input()
    qte = int(input())
    t_decod = ''
    for l in texto:
        posicao = ord(l)-qte

        if(posicao < 65):
            t_decod += chr(91-(65-posicao))
        else:
            t_decod += chr(ord(l)-qte)
    print(t_decod)