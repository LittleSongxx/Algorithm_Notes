n = int(input())
matrix = [input().strip() for _ in range(n)]

pre = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        pre[i][j] = pre[i][j - 1] + pre[i - 1][j] - pre[i - 1][j - 1] + int(matrix[i - 1][j - 1])

# 枚举边长 size
for size in range(1, n + 1):
    total_cells = size * size

    # 如果总格子数是奇数，不可能 0 和 1 数量相等
    if total_cells % 2 == 1:
        print(0)
        continue

    need_ones = total_cells // 2
    count = 0

    # 枚举所有 size x size 子矩阵（类似卷积的滑动窗口）
    for x1 in range(1, n - size + 2):  # 右端点遍历到n+1时，左端点对应n+1 -size +1，即n-size+2
        for y1 in range(1, n - size + 2):
            x2 = x1 + size - 1
            y2 = y1 + size - 1

            # 用二维前缀和求这个子矩阵中 1 的个数
            ones = pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1]
            if ones == need_ones:
                count += 1
    print(count)
