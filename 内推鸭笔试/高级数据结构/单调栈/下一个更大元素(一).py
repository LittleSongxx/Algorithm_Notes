n = int(input())
a = list(map(int, input().split()))

result = [-1] * n  # 默认所有答案为 -1
stack = []  # 栈，存放元素索引

for i in range(n):
    while stack:  # 找找看当前元素会是哪些栈中元素的目标元素（第一个比他们大的）
        if a[i] > a[stack[-1]]:  # 当前栈顶元素符合
            top_index = stack.pop()  # 出栈
            result[top_index] = i  # 记录下标i的元素是第一个比 a[top_index] 大的元素
        else:
            break
    stack.append(i)  # 当前元素都没有栈中元素大，把他也入栈。由此也就构成了单调递减的栈了
print(*result)
