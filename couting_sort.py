def countingSort(arr):
    count = [0 for _ in range(max(arr) + 1)]
    for num in arr:
        count[num] += 1
    total = 0
    for i in range(len(count)):
        total = count[i] + total
        count[i] = total
    output = []
    startIndex = 0
    for i in range(len(count)):
        endIndex = count[i]
        output.extend([i for _ in range(startIndex, endIndex)])
        startIndex = endIndex
    print(arr)
    print(output)
    
if __name__ == '__main__':
    countingSort([0, 5, 2, 5, 4, 1, 3, 0, 6, 6, 1])
    countingSort([5, 2, 5, 4, 1, 10, 6, 6, 1])