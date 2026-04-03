n = int(input())
a = list(map(int, input().split()))
res = [-1] * n

def get_weight(x):
    weight = 0
    while x:
        weight += x % 16
        x = x // 16
    return weight

stack = []
for i in range(n):
    while stack:
        if get_weight(a[i]) > get_weight(a[stack[-1]]):
            top_index = stack.pop()
            res[top_index] = i
        else:
            break
    stack.append(i)
print(*res)