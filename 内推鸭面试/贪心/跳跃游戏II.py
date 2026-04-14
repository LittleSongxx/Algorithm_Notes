nums = list(map(int, input().split()))
n = len(nums)

if n == 1:
    print(0)
else:
    steps = 0
    end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        # 到达了此次最远的边界，不得不跳了
        if i == end:
            steps += 1
            end = farthest  # 表示用 steps 次跳跃最远能到哪里
            # 用 steps 次跳跃最远已经能到达终点
            if end >= n - 1:
                break

    print(steps)
