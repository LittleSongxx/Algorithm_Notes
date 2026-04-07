import math


def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):  # 枚举2~sqrt(x),看是否有x的因子
        if x % i == 0:
            return False
    return True


n = int(input())
if isprime(n):
    print("YES")
else:
    print("NO")
