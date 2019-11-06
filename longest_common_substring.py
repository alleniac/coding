import time

def test(func, testCase):
    test1 = ['abdca', 'cbda']
    test2 = ['passport', 'ppsspt']

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'test{testCase}'][0], lcl[f'test{testCase}'][1])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(s1, s2):
    return dfs(s1, s2, 0, 0)

def func2(s1, s2):
    n = len(s1)
    m = len(s2)
    # stores the longest common subsequence at index i, j for s1, s2
    memo = [[-1 for _ in range(m)] for _ in range(n)]
    return dfs2(s1, s2, memo, 0, 0)

# return the longest common subsequence at the index of i, j at s1, s2
def dfs(s1, s2, i, j):
    n = len(s1)
    m = len(s2)
    if i == n or j == m:
        return 0
    if s1[i] == s2[j]:
        return 1 + dfs(s1, s2, i + 1, j + 1)
    
    res1 = dfs(s1, s2, i + 1, j)
    res2 = dfs(s1, s2, i, j + 1)

    return max(res1, res2)

def dfs2(s1, s2, memo, i, j):
    n = len(s1)
    m = len(s2)

    # base case
    if i == n or j == m:
        return 0

    # if visited this state (i, j) before
    if memo[i][j] != -1:
        return memo[i][j]
    
    if s1[i] == s2[j]:
        memo[i][j] = 1 + dfs2(s1, s2, memo, i + 1, j + 1)
        return memo[i][j]
    
    memo[i][j] = max(dfs2(s1, s2, memo, i + 1, j), dfs2(s1, s2, memo, i, j + 1))
    return memo[i][j]

if __name__ == "__main__":
    test(func1, 1)
    test(func2, 1)

    test(func1, 2)
    test(func2, 2)
