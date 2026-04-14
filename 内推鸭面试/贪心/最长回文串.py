from collections import Counter

s = input().strip()

cnt = Counter(s)
ans = 0
has_odd = False

for ch in cnt:
    ans += (cnt[ch] // 2) * 2  # 如果是偶数则不变，奇数则变成比他小1的偶数

    if cnt[ch] % 2 == 1:
        has_odd = True

# 有奇数个的，可以夹在中间
if has_odd:
    ans += 1

print(ans)
