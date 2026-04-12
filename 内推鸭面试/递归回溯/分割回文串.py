s = input().strip()
n = len(s)

# 判断是否是回文串
def check(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


ans = []
path = []


def dfs(start):
    if start == n:
        ans.append(path[:])
        return

    # 枚举从 start 开始的所有子串
    for end in range(start, len(s)):
        sub = s[start:end + 1] # 当前选择的子串
        if check(sub):
            path.append(sub)
            dfs(end + 1)
            path.pop()

dfs(0)

for i in ans:
    print(" ".join(i))

