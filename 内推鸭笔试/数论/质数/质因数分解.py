import math

x = int(input().strip())
limit = math.isqrt(x)

# 从 2 开始，每次加 1（步长为 1：2, 3, 4, 5, 6...）
for i in range(2, limit + 1):
    if x % i == 0:
        count = 0
        while x % i == 0:
            count += 1
            x //= i
        print(f"{i} {count}")

# 如果最后 x 没有被除到 1，说明剩下的 x 本身就是一个大于原根号的质数
if x > 1:
    print(f"{x} 1")
