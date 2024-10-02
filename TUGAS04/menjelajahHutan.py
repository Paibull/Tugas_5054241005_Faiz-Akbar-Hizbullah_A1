r, c, N = map(int, input().split())

tambang = [list(map(int, input().split())) for i in range(r)]

move = input()

posXY = [0,0]
gold = tambang[posXY[0]][posXY[1]]
wrongMove = 0
for step in move:
    if step == 'R' and 0 <= posXY[1] + 1 < c:
        posXY[1] += 1
        gold += tambang[posXY[0]][posXY[1]] + 3

    elif step == 'L' and 0 <= posXY[1] - 1 < c:
        posXY[1] -= 1
        gold += tambang[posXY[0]][posXY[1]] - 2

    elif step == 'U' and 0 <= posXY[1] - 1 < r:
        posXY[0] -= 1
        gold += tambang[posXY[0]][posXY[1]] + 3

    elif step == 'D' and 0 <= posXY[1] + 1 < r:
        posXY[0] += 1
        gold += tambang[posXY[0]][posXY[1]] - 2
    else:
        wrongMove+=1
    
print(gold)
if wrongMove > 0:
    print('gerakanmu salah bung! ')