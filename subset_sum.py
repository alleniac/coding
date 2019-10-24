def func1(arr, target):
    return dfs(arr, 0, target)

def dfs(arr, index, remain):
    if len(arr) == 0 or index >= len(arr) or remain < 0:
        return False
    if remain == 0:
        return True

    return dfs(arr, index + 1, remain - arr[index]) or dfs(arr, index + 1, remain)

if __name__ == '__main__':
    print(f'func1: {func1([1, 2, 3, 7], 6)}')
    print(f'func1: {func1([1, 2, 7, 1, 5], 10)}')
    print(f'func1: {func1([3, 1, 4, 8], 6)}')
    