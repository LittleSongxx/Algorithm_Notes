n = int(input())
boxes = []

for _ in range(n):
    l, w, h = map(int, input().split())
    boxes.append((l, w, h))  # 每次追加一行

boxes.sort()

dp = [0] * n

for i in range(n):
    dp[i] = boxes[i][2]  # 每一层最高的
    for j in range(i):
        # 上面层的三维都比当前层小
        if boxes[j][0] < boxes[i][0] and boxes[j][1] < boxes[i][1] and boxes[j][2] < boxes[i][2]:
            dp[i] = max(dp[i], dp[j] + boxes[i][2])

print(max(dp))
