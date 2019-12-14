def quickSort(arr, start, end):
    if start >= end:
        return

    pivot = arr[end]
    i, j = start, end - 1
    while i <= j:
        if arr[i] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    arr[i], arr[end] = arr[end], arr[i]

    quickSort(arr, start, i - 1)
    quickSort(arr, i + 1, end)

    return

if __name__ == "__main__":
    arr = [6, 4, 1, 4, 5, 2, 3, 3, 10]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)