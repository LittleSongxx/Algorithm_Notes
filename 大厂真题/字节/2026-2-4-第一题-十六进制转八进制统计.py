T = int(input())
hex_to_bin = {
    'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111'
}
bin_to_oct = {
    '000': 0, '001': 1, '010': 2, '011': 3,
    '100': 4, '101': 5, '110': 6, '111': 7
}

for _ in range(T):
    n = input()
    # 1. 拼接二进制字符串
    bin_str = "".join(hex_to_bin[c] for c in n)  # 将输入的16进制数拼接在一起转化成二进制，比如AA变成10101010

    # 2. 补齐前导0，使得二进制长度能被3整除
    rem = len(bin_str) % 3
    if rem != 0:
        bin_str = "0" * (3 - rem) + bin_str

    # 3. 每 3 个字符切一刀，统计八进制的词频
    counts = [0] * 8
    for j in range(0, len(bin_str), 3):
        chunk = bin_str[j:j + 3]
        counts[bin_to_oct[chunk]] += 1

    # 4. 找到最大频次
    max_cnt = max(counts)

    # 5. 收集出现次数等于 max_cnt 的数字
    # range(8) 本身就是 0-7 升序，天然满足题目要求的“按升序依次输出”
    res = [str(d) for d in range(8) if counts[d] == max_cnt]

    print(" ".join(res))
