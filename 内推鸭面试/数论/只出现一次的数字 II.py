nums = list(map(int, input().split()))

ans = 0

# 因为题目范围是 32 位整数，所以检查 0 到 31 位
for i in range(32):
    cnt = 0

    # 统计所有数字第 i 位上有多少个 1
    for x in nums:
        if (x >> i) & 1:
            cnt += 1

    # 如果 cnt 不能被 3 整除，说明答案的这一位是 1
    if cnt % 3 != 0:
        ans += 2 ** i

# 处理负数
if ans >= 2 ** 31:
    ans -= 2 ** 32

print(ans)
