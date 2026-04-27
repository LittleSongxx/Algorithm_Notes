from collections import defaultdict

n = int(input())
words = input().split()

# key为按字符ASCII大小排序后的字符串，value是原字符串
# 例如"eat"存入后变成 key="aet", value="eat"
mp = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    mp[key].append(word)

# 经过上面的for循环，此时mp中的values就是题目要求的字母异位词分组
for group in mp.values():
    print(' '.join(group))
