from math import inf

prices = list(map(int, input().split()))

buy1 = -inf
sell1 = 0
buy2 = -inf
sell2 = 0

for p in prices:
    buy1 = max(buy1, -p)
    sell1 = max(sell1, buy1 + p)
    buy2 = max(buy2, sell1 - p)
    sell2 = max(sell2, buy2 + p)

print(sell2)
