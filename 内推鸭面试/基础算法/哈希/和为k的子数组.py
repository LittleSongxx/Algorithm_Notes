from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = defaultdict(int)  # 不存在的值为int类型的空值，即0
cnt[0] = 1  # 前缀和 0 出现过 1 次

pre_sum = 0
ans = 0

for x in a:
    # 1. 先计算当前前缀和
    pre_sum += x

    # 2. 再判断之前是否有 pre_sum - k
    ans += cnt[pre_sum - k]

    # 3. 最后记录当前前缀和
    cnt[pre_sum] += 1

print(ans)
