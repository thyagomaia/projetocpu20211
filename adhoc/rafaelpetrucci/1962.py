number = int(input())
for _ in range(number):
    year = int(input())
    result = 2015 - year
    if result < 0:
        result = (result * -1) + 1
        print('{} A.C.'.format(result))
    elif result == 0:
        result += 1
        print('{} A.C.'.format(result))
    elif result > 0:
        print('{} D.C.'.format(result))