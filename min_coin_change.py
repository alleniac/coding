import time
import math

def test(func, testCase):
    # 2
    testCoins1 = [1, 2, 3]
    testTotal1 = 5

    # 4
    testCoins2 = [1, 2, 3, 4, 5]
    testTotal2 = 20

    # 34
    testCoins3 = [3,4,20,1,8,12,30]
    testTotal3 = 1000

    # 100
    testCoins4 = [1]
    testTotal4 = 100

    # 9
    testCoins5 = [1, 2, 3, 4, 6]
    testTotal5 = 50

    # 4
    testCoins6 = [1, 2, 3]
    testTotal6 = 11

    # 4
    testCoins7 = [1, 2, 3, 4, 5]
    testTotal7 = 18

    # -1
    testCoins8 = [3, 5]
    testTotal8 = 7

    # 0
    testCoins9 = []
    testTotal9 = 0

    # -1
    testCoins10 = []
    testTotal10 = 3

    testCoins11 = [205,37,253,463,441,129,156,429,101,423,311]
    testTotal11 = 6653

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testCoins{testCase}'], lcl[f'testTotal{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

# return the minimum number of coins needed for the total amount
def func1(coins, total):
    result = dfs(coins, total, 0)
    return -1 if result == math.inf else result

def func2(coins, total):
    dp = [[-1 for _ in range(total + 1)] for _ in range(len(coins))]
    result = dfs2(coins, total, dp, 0)
    return -1 if result == math.inf else result

def func3(coins, total):
    n = len(coins)

    if total == 0:
        return 0
    if n == 0:
        return -1

    dp = [[math.inf for _ in range(total + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    
    for i in range(n):
        for j in range(total + 1):
            if i > 0:
                dp[i][j] = dp[i - 1][j]
            result1 = dp[i][j - coins[i]] + 1 if j - coins[i] >= 0 and dp[i][j - coins[i]] != math.inf else math.inf
            dp[i][j] = min(result1, dp[i][j])
    
    return dp[n - 1][total] if dp[n - 1][total] != math.inf else -1

def dfs(coins, total, index):
    if total == 0:
        return 0

    n = len(coins)

    if n == 0 or index >= n or total < 0:
        return math.inf
    
    # include myself
    result1 = math.inf
    if total - coins[index] >= 0:
        if dfs(coins, total - coins[index], index) != math.inf:
            result1 = dfs(coins, total - coins[index], index) + 1
    
    result2 = dfs(coins, total, index + 1)

    # if result1 == -1 and result2 == -1:
    #     return -1
    # elif result1 != -1 and result2 != -1:
    #     return min(result1, result2)
    # else:
    #     return result1 if result2 == -1 else result2
    return min(result1, result2)

def dfs2(coins, total, dp, index):
    if total == 0:
        return 0

    n = len(coins)
    if n == 0 or index >= n or total < 0:
        return math.inf

    if dp[index][total] != -1:
        return dp[index][total]

    result1 = math.inf
    if total - coins[index] >= 0:
        if dfs2(coins, total - coins[index], dp, index) != math.inf:
            result1 = dfs2(coins, total - coins[index], dp, index) + 1
    
    result2 = dfs2(coins, total, dp, index + 1)

    dp[index][total] = min(result1, result2)
    return dp[index][total]

if __name__ == '__main__':
    test(func=func1, testCase=1)
    test(func2, 1)
    test(func3, 1)

    test(func1, 2)
    test(func2, 2)
    test(func3, 2)

    # test(func1, 3)
    test(func2, 3)
    test(func3, 3)

    # test(func1, 4)
    test(func2, 4)
    test(func3, 4)

    # test(func1, 5)
    test(func2, 5)
    test(func3, 5)

    test(func1, 6)
    test(func2, 6)
    test(func3, 6)

    test(func1, 7)
    test(func2, 7)
    test(func3, 7)

    test(func1, 8)
    test(func2, 8)
    test(func3, 8)

    test(func1, 9)
    test(func2, 9)
    test(func3, 9)

    test(func1, 10)
    test(func2, 10)
    test(func3, 10)

    test(func2, 11)
    test(func3, 11)
