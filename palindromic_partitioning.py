import time

def test(func, testCase):
    testStr1 = 'abdbca'
    testStr2 = 'cdpdd'
    testStr3 = 'pqr'
    testStr4 = 'aaaa'
    testStr5 = 'madam'
    testStr6 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'testStr{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def isPal(s, start, end):
    n = len(s)
    if n == 1:
        return True
    while (start <= end):
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def func1(s):
    return dfs(s, 0)

def func2(s):
    n = len(s)
    pal = [[False for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        left = i
        right = i
        while left >= 0 and right < n:
            if isPal(s, left, right):
                pal[left][right] = True
                left -= 1
                right += 1
            else:
                break
    for i in range(0, n):
        left = i
        right = i + 1
        while left >= 0 and right < n:
            if isPal(s, left, right):
                pal[left][right] = True
                left -= 1
                right += 1
            else:
                break
    # keep the minimum number of palindromic partitions from index to the end
    memo = [-1 for _ in range(n)]
    return dfs2(s, pal, memo, 0)
            

def dfs(s, start):
    n = len(s)
    if start >= n - 1 or isPal(s, start, n - 1):
        return 0
    
    minRes = n - start - 1
    for i in range(start, n):
        if isPal(s, start, i):
            minRes = min(minRes, 1 + dfs(s, i + 1))
    
    return minRes

def dfs2(s, pal, memo, start):
    n = len(s)

    # base case: 
    if start >= n - 1 or pal[start][n - 1]:
        return 0
    
    # if the result from `start` up till end is found, return it directly
    if memo[start] != -1:
        return memo[start]
    
    minRes = n - start
    for i in range(start, n):
        if pal[start][i]:
            minRes = min(minRes, 1 + dfs2(s, pal, memo, i + 1))
    memo[start] = minRes
    return memo[start]

if __name__ == '__main__':
    # test(func1, 1)
    # test(func2, 1)
    # test(func1, 2)
    # test(func2, 2)
    # test(func1, 3)
    # test(func2, 3)
    # test(func1, 4)
    # test(func2, 4)
    # test(func1, 5)
    # test(func2, 5)
    # test(func1, 6)
    test(func2, 6)