s = input().strip()
n = len(s)

vowels = set("aeiou")
# 先求整个字符串的总和
total = 0
for ch in s:
    if ch in vowels:
        total += 1
    else:
        total -= 1

# 情况1：总和为0，任意切法都可以
if total == 0:
    print(n - 1)
else:
    # 情况2：总和不是偶数，不可能平分
    if total % 2 != 0:
        print(0)
    else:
        target = total // 2
        pre = 0
        ans = 0
        # 只能切在前 n-1 个位置
        for i in range(n - 1):
            if s[i] in vowels:
                pre += 1
            else:
                pre -= 1
            if pre == target:
                ans += 1
        print(ans)
