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

# my own dp solution
def func3(arr):
    if len(arr) == 0:
        return False
    total = sum(arr)
    if total % 2 == 1:
        return False

    dp = [[False for x in range(int(total / 2) + 1)] for y in range(len(arr))]

    # init
    for i in range(len(arr)):
        dp[i][0] = True
    for j in range(int(total / 2) + 1):
        if arr[0] == j:
            dp[0][j] = True
    
    for i in range(1, len(arr)):
        for j in range(1, int(total / 2) + 1):
            dp[i][j] = dp[i - 1][j - arr[i]] or dp[i - 1][j]
    
    return dp[len(arr) - 1][int(total / 2)]

# tutorial's dp solution
def func4(num):
    s = sum(num)

    if s % 2 != 0:
        return False

    s = int(s / 2)
    n = len(num)

    dp = [[False for x in range(s + 1)] for y in range(n)]

    # populate the s=0 columns, as we can always for '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is
    # equal to its value
    for j in range(1, s+1):
        dp[0][j] = num[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, s+1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:  # else if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]

    # the bottom-right corner will have our answer.
    return dp[n - 1][s]

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
    print(f'func1: {func1([1, 2, 3, 4])},  func2: {func2([1, 2, 3, 4])},  func3: {func3([1, 2, 3, 4])}')
    print(f'func1: {func1([2, 3, 4, 6])},  func2: {func2([2, 3, 4, 6])},  func3: {func3([2, 3, 4, 6])}')
    print(f'func1: {func1([1, 5, 11, 9])}, func2: {func2([1, 5, 11, 9])}, func3: {func3([1, 5, 11, 9])}')
    print(f'func1: {func1([1, 5, 11, 7])}, func2: {func2([1, 5, 11, 7])}, func3: {func3([1, 5, 11, 7])}')
    print(f'func1: {func1([1, 3])},        func2: {func2([1, 3])},        func3: {func3([1, 3])}')
    print(f'func1: {func1([])},            func2: {func2([])},            func3: {func3([])}')

    start = time.perf_counter()
    print(f'func1: {func1([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79])}')
    end = time.perf_counter()
    print(f'time: {end - start}')

    start = time.perf_counter()
    print(f'func2: {func2([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79])}')
    end = time.perf_counter()
    print(f'time: {end - start}')

    start = time.perf_counter()
    print(f'func3: {func3([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79])}')
    end = time.perf_counter()
    print(f'time: {end - start}')

    start = time.perf_counter()
    print(f'func4: {func4([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79])}')
    end = time.perf_counter()
    print(f'time: {end - start}')