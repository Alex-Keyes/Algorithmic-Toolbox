# Uses python3
def calc_fib(n):
    fib_nums = [0, 1]
    for num in range(2, n+1):
        fib_nums.append(fib_nums[num-1] + fib_nums[num-2])
    return fib_nums[n]


n = int(input())
print(calc_fib(n))
