def func1(arr):
    total = sum(arr)
    if total % 2 == 1:
        return False
    return dfs(arr, 0, 0, total / 2)

def func2(arr):
    total = sum(arr)
    if total % 2 == 1:
        return False
    dp = [[-1 for x in range(len(arr))] for y in range(int(total / 2 + 1))]
    return True if dfs_with_memo(arr, dp, 0, 0, total / 2) == 1 else False

def dfs(arr, index, crtSum, sum):
    if len(arr) == 0 or index >= len(arr) or crtSum > sum:
        return False
    if crtSum == sum:
        return True

    return dfs(arr, index + 1, crtSum + arr[index], sum) or dfs(arr, index + 1, crtSum, sum) 

def dfs_with_memo(arr, dp, index, crtSum, sum):
    if len(arr) == 0 or index >= len(arr) or crtSum > sum:
        return 0
    if crtSum == sum:
        dp[index][crtSum] = 1
        return 1
    if dp[index][crtSum] != -1:
        return dp[index][crtSum]
    leftResult = dfs(arr, index + 1, crtSum + arr[index], sum)
    rightResult = dfs(arr, index + 1, crtSum, sum)
    if leftResult == 1 or rightResult == 1:
        dp[index][crtSum] = 1
    else:
        dp[index][crtSum] = 0
    return dp[index][crtSum]

if __name__ == "__main__":
    print(f'func1: {func1([1, 2, 3, 4])}, func2: {func2([1, 2, 3, 4])}')
    print(f'func1: {func1([2, 3, 4, 6])}, func2: {func2([2, 3, 4, 6])}')
    print(f'func1: {func1([1, 5, 11, 9])}, func2: {func2([1, 5, 11, 9])}')
    print(f'func1: {func1([1, 5, 11, 7])}, func2: {func2([1, 5, 11, 7])}')
    print(f'func1: {func1([1, 3])}, func2: {func2([1, 3])}')
    print(f'func1: {func1([])}, func2: {func2([])}')