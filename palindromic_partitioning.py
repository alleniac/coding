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
        while left >= 0 and right < n and s[left] == s[right]:
            pal[left][right] = True
            left -= 1
            right += 1
    for i in range(0, n):
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            pal[left][right] = True
            left -= 1
            right += 1
    # keep the minimum number of palindromic partitions from index to the end
    memo = [-1 for _ in range(n)]
    return dfs2(s, pal, memo, 0)

def func3(s):
    n = len(s)
    pal = [[False for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        left = i
        right = i
        while left >= 0 and right < n and s[left] == s[right]:
            pal[left][right] = True
            left -= 1
            right += 1
    for i in range(0, n):
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            pal[left][right] = True
            left -= 1
            right += 1
    # keep the minimum number of palindromic partitions from index to the end
    memo = [-1 for _ in range(n)]
    return dfs3(s, pal, memo, n -1)   

def func4(s):
    n = len(s)
    pal = [[False for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        left = i
        right = i
        while left >= 0 and right < n and s[left] == s[right]:
            pal[left][right] = True
            left -= 1
            right += 1
    for i in range(0, n):
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            pal[left][right] = True
            left -= 1
            right += 1
    
    # from index to end, the minimum number of partitions
    num = [-1 for _ in range(n)]
    for start in range(n - 1, -1, -1):
        minRes = n - start
        for end in range(n - 1, start - 1, -1):
            if pal[start][end] and end == n - 1:
                minRes = 0
            elif pal[start][end]:
                minRes = min(minRes, 1 + num[end + 1])
        num[start] = minRes
    return num[0]

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

def dfs3(s, pal, memo, end):
    if end == 0 or pal[0][end]:
        return 0
    
    if memo[end] != -1:
        return memo[end]
    
    minRes = end
    for i in range(0, end + 1):
        if pal[i][end]:
            minRes = min(minRes, 1 + dfs3(s, pal, memo, i - 1))
    
    memo[end] = minRes
    return memo[end]

if __name__ == '__main__':
    test(func1, 1)
    test(func2, 1)
    test(func3, 1)

    test(func1, 2)
    test(func2, 2)
    test(func3, 2)

    test(func1, 3)
    test(func2, 3)
    test(func3, 3)
    
    test(func1, 4)
    test(func2, 4)
    test(func3, 4)

    test(func1, 5)
    test(func2, 5)
    test(func3, 5)

    # test(func1, 6)
    test(func2, 6)
    test(func3, 6)