m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# top：上边界; bottom：下边界
top, bottom = 0, m - 1
# left：左边界; right：右边界
left, right = 0, n - 1

ans = []

while top <= bottom and left <= right:
    # 1. 左 -> 右
    for i in range(left, right + 1):
        ans.append(matrix[top][i])
    top += 1  # 上边界下移

    # 2. 上 -> 下
    for j in range(top, bottom + 1):
        ans.append(matrix[j][right])
    right -= 1  # 右边界左移

    # 3. 右 -> 左
    if top <= bottom:
        for k in range(right, left - 1, -1):
            ans.append(matrix[bottom][k])
        bottom -= 1  # 下边界上移

    # 4. 下 -> 上
    if left <= right:
        for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1  # 左边界右移
        
print(*ans)
