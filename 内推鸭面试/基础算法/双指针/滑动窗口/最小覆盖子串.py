from collections import defaultdict

s = input().strip()
t = input().strip()

need = defaultdict(int)
# 统计分别需要每个字符的个数
for ch in t:
    need[ch] += 1

window = defaultdict(int)

left = 0
valid = 0
start = 0
min_len = float('inf')

for right in range(len(s)):
    ch = s[right]
    if ch in need:
        window[ch] += 1
        if window[ch] == need[ch]:
            valid += 1  # 符合的个数+1

    # 只要当前窗口已经满足要求，就不停尝试从左边缩小，直到刚好不能再缩为止。
    while valid == len(need):
        curr_len = right - left + 1
        if curr_len < min_len:
            min_len = curr_len
            start = left

        remove_ch = s[left]
        if remove_ch in need:  # 当前字符是匹配项
            if window[remove_ch] == need[remove_ch]:  # 敲好够数，删不得
                # 若删了则valid就得-1，而这里-1之后可能就会使下一次的while不成立，则min_len永远停留在上一轮的最小长度
                valid -= 1
            window[remove_ch] -= 1  # 移除窗口最左边元素
        left += 1

# 输出答案
if min_len == float('inf'):
    print("")
else:
    print(s[start:start + min_len])
