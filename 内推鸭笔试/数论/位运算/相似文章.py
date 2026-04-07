from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
# 关键点：如果a ^ b = k，则有a ^ k = b及b ^ k = a
mp = defaultdict(int)  # 统计数组中的元素出现次数
ans = 0
for i in range(n):
    mp[a[i]] += 1  # 将当前元素加入字典
    target = a[i] ^ k
    ans += mp[target]  # 与当前元素匹配的是target，其个数为mp[target]
print(ans)