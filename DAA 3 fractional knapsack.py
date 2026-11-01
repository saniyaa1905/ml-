
# DAA Practical 3: Fractional Knapsack using Greedy Method

# Accept number of items
n = int(input("Enter number of items: "))

weights = []
profits = []

# Accept weight and profit of each item
for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    p = float(input(f"Enter profit of item {i+1}: "))

    weights.append(w)
    profits.append(p)

# Accept knapsack capacity
capacity = float(input("Enter knapsack capacity: "))

# Calculate profit-to-weight ratio
ratio = []

for i in range(n):
    ratio.append(profits[i] / weights[i])

# Sort items in descending order of ratio
items = sorted(
    zip(ratio, weights, profits),
    reverse=True
)

total_profit = 0

# Select items using Greedy Method
for r, w, p in items:

    if capacity >= w:
        # Take the complete item
        capacity -= w
        total_profit += p

    else:
        # Take the fractional part of the item
        total_profit += r * capacity
        break

# Display maximum profit
print("\nMaximum Profit:", total_profit)
