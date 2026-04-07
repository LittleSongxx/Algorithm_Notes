import sys

s = sys.stdin.readline().rstrip('\n')

window = set()  # 记录当前窗口中的字符，set判断是否存在某个元素只需要O(1)，list要O(n)
left = 0  # 窗口左边界
ans = 0

for right in range(len(s)):
    while s[right] in window:
        window.remove(s[left])
        left += 1
    window.add(s[right])
    ans = max(ans, right - left + 1)

print(ans)
