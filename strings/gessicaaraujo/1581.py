n = int(input())
while(n > 0):
    n -= 1
    l = []
    m = int(input())
    while(m > 0):
        m -= 1
        l.append(input())
    lang = l[0]
    for m in l:
        if m != lang:
            lang = 'ingles'
            break
    print(lang)