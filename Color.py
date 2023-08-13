from collections import Counter
import random

# the color data provided as a list
colors = ["green", "yellow", "green", "brown",  "red", "blue", "pink", "blue", "yellow", "orange", "cream", "orange", "red", "white", "blue", "white", "blue", "blue", "blue", "green", "arsh", "brown", "green", "brown", "blue", "blue", "blew", "pink", "pink", "orange", "orange", "red", "white", "blue", "white", "white", "blue", "blue", "blue", "green", "yellow", "green", "brown", "blue", "pink", "red", "yellow", "orange", "red", "orange", "red", "blue", "blue", "white", "blue", "blue", "white", "white", "blue", "blue", "green", "white", "blue", "brown", "pink", "yellow", "orange", "cream", "orange", "red", "white", "blue", "white", "blue", "blue", "blue", "green", "green", "white", "green", "brown", "blue", "blue", "black", "white", "orange", "red", "red", "red", "white", "blue", "white", "blue", "blue", "blue", "white"]

# Calculate mean color
mean_color = max(Counter(colors), key=Counter(colors).get)

# Calculate mode (most frequent) color
mode_color = Counter(colors).most_common(1)[0][0]

# Calculate median color
sorted_colors = sorted(colors)
middle_index = len(sorted_colors) // 2
median_color = sorted_colors[middle_index]

# Calculate variance
color_frequencies = Counter(colors)
total_colors = len(colors)
variance = sum((color_frequencies[color] / total_colors) * (color_frequencies[color] / total_colors) for color in color_frequencies)

# Calculate probability of red color
probability_red = color_frequencies.get("red", 0) / total_colors

# Save colors and frequencies in PostgreSQL (Replace with actual connection details) i have none
# conn = psycopg2.connect("dbname=test user=postgres password=yourpassword host=localhost")
# cur = conn.cursor()

'''for color, frequency in color_frequencies.items():
    cur.execute("INSERT INTO color_data (color, frequency) VALUES (%s, %s)", (color, frequency))

conn.commit()
cur.close()
conn.close()'''

# Recursive searching algorithm
def recursive_search(arr, target, index=0):
    if index >= len(arr):
        return False
    if arr[index] == target:
        return True
    return recursive_search(arr, target, index + 1)

# Generate random 4-digit binary number and convert to base 10
binary_number = "".join(str(random.randint(0, 1)) for _ in range(4))
decimal_number = int(binary_number, 2)

# Sum the first 50 Fibonacci sequence
def fibonacci_sum(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return sum(fib)

fibonacci_sum_50 = fibonacci_sum(50)
# Print results
print("Mean Color:", mean_color)
print("Most Frequent Color:", mode_color)
print("Median Color:", median_color)
print("Variance:", variance)
print("Probability of Red:", probability_red)
print("Recursive Search:", recursive_search([1, 2, 3, 4, 5], 3))
print("Generated Binary Number:", binary_number)
print("Converted Decimal Number:", decimal_number)
print("Sum of First 50 Fibonacci Numbers:", fibonacci_sum_50)