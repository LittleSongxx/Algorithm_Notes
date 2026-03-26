import math
from functools import reduce

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算数组 a 中所有元素的最大公约数 (GCD)。
    g = reduce(math.gcd, a)  # reduce：函数式编程工具，会对数组中的元素进行累积操作
    cnt = 0  # 需要的操作次数
    for i in range(n):
        cnt += (a[i] // g) - 1  # 切成n段需要n-1刀
    if cnt > k:
        print("NO")
    else:
        print("YES")
