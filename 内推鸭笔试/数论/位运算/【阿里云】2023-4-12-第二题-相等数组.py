n = int(input())
a = list(map(int, input().split()))
total_ops = 0

# 题目规定数字最大为 2^31 - 1，所以最多有 31 位二进制 (0 到 30)
for i in range(31):
    ones_count = 0

    # 统计所有数字在第 i 位上 1 的个数
    for num in a:
        if (num >> i) & 1:
            ones_count += 1

    # 0 的个数自然等于总数 n 减去 1 的个数
    zeros_count = n - ones_count

    # 贪心：这一位统一成 0 还是统一成 1？取操作次数较少的那个
    total_ops += min(ones_count, zeros_count)

print(total_ops)
