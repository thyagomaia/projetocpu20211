a = input().split(" ")
b = input().split(" ")

for i in range(0, 5, 1):
    if (a[i] == b[i]):
        print("N")
        break
    if (i == 4):
        print("Y")