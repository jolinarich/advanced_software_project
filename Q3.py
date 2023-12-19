# Find the largest possible profit
current_max_val = float('-inf')
max_profit_val = 0

for price in reversed(apple_prices):
    current_max_val = max(current_max_val, price)
    potential_profit = current_max_val - price
    max_profit_val = max(potential_profit, max_profit_val)

print("Largest Possible Profit: $", max_profit_val)
