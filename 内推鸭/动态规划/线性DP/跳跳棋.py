n = int(input())
w = [0] + list(map(int, input().split()))
f = [0] * (n + 1)  # 跳到前i个格子的最大得分
f[1] = w[1]
for i in range(2, n + 1):
    f[i] = max(f[i - 2] + w[i], f[i - 1])  # 可以由第i-2个格子跳过来，也可以不跳到第i个格子
print(f[n])
