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

def dfs(s1, s2, i, j, length):
    n1 = len(s1)
    n2 = len(s2)
    if i >= n1 or j >= n2:
        return length
    if s1[i] == s2[j]:
        length = dfs(s1, s2, i + 1, j + 1, length + 1)
    
    return max(length, dfs(s1, s2, i, j + 1, 0), dfs(s1, s2, i + 1, j, 0))

if __name__ == '__main__':
    test(func1, 1)
    test(func1, 2)
    