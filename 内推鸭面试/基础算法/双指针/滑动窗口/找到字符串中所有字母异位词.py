s = input().strip()
p = input().strip()

n = len(s)
m = len(p)

if m > n:
    print()
else:
    p_count = [0] * 26
    window_count = [0] * 26

    # 统计p中每个字符出现个数
    for ch in p:
        p_count[ord(ch) - ord('a')] += 1

    # 统计 s 的第一个长度为 m 的窗口
    for i in range(m):
        window_count[ord(s[i]) - ord('a')] += 1

    ans = []

    # 第一个窗口
    if window_count == p_count:  # 比较 26 个位置是不是全都一样。
        ans.append(0)  # 起始位置0处匹配

    for i in range(m, n):
        # 加入右边新字符
        window_count[ord(s[i]) - ord('a')] += 1
        # 移出左边旧字符
        window_count[ord(s[i - m]) - ord('a')] -= 1

        # 当前窗口起点是 i - m + 1
        if window_count == p_count:
            ans.append(i - m + 1)

    print(*ans)