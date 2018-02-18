# Uses python3
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd


def euclid_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
print(euclid_gcd(a, b))
# print(gcd_naive(a, b))
