nums1 = input().strip()
nums2 = input().strip()

i = len(nums1) - 1
j = len(nums2) - 1

carry = 0
ans = []

while i >= 0 or j >= 0 or carry:
    if i >= 0:
        x = ord(nums1[i]) - ord('0')
    else:
        x = 0

    if j >= 0:
        y = ord(nums2[j]) - ord('0')
    else:
        y = 0

    total = x + y + carry

    carry = total // 10

    ans.append(str(total % 10))

    i -= 1
    j -= 1

ans.reverse()

print(''.join(ans))
