version1 = input().strip()
version2 = input().strip()

# 1.2  -> [1, 2]
# 1.10 -> [1, 10]
v1 = version1.split('.')
v2 = version2.split('.')

n = max(len(v1), len(v2))

for i in range(n):
    # 处理末尾修订号缺失的情况，例如1.0和1.0.1比，1.0视为1.0.0
    num1 = int(v1[i] if i < len(v1) else 0)
    num2 = int(v2[i] if i < len(v2) else 0)

    # 某一位不相等则可以直接判断整个版本号的大小
    if num1 > num2:
        print(1)
        break
    elif num1 < num2:
        print(-1)
        break

# 比较完全部位才能判断是否相等
else:
    print(0)