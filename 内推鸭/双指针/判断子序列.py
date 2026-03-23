n, m = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

p1 = p2 = 0
while p1 < n and p2 < m:
    if list_a[p1] == list_b[p2]:
        p1 += 1
    p2 += 1
# 因为最后一次判断==后又让p1+1里一次，所以输出时是判断p1==n而不是n-1
print("Yes" if p1 == n else "No")
