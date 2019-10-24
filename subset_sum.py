def func1(arr, target):
    print(f'dfs: {dfs(arr, 0, target)}')
    dp = [[-1 for x in range(target + 1)] for y in range(len(arr))]
    print(f'dfs2: {True if dfs2(arr, dp, 0, target) == 1 else False}')    

def dfs(arr, index, remain):
    if len(arr) == 0 or index >= len(arr) or remain < 0:
        return False
    if remain == 0:
        return True

    return dfs(arr, index + 1, remain - arr[index]) or dfs(arr, index + 1, remain)

def dfs2(arr, dp, index, remain):
    if len(arr) == 0 or index >= len(arr) or remain < 0:
        return 0
    if remain == 0:
        return 1
    if dp[index][remain] != -1:
        return dp[index][remain]
    
    # include myself
    if dfs2(arr, dp, index + 1, remain - arr[index]) == 1:
        dp[index][remain] = 1
        return 1
    
    # not include myself
    dp[index][remain] = 1 if dfs2(arr, dp, index + 1, remain) == 1 else 0
    return dp[index][remain]

if __name__ == '__main__':
    func1([1, 2, 3, 7], 6)
    func1([1, 2, 7, 1, 5], 10)
    func1([3, 1, 4, 8], 6)
    