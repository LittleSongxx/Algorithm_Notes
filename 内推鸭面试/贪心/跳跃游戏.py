nums = list(map(int, input().split()))

max_reach = 0
n = len(nums)

for i in range(n):
    # 如果当前位置都到不了，说明后面更不可能到
    if i > max_reach:
        print("false")
        break
    # 更新当前最远能到达的位置
    max_reach = max(max_reach, i + nums[i])

    # 如果已经能到最后一个位置，直接结束
    if max_reach >= n - 1:
        print("true")
        break
