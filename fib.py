import sys
import time

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    n_to_ans = dict()
    return fib2_helper(n_to_ans, n)

def fib2_helper(n_to_ans, n):
    if n in n_to_ans:
        return n_to_ans[n]
    ans = 0
    if n == 0 or n == 1:
        ans = n
    else:
        ans = fib2_helper(n_to_ans, n - 1) + fib2_helper(n_to_ans, n- 2)
    n_to_ans[n] = ans
    return ans

if __name__ == '__main__':   
    for n in sys.argv[1:]:
        n = int(n)

        # start = time.perf_counter()
        # print(f'fib({n}) = {fib(n)}')
        # end = time.perf_counter()
        # print(f'Time elapsed for fib func is: {end - start}')

        start = time.perf_counter()
        print(f'fib2({n}) = {fib2(n)}')
        end = time.perf_counter()
        print(f'Time elapsed for fib2 func is: {end - start}')