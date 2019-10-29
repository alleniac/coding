def func1(weights, profits, capacity):
    # assume that len(weights) == len(profits)
    return dfs(weights, profits, capacity, 0, 0)

def dfs(weights, profits, capacity, crtWeight, index):
    n = len(weights)
    
    if n == 0 or index >= n or crtWeight > capacity:
        return 0
    
    # include myself
    profit1 = 0
    if weights[index] + crtWeight <= capacity:
        profit1 = profits[index] + dfs(weights, profits, capacity, crtWeight + weights[index], index)
    
    # not include myself
    profit2 = dfs(weights, profits, capacity, crtWeight, index + 1)

    return max(profit1, profit2)

if __name__ == '__main__':
    testWeights1 = [1, 2, 3]
    testProfits1 = [15, 20, 50]
    testCapacity1 = 5

    testWeights2 = [1, 3, 4, 5]
    testProfits2 = [15, 50, 60, 90]
    testCapacity2 = 8

    testWeights3 = [1, 3, 4, 5]
    testProfits3 = [15, 50, 60, 90]
    testCapacity3 = 6

    testWeights4 = [2, 3, 4, 5]
    testProfits4 = [35, 50, 60, 75]
    testCapacity4 = 100

    result1 = func1(testWeights1, testProfits1, testCapacity1)
    print(f'func1 result1: {result1}')

    result2 = func1(testWeights2, testProfits2, testCapacity2)
    print(f'func1 result2: {result2}')

    result3 = func1(testWeights3, testProfits3, testCapacity3)
    print(f'func1 result3: {result3}')

    result4 = func1(testWeights4, testProfits4, testCapacity4)
    print(f'func1 result3: {result4}')
