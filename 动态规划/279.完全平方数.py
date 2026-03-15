from functools import lru_cache
from math import inf, isqrt

'''
   记忆搜索法（递归）
'''
@lru_cache
def dfs(i, target):
    if (i == 0):  # 最小的完全平方数是1，递归到0说明全部递归完了
        return inf if target else 0  # 递归完了还没有加到target，则返回inf表示失败，否则返回0
    if i * i > target:  # 超过了目标值
        return dfs(i - 1, target)  # 只能不选，递归到下一个
    return min(dfs(i - 1, target), dfs(i, target - i * i) + 1)


'''
   递推法
'''
N = 10000
n = isqrt(N) + 1
f = [[0] * (N + 1) for _ in range(n)]  # 创建一个二维数组，行数为isqrt(N)+1（额外包括0），列数为N+1（遍历0到N共n+1个数）
f[0] = [0] + [inf] * N  # f[0][0] = 0，f[0][1] 到 f[0][N] 都是 inf
for i in range(1, n):  # 遍历行，即遍历完全平方数，得到的是可以用的i个平方数
    for j in range(N + 1):  # 遍历列，即遍历0到N共这N+1个目标和
        if i * i > j:
            f[i][j] = f[i - 1][j]  # 只能不选
        else:
            f[i][j] = min(f[i - 1][j],  # 不选
                          f[i][j - i * i] + 1)  # 选
# 最终的结果保存的是使用前 i 个完全平方数（即 1², 2², ..., i²），凑成目标和 j 所需的最少完全平方数个数。

'''
   优化空间
'''
N = 10000
n = isqrt(N) + 1
f = [0] + [inf] * N
for i in range(1, n):
    for j in range(i * i, N + 1):  # j < i * i时递推式为f[j]=f[j]，直接跳过
        f[j] = min(f[j], f[j - i * i] + 1)  # 不选 vs 选


class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)  # 记忆搜索法


class Solution2:
    def numSquares(self, n: int) -> int:
        return f[isqrt(n)][n]  # 递推法


if __name__ == '__main__':
    s1 = Solution()
    s2 = Solution2()
    print(s1.numSquares(12))
    print(s2.numSquares(12))
