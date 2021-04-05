N = int(input())
strgv = [input().replace(',', '').replace(' ', '') for i in range(N)]

alfav = [0]*N

for i in range(N):
    alfav[i] = len(set(strgv[i]))

for i in range(N):
    if(alfav[i]==26):
        print('frase completa')
    elif(alfav[i] >= 13):
        print('frase quase completa')
    else:
        print('frase mal elaborada')