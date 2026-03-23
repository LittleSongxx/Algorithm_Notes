# 1. 使用最基础的 input() 读取一行输入，并去掉两边多余的空格
s = input().strip()

# 如果输入为空或者只是个空括号，直接返回
if not s or s == "[]":
    print("[]")

# 2. 脱掉最外层的左右括号 '[' 和 ']'
s = s[1:-1]

# 3. 按逗号切分成一个个元素字符串
tokens = s.split(',')

stack = []  # 用来存储合并后的结果，格式为 [ [val, count], ... ]

for token in tokens:
    # 去除元素两端的空格
    token = token.strip()
    if not token:
        continue

    # 4. 解析当前元素的值 (val) 和数量 (count)
    if '(' in token:
        idx = token.index('(')
        val = int(token[:idx])
        count = int(token[idx + 1:-1])  # 提取括号里的数字
    else:
        val = int(token)
        count = 1

    # 5. 合并逻辑：只对比栈顶（最后一个元素）是不是和当前值相邻且相等
    if stack and stack[-1][0] == val:
        stack[-1][1] += count  # 数量累加
    else:
        stack.append([val, count])  # 作为新元素入栈

# 6. 重新格式化并输出
res_strs = [f"{v}({c})" for v, c in stack]
print(f"[{','.join(res_strs)}]")
