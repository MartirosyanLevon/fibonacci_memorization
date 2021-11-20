fibo_cache = {}


def fib(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)
    fibo_cache[n] = value
    return value


size = int(input('enter size of fibonacci : '))
for n in range(1, size + 1):
    print(n, ':', fib(n))
