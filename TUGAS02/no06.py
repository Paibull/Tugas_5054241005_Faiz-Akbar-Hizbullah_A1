x,y=map(float,input('Masukkan koordinat (x, y)=> ').split(','))

if x == 0 and y == 0:
    print(f'({x},{y}) berada di titik asal')
elif x == 0:
    print(f'({x},{y}) berada di y-axis')
elif y == 0:
    print(f'({x},{y}) berada di di x-axis')
elif x > 0 and y > 0:
    print(f'({x},{y}) berada di kuadran 1')
elif x < 0 and y > 0:
    print(f'({x},{y}) berada di kuadran 2')
elif x < 0 and y < 0:
    print(f'({x},{y}) berada di kuadran 3')
elif x > 0 and y < 0:
    print(f'({x},{y}) berada di kuadran 4')

   



