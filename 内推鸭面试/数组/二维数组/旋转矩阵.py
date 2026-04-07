n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 转置
for i in range(n):
    for j in range(i + 1, n):  # 主对角线右上方的区域，不包括对角线
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 翻转每一行
for i in range(n):
    matrix[i].reverse()

for row in matrix:
    print(*row)