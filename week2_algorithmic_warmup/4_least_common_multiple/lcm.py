# Uses python3
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm_efficient(a, b):
    return a * b // gcd(a, b)


a, b = map(int, input().split())
print(lcm_efficient(a, b))
