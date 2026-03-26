n = int(input())
w = list(map(int, input().split()))

max_len = 1
curr_len = 1
for i in range(1, n):
    if w[i] <= w[i - 1]:
        curr_len = 1
    else:
        curr_len += 1
    max_len = max(max_len, curr_len)
print(max_len)
