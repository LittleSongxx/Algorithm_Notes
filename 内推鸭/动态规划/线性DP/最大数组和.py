n = int(input())
a = list(map(int, input().split()))

total = sum(a)

INF = 10 ** 30
min_sum = INF  # 全偶数合法区间中的最小子段和
cur = None  # 当前以当前位置结尾的最小子段和

for x in a:
    if x % 2 == 0:  # 只有偶数才能进入可选区间
        if cur is None:
            cur = x
        else:
            cur = min(x, cur + x)
        min_sum = min(min_sum, cur)
    else:
        cur = None  # 奇数把区间切断

# 如果没有合法区间，或者最优区间和 >= 0，就不操作
if min_sum == INF or min_sum >= 0:
    print(total)
else:
    print(total - min_sum // 2)
