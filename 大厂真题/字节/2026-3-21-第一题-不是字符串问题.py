T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    s = input().strip()
    # 使用集合来存储生成的不同字符串，自动去重
    unique_f_strings = set()

    # 计算前一半的字符数量
    k = x // 2

    # 遍历所有长度为 x 的子串
    for i in range(n - x + 1):
        t = s[i: i + x]

        # 第一部分：前 k 个字符，从小到大排序
        part1 = "".join(sorted(t[:k]))

        # 第二部分：整串，从大到小排序
        part2 = "".join(sorted(t, reverse=True))

        # 第三部分：剩余字符，从小到大排序
        part3 = "".join(sorted(t[k:]))

        # 拼接三部分并加入集合
        f_t = part1 + part2 + part3
        unique_f_strings.add(f_t)

    # 集合的长度即为不同新字符串的数量
    print(len(unique_f_strings))
