prices = list(map(int, input().split()))

min_price = prices[0]
ans = 0

for p in prices:
    min_price = min(min_price, p)
    ans = max(ans, p - min_price)

print(ans)
