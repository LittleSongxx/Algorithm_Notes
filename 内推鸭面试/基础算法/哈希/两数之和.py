def twoSum(nums, target):
    mp = dict()
    n = len(nums)

    for i in range(n):
        need = target - nums[i]

        if need in mp:
            return [mp[need], i]

        mp[nums[i]] = i

    # 没找到
    return [-1, -1]


if __name__ == "__main__":
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))

    res = twoSum(nums, target)

    print(res[0], res[1])
