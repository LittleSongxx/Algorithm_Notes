from math import inf

prices = list(map(int, input().split()))
n = len(prices)

ans = 0
min = inf
max = -inf
for i in range(n):
    if prices[i] < min:
        min