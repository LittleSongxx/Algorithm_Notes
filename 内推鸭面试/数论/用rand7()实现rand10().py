from random import randint


def rand7():
    return randint(1, 7)


def rand10():
    while True:
        num = (rand7() - 1) * 7 + rand7()

        if num <= 40:
            return (num - 1) % 10 + 1


t = int(input())

# 调用rand10并输出结果
results = []
for _ in range(t):
    results.append(str(rand10()))
print('\n'.join(results))
