def fractional_knapsack(profit, weight, capacity):
    n = len(profit)

    # Calculate profit/weight ratio
    items = []
    for i in range(n):
        ratio = profit[i] / weight[i]
        items.append((ratio, profit[i], weight[i]))

    # Sort by decreasing ratio
    items.sort(reverse=True)

    total_profit = 0

    # Select items
    for ratio, p, w in items:
        if capacity >= w:
            capacity = capacity - w
            total_profit = total_profit + p
        else:
            total_profit = total_profit + p * (capacity / w)
            break

    return total_profit


# Given objects
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

# Find maximum profit
answer = fractional_knapsack(profit, weight, capacity)

print("Maximum Profit =", answer)
