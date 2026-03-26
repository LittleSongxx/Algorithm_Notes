def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)
