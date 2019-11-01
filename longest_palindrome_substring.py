import time

def test(func, testCase):
    testStr1 = 'abdbca'
    testStr2 = 'cddpd'
    testStr3 = 'pqr'
    testStr4 = 'aaaa'
    testStr5 = 'cdpqabdbcardpd'

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testStr{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

# find the length of longest palindrome substring
def func1(s):
    return dfs(s, 0, len(s) - 1)

def func2(s):
    n = len(s)
    # keeps the longest palindrome substring between start and end
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    return dfs2(s, memo, 0, n - 1)

def func3(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    maxLength = 1
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if s[start] == s[end]:
                if end == start + 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    maxLength = max(maxLength, end - start + 1)
    return maxLength

def dfs(s, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if s[start] == s[end]:
        res = dfs(s, start + 1, end - 1)
        if res == end - start - 1:
            return res + 2
    length1 = dfs(s, start + 1, end)
    length2 = dfs(s, start, end - 1)
    return max(length1, length2)

def dfs2(s, memo, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if memo[start][end] != -1:
        return memo[start][end]
    if s[start] == s[end]:
        res = dfs2(s, memo, start + 1, end - 1)
        if res == end - start - 1:
            memo[start][end] = res + 2
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

    test(func1, 5)
    test(func2, 5)
    test(func3, 5)