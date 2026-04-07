n = int(input())

# 边界情况：0 和 1 都不包含质数
if n < 2:
    print(0)
else:
    # 2. 假设 0 到 n 全是质数 (True)
    is_prime = [True] * (n + 1)

    # 明确 0 和 1 不是质数
    is_prime[0] = False
    is_prime[1] = False

    # 3. 开始执行埃氏筛逻辑
    # 外层循环只需要遍历到根号 n 即可 (即 p * p <= n)
    limit = int(n ** 0.5)
    for p in range(2, limit + 1):
        # 如果 p 没有被前面的数划掉，那它就是质数
        if is_prime[p]:

            # 4. 把 p 的倍数全部划掉 (置为 False)
            # 从 p*p 开始划，步长为 p(p的倍数)，一直划到 n
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # 5. 统计剩下的 True 的个数
    # sum() 函数会自动把 True 当成 1，False 当成 0 进行累加
    print(sum(is_prime))
