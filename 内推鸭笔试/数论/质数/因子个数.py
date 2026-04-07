import math

x = int(input().strip())

count = 0
# 我们只需要遍历到根号 x 即可
# 注意要向下取整并转为 int
limit = int(math.sqrt(x))

for i in range(1, limit + 1):
    # 如果 i 能整除 x，说明 i 是 x 的因子
    if x % i == 0:
        count += 1  # 记下因子 i

        # 配对的另一个因子是 x // i
        # 如果这两个因子不相等，说明是两个不同的因子
        if i != x // i:
            count += 1

# 输出总数
print(count)
