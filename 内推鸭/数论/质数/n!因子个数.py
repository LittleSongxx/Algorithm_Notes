n = int(input().strip())
MOD = 10 ** 9 + 7

# 1. 埃氏筛法预处理 2 到 n 的所有质数
# is_prime[i] 为 True 表示 i 是质数
is_prime = [True] * (n + 1)
primes = []  # 记录每个质因数

for p in range(2, n + 1):
    if is_prime[p]:
        primes.append(p)
        # 埃氏筛法，将质数 p 的倍数都标记为非质数
        for i in range(p * p, n + 1, p):
            is_prime[i] = False

# 2. 计算因子个数
ans = 1
for p in primes:  # 遍历所有质因数p
    count = 0  # 记录各个质因数的质数a
    temp = n

    # 用勒让德定理求各个质因数的指数
    # 利用 temp // p 可以避免计算 p 的高次幂，优化速度并防止溢出
    while temp > 0:
        count += temp // p
        temp //= p  # 由于下一次要计算temp/p^2，为避免计算平方，这里先用temp除一次p，下次遍历就只需要除一次p了

    # 根据约数个数定理累乘，并取模（题目要求）
    ans = (ans * (count + 1)) % MOD

# 输出结果
print(ans)
