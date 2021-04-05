while True:
    try:
        sentence = str(input())
        maiu = False
        minusculo = True
        espaco = False
        for c in range(0, len(sentence)):
            if sentence[c] == ' ':
                print(' ', end='')
                espaco = True
            elif not maiu or not ' ':
                if not espaco:
                    print(sentence[c].upper(), end='')
                    maiu = True
            elif maiu or not ' ':
                if not espaco:
                    print(sentence[c].lower(), end='')
                    maiu = False
            espaco = False
        print('')
    except EOFError:
        break