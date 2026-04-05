from random import choice

x = int(input())

# 预处理所有可能用到的 3 的幂
powers = []
p = 1
total = 0

while total < x:
    powers.append(p)
    total += p
    p *= 3

# 用来记录答案中的每一项（按从大到小保存）
path = []


def dfs(k, remain):
    if k < 0:
        return remain == 0
    p = powers[k]

    # 剩下的幂最多能凑出的绝对值
    max_smaller = (p - 1) // 2

    # 这一步是为了先从靠近remain的方向找答案
    if remain >= 0:
        choices = [1, 0, -1]
    else:
        choices = [-1, 0, 1]

    for choice in choices:
        new_remain = remain - choice * p

        # 后面的更小幂无论如何也凑不出这么大
        if abs(new_remain) > max_smaller and k > 0:
            continue
        if choice == 1:
            path.append("+" + str(p))
        elif choice == -1:
            path.append("-" + str(p))

        if dfs(k - 1, new_remain):
            return True

        # 回溯
        if choice != 0:
            path.pop()

    return False


dfs(len(powers) - 1, x)

answer = "".join(path)
if answer[0] == "+":
    answer = answer[1:]

print(answer)
