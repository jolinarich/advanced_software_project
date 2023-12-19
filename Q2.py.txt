import matplotlib.pyplot as plt
import statistics

# Load data from the file
with open("sample_AAPL_for_mac_users.txt", "r") as file:
    lines = file.read().splitlines()
    apple_prices = [float(price) for price in lines]

# Calculate the mean and standard deviation
mean_price = statistics.mean(apple_prices)
std_deviation = statistics.stdev(apple_prices)

print("Mean Price:", mean_price)
print("Standard Deviation:", std_deviation)

# Create a line graph
x = list(range(1, 253))  # 1 to 252 trading days
plt.plot(x, apple_prices)
plt.title("Apple Stock Price, Nov 2019 to Nov 2020")
plt.xlabel("Day")
plt.ylabel("Trading Price")
plt.show()
