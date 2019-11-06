# import time

# def test(func, testCase):
#     test1 = ['abdca', 'cbda']
#     test2 = ['passport', 'ppsspt']

#     lcl = locals()

#     start = time.perf_counter()
#     result = func(lcl[f'test{testCase}'][0], lcl[f'test{testCase}'][1])
#     end = time.perf_counter()
#     print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

# def func1(s1, s2):
#     return dfs(s1, s2, 0, 0, 0)

# # minimum delete and insert operation counts at position i, j for s1, s2
# def dfs(s1, s2, i, j, count):
#     n = len(s1)
#     m = len(s2)
#     if i == n or j == m:
#         return count
#     if s1[i] == s2[j]:
#         return dfs(s1, s2, i + 1, j + 1, count)
    
#     # if not equal, then there are 2 choices
#     # 1. delete the current index (use the next character of s1 to match current character of s2)
#     res1 = dfs(s1, s2, i + 1, j, count + 1)
#     # 2. insert a character to the current position of s1 to match the current character of s2
#     res2 = dfs(s1, s2, i, j + 1, count + 1)

#     # find the minimum
#     return min(res1, res2)
    
# if __name__ == '__main__':
#     test(func1, 1)
    
#     test(func1, 2)