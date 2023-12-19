with open("sample_AAPL_for_mac_users.txt", "r") as file:
    lines = file.read().splitlines()
    apple_prices = [float(price) for price in lines]

import statistics

# Calculate the mean (average)
mean_price = statistics.mean(apple_prices)

# Calculate the standard deviation
std_deviation = statistics.stdev(apple_prices)

print("Mean Price:", mean_price)
print("Standard Deviation:", std_deviation)
