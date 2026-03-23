n, k = map(int, input().split())
num = list(map(int, input().split()))
s = len(set(num))
print(s if s <= k else k)