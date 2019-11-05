import time

def test(func, testCase):
    test1 = ['abdca', 'cbda']
    test2 = ['passport', 'psspt']

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'test{testCase}'][0], lcl[f'test{testCase}'][1])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(s1, s2):
    return dfs(s1, s2, 0, 0, 0)

def func2(s1, s2):
    n = len(s1)
    m = len(s2)
    memo = [[[-1 for _ in range(max(n, m))] for _ in range(m)] for _ in range(n)]
    return dfs2(s1, s2, memo, 0, 0, 0)

def func3(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    maxLength = -1
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                maxLength = max(maxLength, dp[i][j])
    return maxLength

def func4(s1, s2):
    n = len(s1)
    m = len(s2)
    if n == 0 or m == 0:
        return 0
    prev = [0 for _ in range(m + 1)]
    crt = [0 for _ in range(m + 1)]
    result = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                crt[j] = prev[j - 1] + 1
                result = max(result, crt[j])
        prev, crt = crt, [0 for _ in range(m + 1)]
    
    return result
                
def dfs(s1, s2, i, j, length):
    n1 = len(s1)
    n2 = len(s2)
    if i >= n1 or j >= n2:
        return length
    if s1[i] == s2[j]:
        length = dfs(s1, s2, i + 1, j + 1, length + 1)
    
    return max(length, dfs(s1, s2, i, j + 1, 0), dfs(s1, s2, i + 1, j, 0))

# return the longest common substring at the positions of i and j till the end of the two strings
def dfs2(s1, s2, memo, i, j, length):
    if i == len(s1) - 1 or j == len(s2) - 1:
        return length
    
    if memo[i][j][length] != -1:
        return memo[i][j][length]
    
    if s1[i] == s2[j]:
        memo[i][j][length] = dfs2(s1, s2, memo, i + 1, j + 1, length + 1)
    
    memo[i][j][length] = max(memo[i][j][length], dfs2(s1, s2, memo, i, j + 1, 0), dfs2(s1, s2, memo, i + 1, j, 0))

    return memo[i][j][length]

if __name__ == '__main__':
    test(func1, 1)
    test(func2, 1)
    test(func3, 1)
    test(func4, 1)

    test(func1, 2)
    test(func2, 2)
    test(func3, 2)
    test(func4, 2)
    