digits = input().strip()

mp = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

res = []
path = []


def dfs(index):
    if index == len(digits):
        res.append(''.join(path))
        return
    letters = mp[digits[index]]

    for ch in letters:
        path.append(ch)
        dfs(index + 1)  # 递归处理下一位，即下一个数对应的字符串
        path.pop()


dfs(0)
print(*res)
