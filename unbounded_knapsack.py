import time

def func1(weights, profits, capacity):
    # assume that len(weights) == len(profits)
    return dfs(weights, profits, capacity, 0, 0)

def func2(weights, profits, capacity):
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(weights))]
    return dfs2(weights, profits, capacity, dp, 0)

def func3(weights, profits, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    # init
    # for i in range(n):
    #     dp[i][0] = 0
    # for j in range(capacity + 1):
    #     if weights[0] <= j:
    #         dp[0][j] = capacity % weights[0] * profits[0]

    for i in range(n):
        for j in range(capacity + 1):
            profit1 = 0
            if j - weights[i] >= 0:
                profit1 = profits[i] + dp[i][j - weights[i]]
            profit2 = dp[i - 1][j]
            dp[i][j] = max(profit1, profit2)
    
    return dp[n - 1][capacity]

def dfs(weights, profits, capacity, crtWeight, index):
    n = len(weights)
    
    if n == 0 or index >= n or crtWeight > capacity:
        return 0
    
    # include myself
    profit1 = 0
    if weights[index] + crtWeight <= capacity:
        profit1 = profits[index] + dfs(weights, profits, capacity, crtWeight + weights[index], index)
    
    # not include myself
    profit2 = dfs(weights, profits, capacity, crtWeight, index + 1)

    return max(profit1, profit2)

def dfs2(weights, profits, capacity, dp, index):
    n = len(weights)

    if n == 0 or index >= n or capacity < 0:
        return 0
    if dp[index][capacity] != -1:
        return dp[index][capacity]

    # include myself
    profit1 = 0
    if capacity - weights[index] >= 0:
        profit1 = profits[index] + dfs2(weights, profits, capacity - weights[index], dp, index)

    # not include myself:
    profit2 = dfs2(weights, profits, capacity, dp, index + 1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]

def test(func, testCase):
    testWeights1 = [1, 2, 3]
    testProfits1 = [15, 20, 50]
    testCapacity1 = 5

    testWeights2 = [1, 3, 4, 5]
    testProfits2 = [15, 50, 60, 90]
    testCapacity2 = 8

    testWeights3 = [1, 3, 4, 5]
    testProfits3 = [15, 50, 60, 90]
    testCapacity3 = 6

    testWeights4 = [2, 3, 4, 5]
    testProfits4 = [35, 50, 60, 75]
    testCapacity4 = 100

    testWeights5 = [2, 3, 3, 4, 7, 5, 4, 10, 6]
    testProfits5 = [35, 50, 60, 75, 100, 78, 41, 99, 74]
    testCapacity5 = 200

    # Access to variables in namespaces: https://stackoverflow.com/questions/8028708/dynamically-set-local-variable
    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testWeights{testCase}'], lcl[f'testProfits{testCase}'], lcl[f'testCapacity{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

if __name__ == '__main__':
    test(func1, 1)
    test(func1, 2)
    test(func1, 3)
    test(func1, 4)
    # This test case takes too long to run for func1
    # test(func1, 5)

    test(func2, 1)
    test(func2, 2)
    test(func2, 3)
    test(func2, 4)
    test(func2, 5)

    test(func3, 1)
    test(func3, 2)
    test(func3, 3)
    test(func3, 4)
    test(func3, 5)