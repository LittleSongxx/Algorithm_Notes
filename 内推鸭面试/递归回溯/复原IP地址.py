from rich import segment

s = input().strip()

res = []
parts = []


def is_valid(segment):
    # 每一字段长度不能为0
    if len(segment) == 0:
        return False

    # 每一字段不能以0开题
    if len(segment) > 1 and segment[0] == '0':
        return False

    # 字段数组要在0-255之间
    if int(segment) > 255:
        return False

    return True


def dfs(start):
    # 如果已经切出了 4 段
    if len(parts) == 4:
        # 只有字符串也刚好用完，才是合法答案
        if start == len(s):
            res.append('.'.join(parts))
        return

    # 每一段最多 3 位，所以尝试长度 1、2、3
    for length in range(1, 4):
        end = start + length

        if end > len(s):
            break

        segment = s[start:end]

        if not is_valid(segment):
            continue

        parts.append(segment)
        dfs(end)
        parts.pop()


dfs(0)

print(res)
