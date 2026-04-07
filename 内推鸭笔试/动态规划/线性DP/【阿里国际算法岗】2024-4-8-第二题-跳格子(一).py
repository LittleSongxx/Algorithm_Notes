n = int(input())
a = [0] + list(map(int, input().split()))
b = [1, 1]  # 斐波那契数列
while b[-1] <= n:  # 构建斐波那契步长
    b.append(b[-1] + b[-2])
m = len(b)
f = [float('-inf')] * (n + 1)  # 由于有负奖励，所以初始化为-inf而非0
f[1] = a[1]
for i in range(2, n + 1):
    for j in range(1, m):
        k = i - b[j]  # 记录上一步从哪来
        if k < 0: break  # k<0说明这一步选的step太大了，超过了剩余可选范围
        f[i] = max(f[i], f[k] + a[i])
print(f[n])
