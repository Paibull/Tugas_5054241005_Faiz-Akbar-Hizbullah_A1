N, K = map(int, input().split())

A = list(map(int, input().split()))

count = 0
for x in range(N):
    if A[x] <= K:
        count+=1

print(count)