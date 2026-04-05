n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort()

res = -1
p1 = p2 = 0
while p1 < n and p2 < n:
    if list1[p1] <= list2[p2]:
        res = max(res, p1 + 1 + n - p2)
        p1 += 1
    else:
        p2 += 1

print(res)
