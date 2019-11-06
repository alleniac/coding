import time
import math

def test(func, testCase):
    test1 = [4,2,3,6,10,1,12]
    test2 = [-4,10,3,7,15]
    test3 = [10,9,2,5,3,7,101,18]

    lcl = locals()

    start = time.perf_counter()
    result = func(lcl[f'test{testCase}'])
    end = time.perf_counter()
    print(f'function: {func.__name__}, testCase: {testCase}, result: {result}, time: {end - start}')

def func1(nums):
    return dfs(nums, 0, -math.inf, 0)

def func2(nums):
    return dfs2(nums, 0, -1)

def func3(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    res = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(0, i):
            if nums[i] > nums[j] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1
                res = max(res, dp[i])
    return res

# return the length of LISubsequence at index
def dfs(nums, index, prevMax, length):
    n = len(nums)
    if index == n:
        return length
    
    # include the current index if it doens't exceed the prevMax
    res1 = -math.inf
    res2 = -math.inf
    if nums[index] > prevMax:
        res1 = dfs(nums, index + 1, nums[index], length + 1)

    res2 = dfs(nums, index + 1, prevMax, length)
    return max(res1, res2)

def dfs2(nums, index, prevIndex):
    if index == len(nums):
        return 0

    res1 = -math.inf
    if prevIndex == -1 or nums[prevIndex] < nums[index]:
        res1 = 1 + dfs2(nums, index + 1, index)
    
    res2 = dfs2(nums, index + 1, prevIndex)
    
    return max(res1, res2)

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