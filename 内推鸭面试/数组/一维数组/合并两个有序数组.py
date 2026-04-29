m, n = map(int, input().split())

nums1 = list(map(int, input().split())) if m + n > 0 else []
nums2 = list(map(int, input().split())) if n > 0 else []

i = m - 1  # nums1 有效部分最后一个元素
j = n - 1  # nums2 最后一个元素
k = m + n - 1  # nums1 最后一个位置

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

# 如果 nums2 还有剩余，继续放进 nums1
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print(*nums1)
