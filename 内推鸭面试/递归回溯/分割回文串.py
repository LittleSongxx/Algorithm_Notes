s = input().strip()
n = len(s)

def check(s):
    return s == s[::-1]

path = []
def dfs(start):
    if start == n:
        path.append()