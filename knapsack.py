import time

def knapsack(weights, profits, capacity):
    return dfs(weights, profits, capacity, 0)

def knapsack_with_memo(weights, profits, capacity):
    memo = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return dfs_with_memo(memo, weights, profits, capacity, 0)

def knapsack_dp(weights, profits, capacity):
    dp = [[0 for x in range(capacity + 1)] for y in range(len(profits))]

    # comment out because they are already 0
    # for i in range(len(profits)):
    #     dp[i][0] = 0
    
    for j in range(1, capacity + 1):
        if weights[0] <= j:
            dp[0][j] = profits[0]
    
    for i in range(1, len(profits)):
        for j in range(1, capacity + 1):
            if weights[i] <= j:
                dp[i][j] = max(dp[i - 1][j], profits[i] + dp[i - 1][j - weights[i]])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[len(profits) - 1][capacity]

def dfs(weights, profits, capacity, index):
    # base case
    if capacity < 0 or index >= len(profits):
        return 0
    
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + dfs(weights, profits, capacity - weights[index], index + 1)
    
    profit2 = dfs(weights, profits, capacity, index + 1)

    return max(profit1, profit2)

def dfs_with_memo(memo, weights, profits, capacity, index):
    # base case:
    if capacity < 0 or index >= len(profits):
        return 0
    
    if memo[index][capacity] != -1:
        return memo[index][capacity]
    
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + dfs_with_memo(memo, weights, profits, capacity - weights[index], index + 1)
    
    profit2 = dfs_with_memo(memo, weights, profits, capacity, index + 1)

    memo[index][capacity] = max(profit1, profit2)
    return memo[index][capacity]

if __name__ == "__main__":
    start = time.perf_counter()
    print(knapsack([1, 2, 3, 5], [1, 6, 10, 16], 7))
    print(knapsack([1, 2, 3, 5], [1, 6, 10, 16], 6))
    end = time.perf_counter()
    print(f'time for recursive function: {end - start}')

    start = time.perf_counter()
    print(knapsack_with_memo([1, 2, 3, 5], [1, 6, 10, 16], 7))
    print(knapsack_with_memo([1, 2, 3, 5], [1, 6, 10, 16], 6))
    end = time.perf_counter()
    print(f'time for recursive function with memo: {end - start}')

    start = time.perf_counter()
    print(knapsack_dp([1, 2, 3, 5], [1, 6, 10, 16], 7))
    print(knapsack_dp([1, 2, 3, 5], [1, 6, 10, 16], 6))
    end = time.perf_counter()
    print(f'time for dp: {end - start}')
