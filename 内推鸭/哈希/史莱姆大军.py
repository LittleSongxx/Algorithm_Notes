n = int(input())
a = [0] + list(map(int, input().split()))
pos = [i for i in range(n + 1)]
for t in range(1, n + 1):
    st = set()
    for i in range(1, n + 1):
        if a[i] == 1:  # 向右移动
            pos[i] += 1
        else:  # 向左移动
            pos[i] -= 1
        if 1 <= pos[i] <= n:
            st.add(pos[i])  # 没越界的
    print(n - len(st), end=' ')
