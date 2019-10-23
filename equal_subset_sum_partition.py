def func1(arr):
    total = sum(arr)
    if total % 2 == 1:
        return False
    return dfs(arr, 0, 0)

def dfs(arr, index, crtSum):
    if index >= len(arr):
        return False
    if crtSum == sum(arr) / 2:
        return True

    return dfs(arr, index + 1, crtSum + arr[index]) or dfs(arr, index + 1, crtSum) 

if __name__ == "__main__":
    print(func1([1, 2, 3, 4]))
    print(func1([1, 1, 3, 4, 7]))
    print(func1([2, 3, 4, 6]))
    print(func1([1, 5, 11, 9]))
    print(func1([1, 5, 11, 7]))
    print(func1([1, 3]))