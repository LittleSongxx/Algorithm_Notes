def check(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

n = int(input())
s = input()
if check(s):
    print("Yes")
else:
    print("No")


