n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

ans = 1
start = 0

# 直接用 i 作为遍历的指针,因为两个数组是同步遍历的
for i in range(1, n):
    # 同步比较 list1 和 list2 当前关卡和上一关卡的差值
    if list1[i] - list1[i - 1] == list2[i] - list2[i - 1]:
        # 更新最大长度，此时当前索引 i 减去 起点 start，再加上 1 就是当前有效关卡数
        ans = max(ans, i - start + 1)
    else:
        # 如果差值不等，说明连续中断了，将起点重置为当前关卡 i
        start = i

print(ans)
