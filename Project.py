import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('madurai_top10_coaching.csv')
if 'Fees' not in df.columns:
    df['Fees'] = [50000, 40000, 35000, 45000, 48000, 30000, 37000, 32000, 42000, 39000]
if 'Rating' not in df.columns:
    df['Rating'] = [4.5, 4.3, 4.7, 4.4, 4.2, 4.1, 4.6, 4.0, 4.3, 4.5]
df['Specialisation_Count'] = df['Specialisation'].apply(lambda x: len(str(x).split('/')))
plt.figure(figsize=(12, 6))
bar_width = 0.25
x = np.arange(len(df))

plt.bar(x - bar_width, df['Specialisation_Count'], width=bar_width, label='Specialisations', color='teal')
plt.bar(x, df['Fees'] / 10000, width=bar_width, label='Fees (×10k)', color='orange')
plt.bar(x + bar_width, df['Rating'], width=bar_width, label='Rating', color='purple')

plt.xlabel('Coaching Centres')
plt.ylabel('Value')
plt.title('Madurai Top 10 Coaching Centres — Fees, Rating & Specialisations')
plt.xticks(x, df['Name'], rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
print(df[['Name', 'Specialisation_Count', 'Fees', 'Rating']])
