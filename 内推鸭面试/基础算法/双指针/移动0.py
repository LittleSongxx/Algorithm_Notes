n = int(input())
nums = list(map(int, input().split()))

j = 0

for i in range(n):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]  # 把非0数换过来，把0换到后面去
        j += 1  # 由于只有当nums[i]!=0时j才会移动，所以j每次会停在0的位置

print(*nums)
