fee = int(input())
prices = list(map(int, input().split()))

buy = -prices[0]
sell = 0

for p in prices[1:]:
    old_buy, old_sell = buy, sell
    buy = max(old_buy, old_sell - p)
    sell = max(old_sell, old_buy + p - fee)

print(sell)
