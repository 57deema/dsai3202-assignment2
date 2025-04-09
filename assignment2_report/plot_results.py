import matplotlib.pyplot as plt

# Metrics
categories = ['Time (s)', 'Moves', 'Backtracks']
original = [0.29, 590, 1]
enhanced = [0.20, 505, 0]

x = range(len(categories))

plt.figure(figsize=(8, 5))
bar1 = plt.bar([i - 0.2 for i in x], original, width=0.4, label='Original Explorer')
bar2 = plt.bar([i + 0.2 for i in x], enhanced, width=0.4, label='Enhanced Explorer')

# Labeling
plt.xticks(x, categories)
plt.ylabel("Values")
plt.title("Original vs Enhanced Explorer Comparison")
plt.legend()

# Save to file
plt.savefig("assignment2_report/results_plot.png")
plt.show()
