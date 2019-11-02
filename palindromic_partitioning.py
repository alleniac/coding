import time

def test(func, testCase):
    testStr1 = 'abdbca'
    testStr2 = 'cdpdd'
    testStr3 = 'pqr'
    testStr4 = 'aaaa'
    testStr5 = 'madam'

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

def dfs(s, start):
    n = len(s)
    if start >= n - 1 or isPal(s, start, n - 1):
        return 0
    
    minRes = n - start - 1
    for i in range(start, n):
        if isPal(s, start, i):
            minRes = min(minRes, 1 + dfs(s, i + 1))
    
    return minRes

if __name__ == '__main__':
    test(func1, 1)
    test(func1, 2)
    test(func1, 3)
    test(func1, 4)
    test(func1, 5)
