x1, y1 = map(float,input('Masukkan koordinat "x1 y1" => ').split())
x2y2 = list(map(float,input('Masukkan koordinat "x2 y2" => ').split()))
x2=x2y2[0]
y2=x2y2[1]

xmid=(x1+x2)/2
ymid=(y1+y2)/2
gradien=(y2-y1)/(x2-x1)

perpenBisector = -1/gradien

b=ymid-perpenBisector*xmid

print(f'Koordinatnya adalah {x1}, {y1} dan {x2}, {y2}')
print(f'Garis bagi tegak lurus untuk garis ini adalah y = {perpenBisector}x + {b}')