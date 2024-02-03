fib_cache = {}


def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1 or n == 2:
        fib_cache[n] = 1
        return 1

    fib_num = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = fib_num
    return fib_num


n = int(input())


fibonacci_num = fibonacci(n)


print(fibonacci_num)
