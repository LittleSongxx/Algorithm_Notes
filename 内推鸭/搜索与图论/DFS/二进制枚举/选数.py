n, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0


def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def dfs(index, chosen_count, current_sum):
    global answer

    # 选满 k 个，检查是否为素数和
    if chosen_count == k:
        if is_prime(current_sum):
            answer += 1
        return

    # 数字用完了
    if index == n:
        return

    # 剪枝：剩下的数不够选满 k 个
    if chosen_count + (n - index) < k:
        return

    # 1. 不选当前数
    dfs(index + 1, chosen_count, current_sum)

    # 2. 选当前数
    dfs(index + 1, chosen_count + 1, current_sum + nums[index])


dfs(0, 0, 0)
print(answer)
