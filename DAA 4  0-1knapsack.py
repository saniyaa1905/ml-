
# DAA Practical 4: 0/1 Knapsack using Dynamic Programming

# Accept number of items
n = int(input("Enter number of items: "))

weights = []
profits = []

# Accept weights and profits
for i in range(n):
    w = int(input(f"Enter weight of item {i+1}: "))
    p = int(input(f"Enter profit of item {i+1}: "))

    weights.append(w)
    profits.append(p)

# Accept knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for j in range(1, capacity + 1):

        if weights[i - 1] <= j:
            dp[i][j] = max(
                dp[i - 1][j],
                profits[i - 1] + dp[i - 1][j - weights[i - 1]]
            )
        else:
            dp[i][j] = dp[i - 1][j]

# Display maximum profit
print("\nMaximum Profit:", dp[n][capacity])

# Find selected items
selected_items = []
j = capacity

for i in range(n, 0, -1):
    if dp[i][j] != dp[i - 1][j]:
        selected_items.append(i)
        j -= weights[i - 1]

selected_items.reverse()

print("Selected Items:", selected_items)
