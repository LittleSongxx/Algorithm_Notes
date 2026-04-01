n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = input().split()
    matrix.append(row)

# 三个二维前缀和
pre_x = [[0] * (m + 1) for _ in range(n + 1)]
pre_y = [[0] * (m + 1) for _ in range(n + 1)]
pre_z = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        ch = matrix[i - 1][j - 1]
        pre_x[i][j] = pre_x[i][j - 1] + pre_x[i - 1][j] - pre_x[i - 1][j - 1] + (1 if 'x' == ch else 0)
        pre_y[i][j] = pre_y[i][j - 1] + pre_y[i - 1][j] - pre_y[i - 1][j - 1] + (1 if 'y' == ch else 0)
        pre_z[i][j] = pre_z[i][j - 1] + pre_z[i - 1][j] - pre_z[i - 1][j - 1] + (1 if 'z' == ch else 0)


def get_sum(pre, x1, y1, x2, y2):
    return pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1]


q = int(input())
ans = []

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    kinds = 0
    if get_sum(pre_x, x1, y1, x2, y2) > 0:
        kinds += 1
    if get_sum(pre_y, x1, y1, x2, y2) > 0:
        kinds += 1
    if get_sum(pre_z, x1, y1, x2, y2) > 0:
        kinds += 1
    ans.append(str(kinds))

print('\n'.join(ans))
