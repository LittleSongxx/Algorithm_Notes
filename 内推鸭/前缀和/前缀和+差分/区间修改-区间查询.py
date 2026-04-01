n, m, q = map(int, input().split())
a = list(map(int, input().split()))

# diff[i] 表示增量数组的差分
diff = [0] * (n + 2)

# 处理 m 次区间修改
for _ in range(m):
    l, r, c = map(int, input().split())
    diff[l] += c
    diff[r + 1] -= c

# 通过对diff求前缀和，计算每个位置的总增量
add = [0] * (n + 1)
for i in range(1, n + 1):
    add[i] = add[i - 1] + diff[i]

# 计算加上增量后的新数组
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = a[i - 1] + add[i]

# 再对新数组求前缀和
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + b[i]

# 回答查询
for _ in range(q):
    l, r = map(int, input().split())
    print(pre[r] - pre[l - 1])