n = int(input())
a = list(map(int, input().split()))

# 显式前缀和数组
pre = [0] * (n + 1)
for i in range(1, n + 1):
    pre[i] = pre[i - 1] + a[i - 1]

ans = float('inf')

for i in range(1, n):
    left = pre[i]
    right = pre[n] - pre[i]
    ans = min(ans, left * right)

print(ans)