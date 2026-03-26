"""
题目：矩阵填写者
给定 n×n 的字母矩阵，执行一次操作：
  选一个字母 ch 和一个位置 (r, c)，将第 r 行和第 c 列全部填上 ch（画十字架）。
求操作后 ch 在矩阵中的最大出现次数，以及达到该最大值的方案数。

核心公式：
  操作后总数 = 原有数量 + 十字架大小(2n-1) - 覆盖损失
  覆盖损失 = row_count[r] + col_count[c] - (交叉点本身是该字母 ? 1 : 0)
  目标：最小化覆盖损失
"""

import string


def solve():
    n = int(input())
    matrix = [input() for _ in range(n)]

    # 预处理：记录每个字母出现在哪些坐标
    coords = {ch: [] for ch in string.ascii_letters}
    """
        coords初始化为这样的字典：
        {
            'a': [],
            'b': [],
            'c': [],
            'd': [],
            # ... 其余50个字母也都是空列表 []
            'Z': []
        }
    """
    for r in range(n):
        for c in range(n):
            coords[matrix[r][c]].append((r, c))
    """
        经过预处理，coords变成这样：
        {
            'a': [(0,0), (0,2), (1,1), (2,0), (2,2)],
            'b': [(0,1), (1,0), (1,2), (2,1)],
            'c': [],
            'd': [],
            # ... 其余字母仍然是空列表
            'Z': []
        }
    """

    best_count = -1
    best_ways = 0
    cross_size = 2 * n - 1  # 十字架的大小

    for ch in string.ascii_letters:
        points = coords[ch]  # 该字母在矩阵中的所有坐标
        original = len(points)  # 初始时该字母在矩阵中的数量

        # ---- 矩阵中没有这个字母 ----
        # 损失为 0，放在任何位置效果一样
        if original == 0:
            count = cross_size  # 十字架覆盖后的总数
            ways = n * n  # 方案数
            if count > best_count:  
                best_count, best_ways = count, ways  # 更新最大值和方案数
            elif count == best_count: 
                best_ways += ways 
            continue  # 继续处理下一个字母

        # 第一步：统计每行、每列有多少个该字母
        row_count = [0] * n
        col_count = [0] * n
        for r, c in points: 
            row_count[r] += 1  # 统计每行有多少个该字母
            col_count[c] += 1  # 统计每列有多少个该字母

        # 第二步：找到行最小值和列最小值
        #   覆盖损失的下界 = min(行) + min(列)，记为 base_loss
        #   如果交叉点恰好是该字母，还能再省 1，损失变为 base_loss - 1
        min_row = min(row_count)
        min_col = min(col_count)
        base_loss = min_row + min_col

        # 第三步：统计有多少行/列恰好取到最小值
        rows_at_min = row_count.count(min_row)
        cols_at_min = col_count.count(min_col)
        # 满足 row_count[r] + col_count[c] == base_loss 的格子总数
        min_loss_pairs = rows_at_min * cols_at_min

        # 第四步：在该字母出现的坐标中，统计两类关键点
        #   perfect:      交叉点是该字母 且 行+列 == base_loss   → 损失 = base_loss - 1
        #   near_perfect: 交叉点是该字母 且 行+列 == base_loss+1 → 损失 = base_loss
        perfect = 0
        near_perfect = 0
        for r, c in points:
            rc_sum = row_count[r] + col_count[c]
            if rc_sum == base_loss:
                perfect += 1
            elif rc_sum == base_loss + 1:
                near_perfect += 1

        # 第五步：确定最小覆盖损失和对应方案数
        if perfect > 0:
            # 存在"完美点"：交叉点是该字母，行列重复计数可以减 1
            min_loss = base_loss - 1
            ways = perfect
        else:
            # 不存在完美点，最小损失只能是 base_loss，有两种来源：
            #   来源 1: 交叉点不是该字母，行+列 == base_loss → 损失 = base_loss - 0
            #   来源 2: 交叉点是该字母，行+列 == base_loss+1 → 损失 = (base_loss+1) - 1
            min_loss = base_loss
            ways = min_loss_pairs + near_perfect

        count = original + cross_size - min_loss

        # 更新全局最优
        if count > best_count:
            best_count, best_ways = count, ways
        elif count == best_count:
            best_ways += ways

    print(f"{best_count} {best_ways}")


T = int(input())
for _ in range(T):
    solve()
