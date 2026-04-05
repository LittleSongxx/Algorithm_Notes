def pre_sum(matrix, n, m):
    pre = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + matrix[i][j]

    return pre


n, m, q = map(int, input().split())

# matrix 用 1 下标
matrix = [[0] * (m + 1)]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    matrix.append(row)

pre = pre_sum(matrix, n, m)

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans = pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1]
    print(ans)
