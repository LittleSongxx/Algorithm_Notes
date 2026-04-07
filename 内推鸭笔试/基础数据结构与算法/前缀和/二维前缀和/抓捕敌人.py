n, A, B = map(int, input().split())
MAXC = 1000

# s[x][y] 先表示该点有多少敌人，后面原地变成二维前缀和
s = [[0] * (MAXC + 1) for _ in range(MAXC + 1)]

for _ in range(n):
    x, y = map(int, input().split())
    s[x][y] += 1  # 将输入的二维坐标(x, y)变成二维数组中具体的点s[x][y]

# 原地构建成二维前缀和
for i in range(1, MAXC + 1):
    for j in range(1, MAXC + 1):
        s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

ans = 0

for x1 in range(1, MAXC + 1):
    x2 = min(MAXC, x1 + A)
    for y1 in range(1, MAXC + 1):
        y2 = min(MAXC, y1 + B)

        cnt = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
        if cnt > ans:
            ans = cnt

print(ans)
