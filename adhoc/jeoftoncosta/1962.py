N = int(input())
anos = []
for i in range(N):
    i = int(input())
    anos.append(i)

for ano in anos:
    if ano>2015:
        T = (ano - 2015)+1
        print(T,"A.C.")
    elif ano<2015:
        T = (ano - 2015)*(-1)
        print(T,"D.C.")
    else:
        T= (ano-2015)+1
        print(T,"A.C.")