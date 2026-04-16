s = input().strip()
n = len(s)

start = 0
max_len = 1


def expand(left, right):
    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1
    # left -= 1，right += 1之后才退出while，所以return时回溯一步
    return left + 1, right - 1


for i in range(n):
    # 奇数长度回文
    l1, r1 = expand(i, i)
    len1 = r1 - l1 + 1

    if len1 > max_len:
        start = l1
        max_len = len1

    # 偶数长度回文
    l2, r2 = expand(i, i + 1)
    len2 = r2 - l2 + 1
    if len2 > max_len:
        start = l2
        max_len = len2

print(s[start:start + max_len])
