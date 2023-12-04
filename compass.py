import pandas as pd
import matplotlib.pyplot as plt

file_path = 'compass.csv'
data = pd.read_csv(file_path)

plt.figure(figsize=(12, 10))

for i in range(len(data)):
    plt.scatter(data['Religous-related (X-axis)'][i], data['State-related (Y-axis)'][i], s=100) # Increased marker size
    plt.text(data['Religous-related (X-axis)'][i] + 0.2,  # Adding a small offset to the text for readability
             data['State-related (Y-axis)'][i] + 0.2, 
             data['Administrator'][i], 
             fontsize=10,
             ha='right')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('CU/BC Admin on mentions', fontsize=14)
plt.xlabel('(Anti-Semitism-related - Islamophobia-related)', fontsize=12)
plt.ylabel('Israel-related - Palestine-related', fontsize=12)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.savefig('political_compass.svg', format='svg', bbox_inches='tight', facecolor='w')

plt.show()