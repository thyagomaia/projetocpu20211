x = input().split()  
x = [int(i) for i in x]

y = input().split()  
y = [int(i) for i in y]

if(x[0] == y[0] or x[1] == y[1] or x[2] == y[2] or x[3] == y[3] or x[4] == y[4]):
    print('N')
else:
    print('Y')