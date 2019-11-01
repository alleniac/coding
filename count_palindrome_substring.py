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

def func1(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        dp[i][i] = True
        count += 1
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if s[start] == s[end]:
                if end == start + 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    count += 1
    return count
    
if __name__ == '__main__':
    test(func1, 1)
    test(func1, 2)
    test(func1, 3)
    test(func1, 4)
    test(func1, 5)