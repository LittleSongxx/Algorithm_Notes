prices = list(map(int, input().split()))

ans = 0
for i in range(1, len(prices)):
    # 只要今天比昨天涨了，那么这段上涨利润就一定可以赚到
    ans += max(0, prices[i] - prices[i - 1])

print(ans)
