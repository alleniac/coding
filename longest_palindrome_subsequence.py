import time

def test(func, testCase):
    testStr1 = 'abdbca'
    testStr2 = 'cddpd'
    testStr3 = 'pqr'
    testStr4 = 'cdpqabdbcardpd'

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testStr{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(s):
    return dfs(s, 0, len(s) - 1)

def func2(s):
    memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return dfs2(s, memo, 0, len(s) - 1)

def func3(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    # notice the sequence of execution
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    return dp[0][n - 1]

def dfs(s, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1
    
    if s[start] == s[end]:
        return 2 + dfs(s, start + 1, end - 1)
    
    case1 = dfs(s, start + 1, end)
    case2 = dfs(s, start, end - 1)

    return max(case1, case2)

def dfs2(s, memo, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if memo[start][end] != -1:
        return memo[start][end]
    
    if s[start] == s[end]:
        memo[start][end] = 2 + dfs2(s, memo, start + 1, end - 1)
        return memo[start][end]
    
    memo[start][end] = max(dfs2(s, memo, start + 1, end), dfs2(s, memo, start, end - 1))

    return memo[start][end]

if __name__ == '__main__':
    test(func1, 1)
    test(func2, 1)
    test(func3, 1)

    test(func1, 2)
    test(func2, 2)
    test(func3, 2)

    test(func1, 3)
    test(func1, 3)
    test(func3, 3)

    test(func1, 4)
    test(func2, 4)
    test(func3, 4)
