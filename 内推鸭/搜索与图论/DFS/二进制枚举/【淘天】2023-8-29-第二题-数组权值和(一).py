n = int(input())
nums = list(map(int, input().split()))

answer = 0

def dfs(index, current_sum, current_size):
    global answer

    if index == n:
        if current_size > 0 and current_sum >= 0:
            answer += current_size
        return

    # 不选 nums[index]
    dfs(index + 1, current_sum, current_size)

    # 选 nums[index]
    dfs(index + 1, current_sum + nums[index], current_size + 1)

dfs(0, 0, 0)
print(answer)
