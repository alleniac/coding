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
    n = len(s1)
    m = len(s2)
    memo = [["" for _ in range(m)] for _ in range(n)]
    return dfs(s1, s2, 0, 0, memo)

def dfs(s1, s2, i, j, memo):
    n = len(s1)
    m = len(s2)
    if i == n or j == m:
        return ""
    if len(memo[i][j]) > 0:
        return memo[i][j]
    if s1[i] == s2[j]:
        res = dfs(s1, s2, i + 1, j + 1, memo)
        res = s1[i] + res
        memo[i][j] = res
        return memo[i][j]
    
    res1 = dfs(s1, s2, i + 1, j, memo)
    res2 = dfs(s1, s2, i, j + 1, memo)
    memo[i][j] = res1 if len(res1) > len(res2) else res2
    return memo[i][j]

if __name__ == '__main__':
    test(func1, 1)
    
    test(func1, 2)