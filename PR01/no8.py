import math
newFlush=2 # 2L/flush
oldFlush=15 # 15L/flush
toiletCost=150 # cost/toilet (USD)
toiletPerPerson=3 # 3 person/toilet
dailyFlush=14 # 14 flush/day

population=int(input('Masukkan jumlah populasi =>'))

totalToilet=math.ceil(population/3)
costOfTotalToilet=totalToilet*toiletCost
costOfOldFlush= oldFlush * dailyFlush * totalToilet
costOfNewFlush= newFlush * dailyFlush * totalToilet

savedWater=costOfOldFlush-costOfNewFlush

print(f'Dengan populasi {population} orang, mengganti toilet yang lama dengan yang baru bisa menghemat {savedWater} liter/hari \ndengan biaya ${costOfTotalToilet:.0f} USD untuk membangun {totalToilet:.0f} toilet baru')