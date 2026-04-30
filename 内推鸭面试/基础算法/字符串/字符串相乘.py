num1 = input().strip()
num2 = input().strip()

if num1 == "0" or num2 == "0":
    print("0")
else:
    m = len(num1)
    n = len(num2)

    res = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            x = int(num1[i])
            y = int(num2[j])

            mul = x * y

            p1 = i + j  # 保存进位
            p2 = i + j + 1  # 保存结果位

            total = mul + res[p2]  # 相乘结果加上原本的数

            res[p2] += total % 10  # 当前结果位
            res[p1] += total // 10  # 进位

    # 由于一开始直接开了m+n个位置，这是可能的最大结果位数
    # 但真正相乘结果可能达不到这么多位置，res前面会有前导0，去除掉
    index = 0
    while index < len(res) and res[index] == 0:
        index += 1

    ans  = ''.join(map(str, res[index:]))

    print(ans)