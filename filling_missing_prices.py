# You are a data analyst for an online retailer. You've been given a dataset of product prices, 
# but some of the prices are missing. 
# You need to clean the data by filling in the missing prices with the median price of the available data.
# This will ensure that your analysis is accurate and that you don't inadvertently 
# skew your results by simply removing the missing data.

import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {'price': [100, 150, np.nan, 200, np.nan, 180, 120]}
df = pd.DataFrame(data)

# Print the DataFrame before filling missing values
print("Before filling missing values:")
print(df)

# Fill missing values with the median
### YOUR CODE HERE ###
media = df['price'].mean()
df['price'] = df['price'].fillna(media)
# Print the DataFrame after filling missing values
print("\nAfter filling missing values:")
print(df)