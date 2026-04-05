from collections import Counter

n, k = map(int, input().split())
s = str(input())


def check(cnts):
    for val in cnts.values():
        if val % 2 == 1:
            return False
    return True


res = 0
cnts = Counter()
l, r = 0, 0

for r in range(n):
    cnts[s[r]] += 1
    # 如果窗口大小>k了，左指针右移
    if r - l + 1 > k:
        cnts[s[l]] -= 1
        # if cnts[s[l]] == 0:
        #     del cnts[s[l]]
        l += 1
    # 如果窗口大小=k了，检查当前窗口内的字符出现次数
    if r - l + 1 == k:
        if check(cnts):
            res += 1
print(res)
