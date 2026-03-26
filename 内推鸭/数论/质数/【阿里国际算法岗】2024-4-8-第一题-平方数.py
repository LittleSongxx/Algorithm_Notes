import math

# 读取输入的数字 x
x = int(input().strip())
ops = 0

while True:
    # 1. 检查是否已经是完全平方数
    r = math.isqrt(x)
    if r * r == x:
        break

    # 2. 判断素数 & 找最小素因子
    is_prime = True
    spf = 0  # smallest prime factor

    if x == 2:
        is_prime = True
    elif x % 2 == 0:
        is_prime = False
        spf = 2
    else:
        # 只需遍历到根号 x 即可，步长为 2 跳过偶数
        limit = math.isqrt(x)
        for i in range(3, limit + 1, 2):
            if x % i == 0:
                is_prime = False
                spf = i
                break

    # 3. 根据判断结果执行操作
    if is_prime:
        x -= 1
    else:
        x //= spf

    ops += 1

print(ops)