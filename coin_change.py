import time

def func1(coins, total):
    return dfs(coins, total, 0)

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

def test(func, testCase):
    testCoins1 = [1, 2, 3]
    testTotal1 = 5

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testCoins{testCase}'], lcl[f'testTotal{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

if __name__ == '__main__':
    test(func=func1, testCase=1)