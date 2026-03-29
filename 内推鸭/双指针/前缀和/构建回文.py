t = int(input())

for case_id in range(1, t + 1):
    n, q = map(int, input().split())
    s = input().strip()

    # pre[i][j] 表示前 i 个字符中，第 j 个字母出现了多少次
    pre = [[0] * 26 for _ in range(n + 1)]

    # 计算二维前缀和
    for i in range(1, n + 1):
        for j in range(26):
            # 先继承前 i - 1 个字符的统计结果
            pre[i][j] = pre[i - 1][j]

        # 当前字符对应的字母编号
        idx = ord(s[i - 1]) - ord('A')

        # 当前字母出现次数加 1
        pre[i][idx] += 1

    ans = 0  # 统计有多少个询问可以回答“是”

    for _ in range(q):
        l, r = map(int, input().split())

        odd_count = 0  # 区间内出现奇数次的字母种类数

        for j in range(26):
            cnt = pre[r][j] - pre[l - 1][j]
            if cnt % 2 == 1:
                odd_count += 1

        if odd_count <= 1:
            ans += 1

    print(f"Case #{case_id}: {ans}")
