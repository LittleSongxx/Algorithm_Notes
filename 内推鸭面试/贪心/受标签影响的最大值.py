from collections import defaultdict

n = int(input())
values = list(map(int, input().split()))
labels = list(map(int, input().split()))
numWanted, useLimit = map(int, input().split())

items = []

for i in range(n):
    items.append((values[i], labels[i]))

items.sort(reverse=True)

label_cnt = defaultdict(int)
ans = 0
chosen = 0

for value, label in items:
    if label_cnt[label] < useLimit:
        ans += value
        label_cnt[label] += 1
        chosen += 1
        if chosen == numWanted:
            break

print(ans)
