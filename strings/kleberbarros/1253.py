N = int(input())

for i in range(N):
    strg = input()
    n = int(input())

    strgv = [ord(i)-64 for i in strg]

    for i in range(len(strg)):
        strgv[i] = chr((strgv[i] - n) % 26 + 64)
        if(strgv[i] == '@'):
            strgv[i] = 'Z'

    strg = ''.join(strgv)
    print(strg)