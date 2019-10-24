import time

def func1(arr):
    total = sum(arr)
    if total % 2 == 1:
        return False
    # return dfs(arr, 0, 0, total / 2)
    return dfs1(arr, 0, int(total / 2))

def func2(arr):
    total = sum(arr)
    if total % 2 == 1:
        return False
    dp = [[-1 for x in range(int(total / 2) + 1)] for y in range(len(arr))]
    # return True if dfs_with_memo(arr, dp, 0, 0, total / 2) == 1 else False
    return True if dfs_with_memo2(arr, dp, 0, int(total / 2)) == 1 else False
    # return True if dfs_with_memo3(arr, dp, 0, int(total / 2)) == 1 else False

def dfs(arr, index, crtSum, sum):
    if len(arr) == 0 or index >= len(arr) or crtSum > sum:
        return False
    if crtSum == sum:
        return True

    return dfs(arr, index + 1, crtSum + arr[index], sum) or dfs(arr, index + 1, crtSum, sum) 

def dfs1(arr, index, sum):
    if len(arr) == 0 or index >= len(arr) or sum < 0:
        return False
    if sum == 0:
        return True
    if arr[index] <= sum:
        if dfs1(arr, index + 1, sum - arr[index]):
            return True
    return dfs1(arr, index + 1, sum)

def dfs_with_memo(arr, dp, index, crtSum, sum):
    if len(arr) == 0 or index >= len(arr) or crtSum > sum:
        return 0
    if crtSum == sum:
        dp[index][crtSum] = 1
        return 1
    if dp[index][crtSum] != -1:
        return dp[index][crtSum]
    leftResult = dfs_with_memo(arr, dp, index + 1, crtSum + arr[index], sum)
    rightResult = dfs_with_memo(arr, dp, index + 1, crtSum, sum)
    if leftResult == 1 or rightResult == 1:
        dp[index][crtSum] = 1
    else:
        dp[index][crtSum] = 0
    return dp[index][crtSum]

def dfs_with_memo2(arr, dp, index, sum):
    if len(arr) == 0 or index >= len(arr) or sum < 0:
        return 0
    if sum == 0:
        dp[index][sum] = 1
        return 1
    if dp[index][sum] != -1:
        return dp[index][sum]
    if dfs_with_memo2(arr, dp, index + 1, sum - arr[index]) == 1:
        dp[index][sum] = 1
        return 1
    dp[index][sum] = dfs_with_memo2(arr, dp, index + 1, sum)
    return dp[index][sum]

def dfs_with_memo3(arr, dp, index, sum):
    if sum == 0:
        return 1
    if len(arr) == 0 or index >= len(arr):
        return 0
    
    if dp[index][sum] == -1:
        if arr[index] <= sum:
            if dfs_with_memo3(arr, dp, index + 1, sum - arr[index]) == 1:
                dp[index][sum] = 1
                return 1
    dp[index][sum] = dfs_with_memo3(arr, dp, index + 1, sum)
    return dp[index][sum]

if __name__ == "__main__":
    print(f'func1: {func1([1, 2, 3, 4])}, func2: {func2([1, 2, 3, 4])}')
    print(f'func1: {func1([2, 3, 4, 6])}, func2: {func2([2, 3, 4, 6])}')
    print(f'func1: {func1([1, 5, 11, 9])}, func2: {func2([1, 5, 11, 9])}')
    print(f'func1: {func1([1, 5, 11, 7])}, func2: {func2([1, 5, 11, 7])}')
    print(f'func1: {func1([1, 3])}, func2: {func2([1, 3])}')
    print(f'func1: {func1([])}, func2: {func2([])}')

    start = time.perf_counter()
    print(f'func1: {func1([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79])}')
    end = time.perf_counter()
    print(f'time: {end - start}')

    start = time.perf_counter()
    print(f'func2: {func2([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79])}')
    end = time.perf_counter()
    print(f'time: {end - start}')