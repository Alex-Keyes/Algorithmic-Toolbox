# Uses python3
def get_fibonacci_last_digit_naive(n):
    fib_nums = [0, 1]
    for num in range(2, n+1):
        new_fib_num = fib_nums[num-1] + fib_nums[num-2]
        fib_nums.append(new_fib_num % 10)
    return fib_nums[n]


n = int(input())
print(get_fibonacci_last_digit_naive(n))
