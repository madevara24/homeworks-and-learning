import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

wtdf = pd.read_csv('wt.csv')
cycle_counts = wtdf['cycle_uuid'].value_counts()
print("\nCycle UUID with most rows:")
print(cycle_counts.head(1))

cycle_subset = wtdf[wtdf['cycle_uuid'] == '17901a85-352b-d41f-a5b1-3f519f3537a2']
cycle_subset = cycle_subset.dropna(subset=['temperature'])

print(cycle_subset.describe())

# Remove rows with 0 values for specified columns
columns_to_check = ['temperature', 'ph', 'do', 'water_height', 'water_clarity', 'tds']
cycle_subset = cycle_subset[(cycle_subset[columns_to_check] != 0).all(axis=1)]

print("\nAfter removing 0 values:")
print(cycle_subset.describe())

# Create figure with two y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Plot other sensors on primary y-axis
other_columns = ['temperature', 'ph', 'do', 'water_height', 'water_clarity']
for column in other_columns:
    ax1.plot(cycle_subset['time'], cycle_subset[column], label=column)

# Plot TDS on secondary y-axis
ax2.plot(cycle_subset['time'], cycle_subset['tds'], label='tds', color='purple', linestyle='--')

ax1.set_xlabel('Time Index')
ax1.set_ylabel('Sensor Values')
ax2.set_ylabel('TDS Value')
ax1.set_title('Sensor Values Over Time')
ax1.grid(True)

# Add legends for both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right')

plt.tight_layout()
plt.show()
