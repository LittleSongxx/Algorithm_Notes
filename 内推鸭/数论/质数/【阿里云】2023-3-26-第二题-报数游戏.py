from collections import deque

# 读取单行输入
n = int(input().strip())

# 特判：如果只有 1 个人，直接留下
if n == 1:
    print(1)
else:
    # 1. 极速埃氏筛，预处理 150000 以内的素数
    # 第 10000 个素数是 104729，所以 15万 的范围绝对够用
    MAX_VAL = 150000
    is_prime = [True] * (MAX_VAL + 1)
    is_prime[0] = is_prime[1] = False
    limit = int(MAX_VAL ** 0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            for i in range(p * p, MAX_VAL + 1, p):
                is_prime[i] = False

    # 2. 队列模拟游戏过程
    # 使用 deque (双端队列) 保证弹出队首和追加队尾的操作都是 O(1) 的极速
    q = deque(range(1, n + 1))
    current_number = 1  # 开始报数，从 1 开始
    while len(q) > 1:
        # 当前轮到的同学出列
        person = q.popleft()

        # 判断当前报的数是不是素数
        if is_prime[current_number]:
            # 是素数，该同学被淘汰，什么都不做，不用加回队列
            pass
        else:
            # 不是素数，安全！走到队尾重新排队
            q.append(person)

        # 准备下一次报数
        current_number += 1

    # 最终队列中剩下的唯一一人就是答案
    print(q[0])
