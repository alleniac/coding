import math
import time

def test(func, testCase):
    testJumps1 = [2,1,1,1,4]
    testJumps2 = [1,1,3,6,9,3,0,1,3]
    testJumps3 = [2,1,1,1,4,2,1,1,1,4,1,1,3,6,1,1,3,6,3,0,1,3,1,1,4]
    testJumps4 = [1,1,4,2,1,1,1,4,1,1,3,6,1,1,3,6,3,1,1,4,2,1,1,1,4,1,1,3,6,1,1,3,6,3,1,1,4,2,1,1,1,4,1,1,3]

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testJumps{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(jumps):
    return dfs(jumps, 0)

def func2(jumps):
    memory = [math.inf for _ in range(len(jumps))]
    return dfs2(jumps, memory, 0)

def func3(jumps):
    n = len(jumps)
    dp = [math.inf for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        maxSteps = jumps[i]
        if maxSteps == 0:
            continue
        for step in range(1, maxSteps + 1):
            if i + step >= n:
                dp[n - 1] = min(dp[n - 1], dp[i] + 1)
                break
            dp[i + step] = min(dp[i + step], dp[i] + 1)
    
    return dp[n - 1]

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

def dfs2(jumps, memory, index):
    n = len(jumps)
    if index >= n - 1:
        return 0
    if memory[index] != math.inf:
        return memory[index]
    
    maxSteps = jumps[index]
    if maxSteps == 0:
        return math.inf
    for step in range(1, maxSteps + 1):
        res = dfs2(jumps, memory, index + step)
        if res != math.inf:
            memory[index] = min(memory[index], res + 1)
    
    return memory[index]

if __name__ == '__main__':
    test(func1, 1)
    test(func2, 1)
    test(func3, 1)
    
    test(func1, 2)
    test(func2, 2)
    test(func3, 2)

    test(func1, 3)
    test(func2, 3)
    test(func3, 3)

    # test(func1, 4)
    test(func2, 4)
    test(func3, 4)
