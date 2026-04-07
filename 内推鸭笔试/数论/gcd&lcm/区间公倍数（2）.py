# 计算区间[1,i]中有多少数字是a的倍数
def find(i, a):
    return i // a  # a 的倍数刚好是每隔 a 个数出现一次。因此，i // a 得到的就是a的倍数的个数


# 辗转相除法求最大公约数
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


# 计算在区间[l,r]中有多少数字是a或b的倍数
def query(l, r, a, b):
    a_cnt = find(r, a) - find(l - 1, a)  # 区间l到r之间a的倍数的个数
    b_cnt = find(r, b) - find(l - 1, b)  # 区间l到r之间b的倍数的个数
    ab = a * b // gcd(a, b)  # a和b的最小公倍数
    ab_cnt = find(r, ab) - find(l - 1, ab)  # 区间l到r之间ab公共倍数的个数
    return a_cnt + b_cnt - ab_cnt  # 容斥原理


q = int(input())
for _ in range(q):
    a, b, l, r = map(int, input().split())
    print(query(l, r, a, b))
