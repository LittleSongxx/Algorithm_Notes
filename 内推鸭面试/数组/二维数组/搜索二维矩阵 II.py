m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
target = int(input())

i, j = 0, n - 1

# i从上往下遍历行，j从右往左遍历列
while i < m and j >= 0:
    if matrix[i][j] == target:
        print("true")
        break
    elif matrix[i][j] > target:  # 大了，往左遍历
        j -= 1
    else:  # 小了，往下遍历
        i += 1
else:
    print("false")