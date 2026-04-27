from typing import Counter

s = input().strip()

cnt = Counter(s)

# 根据字符出现次数逆序排序
chars = sorted(cnt.keys(), key=lambda ch: cnt[ch], reverse=True)

ans = []

# 按个数拼接成完整字符串
for ch in chars:
    ans.append(ch * cnt[ch])

print(''.join(ans))
