import math
import time

def test(func, testCase):
    testJumps1 = [2,1,1,1,4]
    testJumps2 = [1,1,3,6,9,3,0,1,3]

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testJumps{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(jumps):
    return dfs(jumps, 0)

def dfs(jumps, index):
    n = len(jumps)
    if index >= n - 1:
        return 0
    
    maxSteps = jumps[index]
    if maxSteps == 0:
        return math.inf
    result = math.inf
    for step in range(1, maxSteps + 1):
        res = dfs(jumps, index + step)
        if res != math.inf:
            result = min(res + 1, result)
    
    return result

if __name__ == '__main__':
    test(func1, 1)
    test(func1, 2)