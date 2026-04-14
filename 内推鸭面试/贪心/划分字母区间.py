s = input().strip()
n = len(s)

last_index = {}
for i in range(n):
    last_index[s[i]] = i

ans = []
start = 0
end = 0

for i in range(n):
    # 当前子串的最大右边界，即子串中每个字符最后一次出现的位置的最大值
    end = max(end, last_index[s[i]])

    # 如果走到了当前片段的最右边界，说明可以切分
    if i == end:
        ans.append(end - start + 1)
        start = i + 1

print(*ans)
