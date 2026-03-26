from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


s = input()
mp = {}
# 统计每个字符出现的频次
for ch in s:
    if ch in mp:
        mp[ch] += 1
    else:
        mp[ch] = 1

# 对mp中的每个元素做gcd，找出频次的最大公约数
g = reduce(gcd, mp.values())

# 构造基础循环节
res = ""
for i in range(26):
    ch = chr(ord('a') + i) # python不能直接写 'a' + i
    if ch in mp:
        res += ch * (mp[ch] // g)

# 优化点 4：利用 Python 的字符串乘法特性，直接输出重复 g 次的结果
print(res * g)
