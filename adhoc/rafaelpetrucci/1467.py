while True:
    try:
        case = input().split()
        if case[0] == case[1] == case[2]:
            print('*')
        elif case[0] != case[1] == case[2]:
            print('A')
        elif case[0] == case[2] != case[1]:
            print('B')
        elif case[0] == case[1] != case[2]:
            print('C')
    except EOFError:
        break