n = int(input())
nums = list(map(int, input().split()))

left = [1] * n
right = [1] * n

for i in range(1, n):
    for j in range(1, i):
        if nums[j] < nums[i]:
            left[i] = max(left[i], left[j] + 1)

for i in range(n - 1, 1, -1):
    for j in range(n - 1, i, -1):
        if nums[j] < nums[i]:
            right = max(right[i], right[j] + 1)

max_len = 0
for i in range(n):
    max_len = max(max_len, left[i] + right[i] - 1)
print(n - max_len)