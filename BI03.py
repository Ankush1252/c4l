import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100) *100
})

data['C'] = data['A'] * data['B']

plt.figure(figsize=(10,6))
plt.scatter(data['A'], data['C'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Transformed Data')
plt.xlabel('A')
plt.ylabel('C')
plt.grid(True)
plt.show()