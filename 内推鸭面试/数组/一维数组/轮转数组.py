n = int(input())
nums = list(map(int, input().split()))
k = int(input())

k = k % n  # 只右移一圈

nums.reverse()
# nums[:k]:去除前k个元素，[::-1]翻转，nums[:k][::-1]则表示取出前k个元素然后翻转
nums[:k] = nums[:k][::-1]  # 翻转前k个
# nums[k:]从第k个开始取到末尾
nums[k:] = nums[k:][::-1]  # 翻转后n-k个

print(*nums)
