import time

def func1(coins, total):
    return dfs(coins, total, 0)

def func2(coins, total):
    dp = [[-1 for _ in range(total + 1)] for _ in range(len(coins))]
    return dfs2(coins, total, dp, 0)

def func3(coins, total):
    n = len(coins)
    dp = [[0 for _ in range(total + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    for i in range(n):
        for j in range(total + 1):
            if i > 0:
                dp[i][j] = dp[i - 1][j]
            dp[i][j] += dp[i][j - coins[i]] if j - coins[i] >= 0 else 0
    
    return dp[n - 1][total]

def dfs(coins, total, index):
    n = len(coins)
    if n == 0 or index >= n or total < 0:
        return 0

    if total == 0:
        return 1
    
    # include myself
    result1 = 0
    if total - coins[index] >= 0:
        result1 = dfs(coins, total - coins[index], index)
    
    # not include myself
    result2 = dfs(coins, total, index + 1)

    return result1 + result2

def dfs2(coins, total, dp, index):
    n = len(coins)

    if n == 0 or index >= n or total < 0:
        return 0
    if total == 0:
        dp[index][total] = 1
        return 1
    if dp[index][total] != -1:
        return dp[index][total]
    
    # include myself
    result1 = 0
    if total - coins[index] >= 0:
        result1 = dfs2(coins, total - coins[index], dp, index)
    
    # not include myself
    result2 = dfs2(coins, total, dp, index + 1)

    dp[index][total] = result1 + result2
    return dp[index][total]

def test(func, testCase):
    testCoins1 = [1, 2, 3]
    testTotal1 = 5

    testCoins2 = [1, 2, 3, 4, 5]
    testTotal2 = 20

    testCoins3 = [3,4,7,1,9,12,30]
    testTotal3 = 1000

    testCoins4 = [1]
    testTotal4 = 100

    testCoins5 = [1, 2, 3, 4, 6]
    testTotal5 = 50

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testCoins{testCase}'], lcl[f'testTotal{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

if __name__ == '__main__':
    test(func=func1, testCase=1)
    test(func=func2, testCase=1)
    test(func=func3, testCase=1)

    test(func1, 2)
    test(func2, 2)
    test(func3, 2)

    # takes too long for func1 to run
    # test(func1, 3)
    test(func2, 3)
    test(func3, 3)
    
    test(func1, 4)
    test(func2, 4)
    test(func3, 4)

    test(func1, 5)
    test(func2, 5)
    test(func3, 5)