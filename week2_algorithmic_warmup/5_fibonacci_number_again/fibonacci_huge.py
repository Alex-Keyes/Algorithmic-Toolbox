# Uses python3
def get_fibonacci(n):
    fib_nums = [0, 1]
    for num in range(2, n+1):
        fib_nums.append(fib_nums[num-1] + fib_nums[num-2])
    return fib_nums[n]


def fib_period_length(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_fast(n, m):
    remainder = n % fib_period_length(m)
    return get_fibonacci(remainder) % m


n, m = map(int, input().split())
print(get_fibonacci_huge_fast(n, m))
