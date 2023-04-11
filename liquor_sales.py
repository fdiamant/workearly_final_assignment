import pandas as pd
import matplotlib.pyplot as plt

# set this option to display all columns in PyCharm console
# See https://pandas.pydata.org/docs/user_guide/options.html
# display.width : int
#     Width of the display in characters. In case python/IPython is running in
#     a terminal this can be set to None and pandas will correctly auto-detect
#     the width.
pd.options.display.width = 0

# Import the data
df = pd.read_csv('liquor_sales.csv')

# Check for missing values
missing = df[df.isna().any(axis=1)]
# calculate percentage of missing values per column
missing_percentages = round((df.isna().mean() * 100), 2)
# Print the results
print('Rows with missing or null values:\n', missing)
print('Percentage of missing values per column:\n', missing_percentages)
# Export missing values for reference
# missing.to_csv('missing_values.csv', sep=';')





