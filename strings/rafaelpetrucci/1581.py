number = int(input())
for _ in range(number):
    linhas = int(input())
    lingua = []
    for _ in range(linhas):
        lingua.append(input())
    lingua.sort()
    if lingua[0] == lingua[-1]:
        print(lingua[0])
    else:
        print('ingles')