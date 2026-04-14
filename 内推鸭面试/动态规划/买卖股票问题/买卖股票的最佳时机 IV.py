from math import inf

k = int(input())
prices = list(map(int, input().split()))
n = len(prices)

# 最多也就n//2次交易，k >= n // 2时相当于无限次交易，转换为II的做法
if k >= n // 2:
    ans = 0
    for i in range(1, n):
        ans += max(0, prices[i] - prices[i - 1])
    print(ans)
else:
    buy = [-inf] * (k + 1)
    sell = [0] * (k + 1)

    for p in prices:
        prev_buy = buy[:]
        prev_sell = sell[:]
        for t in range(1, k + 1):
            buy[t] = max(prev_buy[t], prev_sell[t - 1] - p)
            sell[t] = max(prev_sell[t], prev_buy[t] + p)

    print(sell[k])
