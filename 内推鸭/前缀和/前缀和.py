def pre_sum(nums):
    n = len(nums)
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + nums[i - 1]
    return pre


n = int(input())
a = list(map(int, input().split()))
pre = pre_sum(a)
print(pre)
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(pre[r] - pre[l - 1])
