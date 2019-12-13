import math

def mergeSort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    left = 0
    right = len(arr) - 1
    mid = math.floor((left + right) / 2)
    L = arr[left : mid + 1]
    R = arr[mid + 1 : right + 1]
    leftSorted = mergeSort(L)
    rightSorted = mergeSort(R)
    result = merge(leftSorted, rightSorted)
    return result

def merge(leftSorted, rightSorted):
    result = []
    n = len(leftSorted)
    m = len(rightSorted)
    left = 0
    right = 0
    while left < n and right < m:
        if leftSorted[left] < rightSorted[right]:
            result.append(leftSorted[left])
            left += 1
        else:
            result.append(rightSorted[right])
            right += 1
    while left < n:
        result.append(leftSorted[left])
        left += 1
    while right < m:
        result.append(rightSorted[right])
        right += 1
    return result

if __name__ == "__main__":
    arr = [6, 3, 4, 1, 3, 5, 2]
    print(mergeSort(arr))