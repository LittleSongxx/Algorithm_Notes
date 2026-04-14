prices = list(map(int, input().split()))

hold = -prices[0]
sold = 0
rest = 0

for p in prices[1:]:
    prev_hold, prev_sold, prev_rest = hold, sold, rest
    hold = max(prev_hold, prev_rest - p)
    sold = prev_hold + p
    rest = max(prev_rest, prev_sold)

print(max(sold, rest))
