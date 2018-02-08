# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

max1 = max(a)
a.remove(max(a))
max2 = max(a)

print(max1 * max2)
