n, q = map(int, input().split())
a = list(map(int, input().split()))

def pre_num(nums):
    n = len(nums)
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + nums[i - 1]
    return pre

pre = pre_num(a)
for _ in range(q):
    l, r = map(int, input().split())
    print("YES" if (pre[r] - pre[l - 1]) % 3 == 0 else "NO")