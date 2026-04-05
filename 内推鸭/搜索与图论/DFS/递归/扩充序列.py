def dfs(n, k):
    if n == 1:
        return 1
    total = pow(2, n - 1) - 1
    center = total + 1
    if k == center:
        return n
    elif k < center:
        return dfs(n - 1, k)
    else:
        return dfs(n - 1, k - center)
    
n, k = map(int, input().split())
print(dfs(n, k))