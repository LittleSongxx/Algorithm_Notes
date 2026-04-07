T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    min_edges = n - 1
    max_edges = n * (n - 1) // 2

    if min_edges <= m <= max_edges:
        print("YES")
    else:
        print("NO")