def knapsack(weights, profits, capacity):
    return dfs(weights, profits, capacity, 0)

def dfs(weights, profits, capacity, index):
    # base case
    if capacity < 0 or index >= len(profits):
        return 0
    
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + dfs(weights, profits, capacity - weights[index], index + 1)
    
    profit2 = dfs(weights, profits, capacity, index + 1)

    return max(profit1, profit2)

if __name__ == "__main__":
    print(knapsack([1, 2, 3, 5], [1, 6, 10, 16], 7))
    print(knapsack([1, 2, 3, 5], [1, 6, 10, 16], 6))

