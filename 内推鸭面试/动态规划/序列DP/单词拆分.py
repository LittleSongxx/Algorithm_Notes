s = input().strip()
word_dict = input().strip().split()

# 用 set 加快查找速度，比如判断某个单词是否在字典中
word_set = set(word_dict)

n = len(s)

min_len = min(len(word) for word in word_dict)
max_len = max(len(word) for word in word_dict)

# dp[i] 表示 s 的前 i 个字符能不能被拼出来
dp = [False] * (n + 1)

# 空字符串可以被拼出来，作为起点
dp[0] = True

# 枚举结尾位置 i
for i in range(min_len, n + 1):
    # 控制s[j:i] 的长度不会超过 max_len
    start = max(0, i - max_len)
    # 控制s[j:i] 的长度不会小于 min_len
    end = i - min_len
    # 枚举切分位置 j
    for j in range(start, end + 1):
        # 如果 s[0:j] 可以拼出来，并且 s[j:i] 是字典里的单词
        if dp[j] and s[j:i] in word_set:
            dp[i] = True
            break

print("true" if dp[n] else "false")
