import time

def test(func, testCase):
    # test1 = [4,2,3,6,10,1,12]
    test1 = [4,1,2,6,10,1,12]
    test2 = [-4,10,3,7,15]
    test3 = [10,9,2,5,3,7,101,18]

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'test{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(s):
    return dfs(s, 0, -1, 0)

def func2(s):
    n = len(s)
    if n == 0:
        return 0
    # represents the maximum sum of subsequence obtained at index i
    dp = [0 for _ in range(n)]
    dp[0] = s[0]
    result = s[0]
    for i in range(1, n):
        dp[i] = s[i]
        for j in range(0, i):
            if s[i] > s[j]:
                dp[i] = max(dp[j] + s[i], dp[i])
        result = max(result, dp[i])
    return result

def dfs(s, index, prevIndex, sum):
    n = len(s)

    # base case:
    if index == n:
        return sum
    
    res1 = sum
    if prevIndex == -1 or s[index] > s[prevIndex]:
        res1 = dfs(s, index + 1, index, sum + s[index])
    
    res2 = dfs(s, index + 1, prevIndex, sum)

    return max(res1, res2)

if __name__ == '__main__':
    test(func1, 1)
    test(func2, 1)

    test(func1, 2)
    test(func2, 2)

    test(func1, 3)
    test(func2, 3)