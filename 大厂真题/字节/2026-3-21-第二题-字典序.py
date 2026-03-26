T = int(input())

for _ in range(T):
    parts = input().split()
    n = int(parts[0])
    A = parts[1]
    B = parts[2]
    # 如果 A 的字典序大于或等于 B，它们之间不可能有单词，直接输出 0
    if A >= B:
        print(0)
    else:
        # 计算 A 的 26 进制数值
        val_a = 0
        for char in A:
            val_a = val_a * 26 + (ord(char) - ord('a'))

        # 计算 B 的 26 进制数值
        val_b = 0
        for char in B:
            val_b = val_b * 26 + (ord(char) - ord('a'))

        # 计算两者之间的严格差值
        print(val_b - val_a - 1)