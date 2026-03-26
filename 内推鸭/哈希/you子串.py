from collections import Counter

s = input()
cnts = Counter(s)  # 统计每个字符出现的次数
num = min(cnts['y'], cnts['o'], cnts['u'])
cnts['y'] -= num
cnts['o'] -= num
cnts['u'] -= num
res = ''
res += 'you' * num
for ch, count in cnts.items():
    res += ch * count
print(res)
