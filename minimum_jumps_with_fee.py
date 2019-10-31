import time
import math

def test(func, testCase):
    testFees1 = [1,2,5,2,1,2]
    testFees2 = [2,3,4,5]

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testFees{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(fees):
    return dfs(fees, 0)

def func2(fees):
    memory = [math.inf for _ in range(len(fees))]
    return dfs2(fees, memory, 0)

def func3(fees):
    n = len(fees)
    if n <= 3:
        return fees[0]
    dp = [math.inf for _ in range(n + 1)]
    dp[0], dp[1], dp[2] = 0, fees[0], fees[0]
    for i in range(3, n + 1):
        dp[i] = min(dp[i - 1] + fees[i - 1], dp[i - 2] + fees[i - 2], dp[i - 3] + fees[i - 3])
    return dp[n]

def dfs(fees, index):
    n = len(fees)

    if index >= n:
        return 0
    
    result = math.inf
    for i in range(1, 4):
        result = min(result, dfs(fees, index + i))
    
    return result + fees[index]

def dfs2(fees, memory, index):
    n = len(fees)

    if index >= n:
        return 0
    
    if memory[index] != math.inf:
        return memory[index]
    
    result = math.inf
    for i in range(1, 4):
        result = min(result, dfs2(fees, memory, index + i))
    
    memory[index] = result + fees[index]
    return memory[index]

if __name__ == '__main__':
    test(func1, 1)
    test(func2, 1)
    test(func3, 1)

    test(func1, 2)
    test(func2, 2)
    test(func3, 2)