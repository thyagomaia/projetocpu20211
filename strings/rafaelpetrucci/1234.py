while True:
    try:
        frase = list(input())
        total = len(frase)
        count = 0
        for i in range(total):
            if frase[i] == ' ':
                continue
            if count % 2 == 0:
                frase[i] = frase[i].upper()
            else:
                frase[i] = frase[i].lower()
            count += 1
        frase = "".join(frase)
        print(frase)
    except EOFError:
        break