n, m = map(int, input().split())

grid = []

for _ in range(n):
    grid.append(list(input().strip()))

directions = [
    (1, 0),  # 下
    (-1, 0),  # 上
    (0, 1),  # 右
    (0, -1)  # 左
]

ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            ans += 1
            stack = [(i, j)]
            grid[i][j] = '0'

            while stack:
                x, y = stack.pop()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    # 没越界且是陆地
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                        # 置为0，表示访问过的标记
                        grid[nx][ny] = '0'
                        stack.append((nx, ny))

print(ans)
