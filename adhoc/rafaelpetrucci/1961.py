case = list(map(int, input().split()))
pipes = list(map(int, input().split()))
count = 0
for i in range(case[1] - 1):
    if abs(pipes[i] - pipes[i + 1]) > case[0]:
        count += 1
        print('GAME OVER')
        break
if count == 0:
    print('YOU WIN')