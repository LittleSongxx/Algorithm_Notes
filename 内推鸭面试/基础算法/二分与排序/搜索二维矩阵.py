m, n = map(int, input().split())

matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input())

left = 0
right = m * n - 1

found = False

while left <= right:
    mid = (left + right) // 2

    row = mid // n
    col = mid % n
    num = matrix[row][col]

    if num == target:
        found = True
        break
    elif num < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print("true")
else:
    print("false")
