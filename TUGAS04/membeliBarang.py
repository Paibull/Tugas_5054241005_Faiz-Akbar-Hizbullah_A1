N, M = map(int, input().split())

P = list(map(int, input().split()))


maxSpend = []
for i in P:
    if i > 0:
        maxSpend.append(i)
if maxSpend == []: # BISA JUGA if not minSpend
    maxSpend.append(max(P))
    
C = list(map(int, input().split()))
minSpend = []
for j in C:
    if j < 0:
        minSpend.append(j)
if minSpend == []: # BISA JUGA if not minSpend
    minSpend.append(min(C))


hasil = sum(minSpend) - sum(maxSpend)
print(hasil)